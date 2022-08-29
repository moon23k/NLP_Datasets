## 💾 NLP_datasets
This repo covers a set of ways to fetch NLP data and process it into a form that the model can take.

<br>

## NMT_Datasets


### IWSLT 2017
> IWSLT refers to "The International Workshop on Spoken Language Translation". It is is a yearly scientific workshop which is associated with an open evaluation campaign on spoken language translation. Here, we only covers En-De Translation Dataset from "The IWSLT 2017 Evaluation Campaign".

<br>

### Multi30k

<br>

### WMT14

<br>

### KoEn
> This dir deals with Korean-English Translation Dataset, which provided from AI_Hub. The original name for this dataset is "한국어-영어 번역(병렬) 말뭉치", and it is available with permission from the AI_Hub web. So, excluding downloading, this dir only covers data processing under the assumption that the original file has been fetched. The original file [한국어-영어 번역(병렬) 말뭉치](https://aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&aihubDataSe=realm&dataSetSn=126) can be fetched from this link.

The Dataset consist of 10 sub-datasets, but only uses 7 like below.

    * 1_구어체(1).xlsx, 1_구어체(2).xlsx 
    * 2_대화체.xlsx
    * 3.문어체_뉴스(1).xlsx, 3.문어체_뉴스(2).xlsx, 3.문어체_뉴스(3).xlsx, 3.문어체_뉴스(4).xlsx

The total size of data is approximately 1.3M.


<br>



<br>


## Dialogue

**Daily**
<br>

**Empathetic**
<br>

**Persona**
<br>

**Blended**
<br>

**HIMYM Script**

<br>

## Summarization

<br>

### How to use
```
git clone https://github.com/moon23k/NLP_datasets
python3 -m pip freeze >requirements.txt
bash the_data_you_want/download_dataset.sh
```
