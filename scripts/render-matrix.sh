#!/bin/zsh
# usage: render-matrix.sh <project> [--4k <format>] [--only <format>]   (NOSHARP=1 env: native 1080 capture, faster drafts)
# For each format in film.json "formats": refuse below 12 GB free, rsync the project to /tmp/rm-<name>-<fmt>,
# set-format.py there, render 60 fps delivery quality (--workers 3 at 1080 class; with --4k <fmt>: that format
# renders --resolution <render4k> --workers 4 HF_CAPTURE_PARALLEL_STREAM=true), write
# <project>/renders/<name>-<fmt>[-4k].mp4, run qa/run-all.sh on it, delete the /tmp copy and work-* dirs.
SKILL=${0:A:h:h}
PROJ=${1:A}; shift
FOURK=""; ONLY=""
while (( $# )); do case $1 in --4k) FOURK=$2; shift 2;; --only) ONLY=$2; shift 2;; *) echo "bad arg $1"; exit 1;; esac; done
NAME=${PROJ:t}
FORMATS=($(python3 -c "import json;print(' '.join(json.load(open('$PROJ/film.json'))['formats']))"))
[[ -n $ONLY ]] && FORMATS=($ONLY)
mkdir -p $PROJ/renders $PROJ/qa
typeset -a SUM
for F in $FORMATS; do
  FREE=$(df -g ~ | awk 'NR==2{print $4}')
  if (( FREE < 12 )); then echo "refusing: only ${FREE} GB free (need 12)"; SUM+=("$F | refused: ${FREE} GB free"); break; fi
  TMP=/tmp/rm-$NAME-$F
  rm -rf $TMP; mkdir -p $TMP
  rsync -a --exclude renders --exclude .hyperframes --exclude 'audio/vo/*/whisper' --exclude 'work-*' --exclude node_modules --exclude qa $PROJ/ $TMP/
  mkdir -p $TMP/renders $TMP/qa
  python3 $SKILL/scripts/set-format.py $TMP $F >/dev/null || { SUM+=("$F | set-format failed"); continue; }
  SUFFIX=""; ARGS=(--workers 3); ENVV=(); SHARP=""
  R4=$(python3 -c "import json;print(json.load(open('$SKILL/formats/presets.json'))['$F']['render4k'])")
  if [[ $F == $FOURK ]]; then
    [[ $R4 == None ]] && { echo "$F has no 4k preset"; SUM+=("$F | no 4k preset"); continue; }
    SUFFIX=-4k; ARGS=(--workers 4 --resolution $R4); ENVV=(HF_CAPTURE_PARALLEL_STREAM=true)
  elif [[ $R4 != None && -z $NOSHARP ]]; then
    # 1080 deliverables are rendered at 4K and downscaled (lanczos, ~CRF 15): a native 1080 capture looked soft 
    SHARP=1; ARGS=(--workers 4 --resolution $R4); ENVV=(HF_CAPTURE_PARALLEL_STREAM=true)
  fi
  OUT=$PROJ/renders/$NAME-$F$SUFFIX.mp4
  RAW=$OUT; [[ -n $SHARP ]] && RAW=$TMP/raw-4k.mp4
  T0=$SECONDS
  (cd $TMP && env $ENVV npx -y hyperframes@0.8.183 render --fps 60 --quality high $ARGS --output $RAW --quiet >$TMP/render.log 2>&1)
  rc=$?
  if [[ $rc == 0 && -n $SHARP && -f $RAW ]]; then
    WH=$(python3 -c "import json;d=json.load(open('$SKILL/formats/presets.json'))['$F'];print(f\"{d['w']}:{d['h']}\")")
    ffmpeg -v error -y -i $RAW -vf "scale=${WH}:flags=lanczos" -c:v libx264 -preset slow -crf 15 -profile:v high -pix_fmt yuv420p -r 60 -c:a copy -movflags +faststart $OUT; rc=$?
    rm -f $RAW
  fi
  if [[ $rc != 0 || ! -f $OUT ]]; then tail -5 $TMP/render.log; SUM+=("$F$SUFFIX | render failed (rc $rc)"); rm -rf $TMP; continue; fi
  # HyperFrames' render audio path lands 0.7-1.9 LU under the mastered mix: mux audio/mix.wav straight onto the picture
  if [[ -f $PROJ/audio/mix.wav ]]; then
    ffmpeg -v error -y -i $OUT -i $PROJ/audio/mix.wav -map 0:v -map 1:a -c:v copy -c:a aac -b:a 256k -shortest $OUT.mux.mp4 && mv $OUT.mux.mp4 $OUT
  fi
  QA_OUT=$PROJ/qa $SKILL/qa/run-all.sh $TMP $OUT $F >$PROJ/qa/run-$F$SUFFIX.log 2>&1; qrc=$?
  SUM+=("$F$SUFFIX | $(( SECONDS - T0 )) s | $(du -h $OUT | cut -f1) | qa rc $qrc ($(grep -cE '^PASS' $PROJ/qa/run-$F$SUFFIX.log) pass, $(grep -cE '^WARN' $PROJ/qa/run-$F$SUFFIX.log) warn, $(grep -cE '^FAIL' $PROJ/qa/run-$F$SUFFIX.log) fail)")
  rm -rf $TMP $PROJ/work-*(N) $TMP/work-*(N)
done
echo; echo "| format | time | size | qa |"; echo "|---|---|---|---|"; for s in $SUM; do echo "| $s |"; done
df -h ~ | tail -1 | awk '{print "free: "$4}'
