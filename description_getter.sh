SCRIPT_DIR=./
OUTPUT_FILE=./output.txt
TMP_FILE=/tmp/tmp.txt

python $SCRIPT_DIR/description_getter.py | sed 's/^  *//g' >> $OUTPUT_FILE
sort $OUTPUT_FILE | uniq > $TMP_FILE
cat $TMP_FILE > $OUTPUT_FILE
