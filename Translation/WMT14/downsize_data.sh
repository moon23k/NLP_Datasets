#!/bin/bash

cd data
mkdir -p wmt_sm

langs=(en de)


#split train dataset
for lang in "${langs[@]}"; do
    awk '{if (NR % 143 == 0)  print $0; }' wmt/train.$lang > wmt_sm/train.$lang
done


#split valid dataset
for lang in "${langs[@]}"; do
    awk '{if (NR % 2 == 0)  print $0; }' wmt/valid.$lang > wmt_sm/valid.$lang
done


#split test dataset
for lang in "${langs[@]}"; do
    awk '{if (NR % 3 == 0)  print $0; }' wmt/test.$lang > wmt_sm/test.$lang
done



for l in "${langs[@]}"; do
    sed -n '1, 30000p' wmt_sm/train.$l > wmt_sm/tmp_train.$l
    rm wmt_sm/train.$l
    mv wmt_sm/tmp_train.$l wmt_sm/train.$l
done


evals=(valid test)
for split in "${evals[@]}"; do
    for l in "${langs[@]}"; do
        sed -n '1, 1000p' wmt_sm/${split}.$l > wmt_sm/tmp_${split}.$l
        rm wmt_sm/${split}.$l
        mv wmt_sm/tmp_${split}.$l wmt_sm/${split}.$l
    done
done