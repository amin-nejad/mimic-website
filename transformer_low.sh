#!/bin/bash

TEST_FILE=input.txt

PROBLEM=mimic_discharge_summaries
MODEL=transformer
HPARAMS=transformer_base
DATA_DIR=/mimic/data/t2t_experiments/transformer/low_resource/full_context/data
TRAIN_DIR=/mimic/data/t2t_experiments/transformer/low_resource/full_context/output
USR_DIR=.

BEAM_SIZE=4
ALPHA=0.6
DBS=4
EXTRA_LEN=50
HPARAMS_OVERRIDE="max_length=10000,max_target_seq_length=512,max_input_seq_length=512"

CUDA_VISIBLE_DEVICES=0 t2t-decoder \
    --t2t_usr_dir=$USR_DIR \
    --data_dir=$DATA_DIR \
    --problem=$PROBLEM \
    --model=$MODEL \
    --hparams_set=$HPARAMS \
    --hparams=$HPARAMS_OVERRIDE \
    --output_dir=$TRAIN_DIR \
    --decode_hparams="beam_size=$BEAM_SIZE,alpha=$ALPHA,batch_size=$DBS,extra_length=$EXTRA_LEN" \
    --decode_from_file=$TEST_FILE \
    --decode_to_file=output.txt