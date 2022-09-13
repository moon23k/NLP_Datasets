## 💾 NLP_datasets
This repo covers a set of ways to fetch NLP data and process it into a form that the model can take.

<br>

## Translation

**IWSLT 2017**
> IWSLT refers to "The International Workshop on Spoken Language Translation". It is is a yearly scientific workshop which is associated with an open evaluation campaign on spoken language translation. Here, we only covers En-De Translation Dataset from "The IWSLT 2017 Evaluation Campaign".

<br>

**Multi30k**

<br>

**WMT14**

<br>

**KoEn**
> This dir deals with Korean-English Translation Dataset, which provided from AI_Hub. The original name for this dataset is "한국어-영어 번역(병렬) 말뭉치", and it is available with permission from the AI_Hub web. So, excluding downloading, this dir only covers data processing under the assumption that the original file has been fetched. The original file [한국어-영어 번역(병렬) 말뭉치](https://aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&aihubDataSe=realm&dataSetSn=126) can be fetched from this link.

<br>

The Dataset consist of 10 sub-datasets, but only uses 7 like below. And the total size of data is approximately 1.3M.

**`1_구어체(1).xlsx`** &nbsp;&nbsp; **`1_구어체(2).xlsx`** &nbsp;&nbsp; **`2_대화체.xlsx`** &nbsp;&nbsp; 

**`3_문어체_뉴스(1)_200226.xlsx`** &nbsp;&nbsp; **`3.문어체_뉴스(2).xlsx`** &nbsp;&nbsp; **`3.문어체_뉴스(3).xlsx`** &nbsp;&nbsp; **`3.문어체_뉴스(4).xlsx`**




<br>



<br>


## Dialogue

**Daily**
> The dialogues in the dataset reflect our daily communication way and cover various topics about our daily life.

<br>

**Empathetic**
> The EmpatheticDialogues dataset is a large-scale multi-turn empathetic dialogue dataset collected on the Amazon Mechanical Turk, containing 24,850 one-to-one open-domain conversations. Each conversation was obtained by pairing two crowd-workers: a speaker and a listener. The speaker is asked to talk about the personal emotional feelings. The listener infers the underlying emotion through what the speaker says and responds empathetically. The dataset provides 32 evenly distributed emotion labels.

<br>

**Persona**

<br>

**Blended**

<br>


**HIMYM**
> This Dataset is extracted from the script of the famous sitcom **How I Met Your Mother**. Compared to other dramas or movies with strong genre characteristics, sitcoms mainly use familiar language in everyday life. And in this sitcom, each character has a distinct personality, which is useful data for the model to learn the personality.
<br>

## Summarization

**CNN_Daily**

<br>

### How to use
```
git clone https://github.com/moon23k/NLP_datasets
python3 -m pip freeze >requirements.txt
bash the_data_you_want/download_dataset.sh
```
