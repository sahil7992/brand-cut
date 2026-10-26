#!/bin/zsh
# usage: new-film.sh <brand> <film-dir> <format> [format...] [--palette <id>]
# Scaffolds a HyperFrames film project themed by brands/<brand>/brand.json:
#   index.html (brand block + scene slots), film.json, SPEC.md, audio/ stubs, qa/,
#   brand assets copied in under assets/. First format = the authoring format;
#   render-matrix.sh renders the rest by copying the project and running set-format.py.
set -e
SKILL=${0:A:h:h}
BRAND=$1; DIR=${2:A}; shift 2
FORMATS=(); PALETTE=""
while (( $# )); do
  if [[ $1 == --palette ]]; then PALETTE=$2; shift 2; else FORMATS+=$1; shift; fi
done
[[ -f $SKILL/brands/$BRAND/brand.json ]] || { echo "no brand $BRAND"; exit 1; }
(( ${#FORMATS} )) || FORMATS=(16x9)
[[ -e $DIR/index.html ]] && { echo "$DIR already has index.html"; exit 1; }
mkdir -p $DIR/{compositions,assets,audio/vo,audio/music,qa,renders}
NAME=${DIR:t}
cp $SKILL/templates/project/{hyperframes.json,CLAUDE.md} $DIR/
sed "s/__NAME__/$NAME/" $SKILL/templates/project/package.json > $DIR/package.json
print -r -- "{\"id\": \"$NAME\", \"name\": \"$NAME\"}" > $DIR/meta.json
cp $SKILL/templates/index.html $DIR/index.html
cp -R $SKILL/brands/$BRAND/assets/. $DIR/assets/
KIT=$SKILL/brands/$BRAND/kit; [[ -d $KIT ]] || KIT=$SKILL/shared/uikit
mkdir -p $DIR/shared && cp $SKILL/shared/*.js $DIR/shared/ && cp $KIT/* $DIR/shared/
ffmpeg -v error -f lavfi -i anullsrc=r=48000:cl=stereo -t 1 $DIR/audio/mix.wav
python3 - "$DIR" "$BRAND" "$PALETTE" "${(j:,:)FORMATS}" <<'PY'
import json, sys
d, brand, pal, fmts = sys.argv[1:5]
json.dump({"brand": brand, "palette": pal or None, "format": fmts.split(",")[0], "formats": fmts.split(",")}, open(f"{d}/film.json", "w"), indent=2)
PY
python3 $SKILL/scripts/set-format.py $DIR $FORMATS[1]
sed "s/__NAME__/$NAME/g; s/__BRAND__/$BRAND/g; s/__FORMATS__/${(j:, :)FORMATS}/g" $SKILL/templates/SPEC.md > $DIR/SPEC.md
print -r -- "# One line per VO line. No ellipses, no dashes, no fillers. vo.py reads this." > $DIR/audio/vo/script.txt
print -r -- '{"music": {"file": "", "offset": 0, "gain_db": -3.5}, "vo": {"file": "audio/vo/vo.wav", "start": 0}, "sfx": [], "platform": "instagram"}' > $DIR/audio/events.json
print "scaffolded $DIR ($BRAND, ${(j:, :)FORMATS})"
