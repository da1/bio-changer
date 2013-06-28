set e
SCRIPT_DIR=${0%/*}
OUTPUT_FILE=$SCRIPT_DIR/output.txt
TMP_FILE=/tmp/tmp.txt

python $SCRIPT_DIR/description_getter.py | sed 's/^  *//g' >> $OUTPUT_FILE
sort $OUTPUT_FILE | uniq > $TMP_FILE
cat $TMP_FILE > $OUTPUT_FILE
