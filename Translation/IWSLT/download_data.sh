#!/bin/bash
#Adopted from https://github.com/facebookresearch/fairseq/blob/main/examples/translation/prepare-iwslt14.sh

mkdir -p iwslt
cd iwslt

wget "http://dl.fbaipublicfiles.com/fairseq/data/iwslt14/de-en.tgz"
tar zxvf de-en.tgz
rm de-en.tgz

langs=(en de)

for l in "${langs[@]}"; do
    f_in=de-en/train.tags.de-en.$l
    f_out=de-en/train_orig.$l

    cat $f_in \
    | grep -v '<url>' \
    | grep -v '<talkid>' \
    | grep -v '<keywords>' \
    | grep -v '<speaker>' \
    | grep -v '<reviewer' \
    | grep -v '<translator' \
    | grep -v '<doc' \
    | grep -v '</doc>' \
    | sed -e 's/<title>//g' \
    | sed -e 's/<\/title>//g' \
    | sed -e 's/<description>//g' \
    | sed -e 's/<\/description>//g' \
    | sed 's/^\s*//g' \
    | sed 's/\s*$//g' \
    > $f_out
done


for l in "${langs[@]}"; do
    for o in `ls de-en/IWSLT*.TED*.de-en.$l.xml`; do
        fname=${o##*/}
        f=de-en/${fname%.*}
        grep '<seg id' $o \
        | sed -e 's/<seg id="[0-9]*">\s*//g' \
        | sed -e 's/\s*<\/seg>\s*//g' \
        | sed -e "s/\Ã¢â‚¬â„¢/\'/g" \
        > $f
        rm $o
    done
done   


for l in "${langs[@]}"; do
    awk '{if (NR%23 == 0)  print $0; }' de-en/train_orig.$l > valid.$l
    awk '{if (NR%23 != 0)  print $0; }' de-en/train_orig.$l > train.$l

    cat de-en/IWSLT14.TED.dev2010.de-en.$l \
        de-en/IWSLT14.TEDX.dev2012.de-en.$l \
        de-en/IWSLT14.TED.tst2010.de-en.$l \
        de-en/IWSLT14.TED.tst2011.de-en.$l \
        de-en/IWSLT14.TED.tst2012.de-en.$l \
        > test.$l
done

rm -r de-en
