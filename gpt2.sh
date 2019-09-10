#!/bin/bash

export CUDA_VISIBLE_DEVICES=0

cd ../text-generation/gpt2/gpt-2

MODEL='original'
DATA_DIR=/mimic/data/gpt2/
INPUT_FILE=~/project/mimic-website/input.txt
OUTPUT_FILE=~/project/mimic-website/output.txt
TOP_K=0
TEMP=1
BS=1

python src/generate_conditional_samples.py --input_file $INPUT_FILE --output_file $OUTPUT_FILE --model_name $MODEL --top_k $TOP_K --temperature $TEMP --batch_size $BS