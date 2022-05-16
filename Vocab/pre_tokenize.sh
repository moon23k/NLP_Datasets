#!/bin/bash

#Peer Tokenize with sacremoses
python3 -m pip install -U sacremoses
for dataset in "${datasets[@]}"; do
    for split in "${splits[@]}"; do
        for lang in "${langs[@]}"; do
            mkdir -p ${dataset}/tok
            sacremoses -l ${lang} -j 8 tokenize < ${dataset}/raw/${split}.${lang} > ${dataset}/tok/${split}.${lang}
        done
    done
done