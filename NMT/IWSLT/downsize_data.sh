#!/bin/bash

cd data
mkdir -p iwslt_sm


langs=(en de)

#split train dataset
for lang in "${langs[@]}"; do
    awk '{if (NR % 5 == 0)  print $0; }' iwslt/train.$lang > iwslt_sm/train.$lang
done


#split valid dataset
for lang in "${langs[@]}"; do
    awk '{if (NR % 7 == 0)  print $0; }' iwslt/valid.$lang > iwslt_sm/valid.$lang
done


#split test dataset
for lang in "${langs[@]}"; do
    awk '{if (NR % 6 == 0)  print $0; }' iwslt/test.$lang > iwslt_sm/test.$lang
done



for l in "${langs[@]}"; do
    sed -n '1, 30000p' iwslt_sm/train.$l > iwslt_sm/tmp_train.$l
    rm iwslt_sm/train.$l
    mv iwslt_sm/tmp_train.$l iwslt_sm/train.$l
done


evals=(valid test)
for split in "${evals[@]}"; do
    for l in "${langs[@]}"; do
        sed -n '1, 1000p' iwslt_sm/${split}.$l > iwslt_sm/tmp_${split}.$l
        rm iwslt_sm/${split}.$l
        mv iwslt_sm/tmp_${split}.$l iwslt_sm/${split}.$l
    done
done