#!/bin/zsh
# usage: run-all.sh <project> <video> <format>      env QA_OUT=<dir> to write the report elsewhere (default <project>/qa)
# Gates: hyperframes check, framecheck, flashcheck, safezone (9x16 4x5 1x1), claims, loudness, fps == 60, size.
# Writes QA-<format>.md with PASS/WARN/FAIL per gate. exit 0 no FAIL, 2 any FAIL.
SKILL=${0:A:h:h}
PROJ=${1:A}; VIDEO=${2:A}; FMT=$3
OUT=${QA_OUT:-$PROJ/qa}; mkdir -p $OUT
REPORT=$OUT/QA-$FMT.md
PY="uvx --python 3.12 --with numpy --with pillow python -I"
typeset -a ROWS; FAIL=0
gate() { ROWS+=("| $1 | $2 | $3 |"); [[ $2 == FAIL ]] && FAIL=1; print -r -- "$2 $1: $3"; }
LOG=$(mktemp -d)

# 1 hyperframes check
(cd $PROJ && npx -y hyperframes@0.8.183 check >$LOG/check.txt 2>&1); rc=$?
sed 's/\x1b\[[0-9;]*m//g' $LOG/check.txt > $LOG/check.clean
detail=$(grep -E "[0-9]+ error\(s\)" $LOG/check.clean | sed 's/^ *//' | tr '\n' ';' | cut -c1-160)
[[ $rc == 0 ]] && gate "hyperframes check" PASS "${detail:-exit 0}" || gate "hyperframes check" FAIL "exit $rc: ${detail:-see log}"

# 2 framecheck (jumps: hard cuts and floods show as big mean differences)
FPS=$(ffprobe -v error -select_streams v:0 -show_entries stream=r_frame_rate -of csv=p=0 $VIDEO | awk -F/ '{printf "%.3f", $1/$2}')
$=PY $SKILL/qa/framecheck.py $VIDEO $FPS >$LOG/frame.txt 2>&1
MAXJ=$(grep "biggest frame" $LOG/frame.txt | sed 's/np.float64(\([0-9.]*\))/\1/g' | grep -oE "\([0-9.]+, [0-9.]+\)" | tr -d '()' | awk -F', ' '{if($2>m)m=$2} END{print m+0}')
if (( MAXJ > 60 )); then gate framecheck WARN "max frame-to-frame jump $MAXJ (>60: hard cut or flood, check it is intended)"; else gate framecheck PASS "max frame-to-frame jump $MAXJ"; fi

# 3 flashcheck
$=PY $SKILL/qa/flashcheck.py $VIDEO --json $OUT/flash-$FMT.json >$LOG/flash.txt 2>&1; rc=$?
fl=$(tail -1 $LOG/flash.txt | cut -c1-160)
case $rc in 0) gate flashcheck PASS "$fl";; 1) gate flashcheck WARN "$fl";; *) gate flashcheck FAIL "$fl";; esac

# 4 safezone (feed and vertical formats)
if [[ $FMT == (9x16|4x5|1x1) ]]; then
  $=PY $SKILL/qa/safezone.py $VIDEO $FMT --out $OUT/safezone-$FMT.png >$LOG/sz.txt 2>&1; rc=$?
  sz=$(grep -E "^WARN band" $LOG/sz.txt | cut -c1-110 | tr '\n' ';')
  [[ $rc == 0 ]] && gate safezone PASS "no text-like detail in unsafe bands (sheet qa/safezone-$FMT.png)" || gate safezone WARN "${sz:-see sheet} (sheet qa/safezone-$FMT.png)"
else
  gate safezone PASS "n/a for $FMT (16:9 title safe is checked by eye)"
fi

# 5 claims
python3 $SKILL/qa/claims.py $PROJ >$LOG/claims.txt 2>&1; rc=$?
[[ $rc == 0 ]] && gate claims PASS "$(tail -1 $LOG/claims.txt)" || gate claims FAIL "$(grep -c '^FAIL' $LOG/claims.txt) finding(s), first: $(grep -m1 '^FAIL' $LOG/claims.txt | cut -c1-110)"

# 6 loudness of the video's audio
if ffprobe -v error -select_streams a:0 -show_entries stream=codec_name -of csv=p=0 $VIDEO | grep -q .; then
  ffmpeg -hide_banner -nostats -i $VIDEO -vn -af ebur128=peak=true -f null - 2>&1 | sed -n '/Summary:/,$p' > $LOG/lufs.txt
  I=$(grep -E "^\s+I:" $LOG/lufs.txt | awk '{print $2}'); TP=$(grep -E "^\s+Peak:" $LOG/lufs.txt | awk '{print $2}')
  st=$(awk -v i="$I" -v t="$TP" 'BEGIN{ if (i=="" ) print "FAIL"; else if (i<-15||i>-13||t>-0.9) print "FAIL"; else if (i<-14.5||i>-13.5) print "WARN"; else print "PASS"}')
  gate loudness $st "${I} LUFS, ${TP} dBTP (target -14 +-1, TP <= -1.0)"
else
  gate loudness FAIL "no audio stream"
fi

# 7 fps and size
read FW FH <<< $(ffprobe -v error -select_streams v:0 -show_entries stream=width,height -of csv=p=0 $VIDEO | tr ',' ' ')
EXP=$(python3 -c "import json;p=json.load(open('$SKILL/formats/presets.json'))['$FMT'];print(p['w'],p['h'])")
read EW EH <<< $EXP
[[ $FPS == 60.000 ]] && gate "fps" PASS "60" || gate "fps" FAIL "$FPS (must be 60)"
if [[ $FW == $EW && $FH == $EH ]] || [[ $FW == $((EW*2)) && $FH == $((EH*2)) ]]; then gate "size" PASS "${FW}x${FH}"; else gate "size" FAIL "${FW}x${FH}, expected ${EW}x${EH} (or 2x)"; fi

{
  print "# QA $FMT: ${VIDEO:t}"; print; print "Run $(date '+%Y-%m-%d %H:%M'). Overall: $([[ $FAIL == 0 ]] && echo PASS-or-WARN || echo FAIL)"; print
  print "| gate | result | detail |"; print "|---|---|---|"; print -l -- $ROWS
} > $REPORT
print "report: $REPORT"; rm -rf $LOG
exit $(( FAIL ? 2 : 0 ))
