#!/bin/bash

cd data
mkdir -p wmt
cd wmt

#Getting common crawl data for training
wget --trust-server-names http://www.statmt.org/wmt13/training-parallel-commoncrawl.tgz
tar zxvf training-parallel-commoncrawl.tgz
ls | grep -v 'commoncrawl.de-en.[de,en]' | xargs rm


#Getting europarl data for training
wget --trust-server-names http://www.statmt.org/wmt13/training-parallel-europarl-v7.tgz
tar zxvf training-parallel-europarl-v7.tgz
cd training && ls | grep -v 'europarl-v7.de-en.[de,en]' | xargs rm
cd .. && mv training/europarl* . && rm -r training training-parallel-europarl-v7.tgz


#Getting Valid and Test datset
wget --trust-server-names http://www.statmt.org/wmt14/test-filtered.tgz
wget --trust-server-names http://data.statmt.org/wmt17/translation-task/test.tgz
tar zxvf test-filtered.tgz && tar zxvf test.tgz
cd test && ls | grep -v '.*deen\|.*ende' | xargs rm
mv test/* . && rm -r test-filtered.tgz test.tgz test


#Concat common and euro datasets
cat commoncrawl.de-en.en europarl-v7.de-en.en > train.en
cat commoncrawl.de-en.de europarl-v7.de-en.de > train.de
rm common* euro*


wget -nc https://raw.githubusercontent.com/moses-smt/mosesdecoder/master/scripts/ems/support/input-from-sgm.perl


valid=newstest2014-deen
test=newstest2017-ende

perl input-from-sgm.perl < $valid-src.en.sgm > valid.en
perl input-from-sgm.perl < $valid-ref.de.sgm > valid.de
perl input-from-sgm.perl < $test-src.en.sgm > test.en
perl input-from-sgm.perl < $test-ref.de.sgm > test.de

rm news* input*
