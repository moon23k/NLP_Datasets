import os, re, json
from tqdm import tqdm
from bs4 import BeautifulSoup
from urllib.request import urlopen



def get_links():
    main = 'https://transcripts.foreverdreaming.org/viewforum.php?f=177'
    urls = [main + f'&start={25 * i}' if i else main for i in range(6)]

    links = []
    for url in urls:
        html = urlopen(url)
        bs = BeautifulSoup(html, "lxml")
        
        tags = bs.find_all('a', {'class': "topictitle"})
        for tag in tags[1:]:
            affix = tag['href'].split('&sid')[0][1:]
            links.append(tag['href'][1:])
            if affix[-5:] == '11688':
                break

    return links



#process Scripts to Dialogue Dataset
def process_script(script):
    processed = [[]]  #container var for processed scripts
    switch = 0

    for line in script:
        seq = line.getText()

        #pass google ads text
        if not seq or 'adsbygoogle' in seq:
            continue

        if seq[0] == '(' or seq[0] == '[':
            switch=1
            if processed[-1] != []:
                processed.append([])
            continue

        if switch and (seq[0] == '(' or seq[0] == '['):
            switch = 0

        if switch:
            if ":" in seq:
                seq = re.sub("[\(\[].*?[\)\]]", "", seq)
                speaker = seq.split(":")[0]
                seq = ''.join(seq.split(":")[1:])
                processed[-1].append({speaker: seq})


    processed = [dial for dial in processed if len(dial) > 1]
    processed = [dial if len(dial) % 2 == 0 else dial[:-1]  for dial in processed]
    
    return processed




#Crawl Dataset and Save the dataset as "raw.txt"
def crawl_dataset(links):
    dataset = []
    #Iterate 20+ Eposodes per 9 Seasons
    for link in tqdm(links):
        html = urlopen(f"https://transcripts.foreverdreaming.org{link}")
        bs = BeautifulSoup(html, "lxml")

        episode = bs.find('div', {'class': "postbody"}) #whole Episode Contents
        script = episode.find_all('p')  #Scripts from Episode
        
        data_per_ep = process_script(script)
        dataset.extend(data_per_ep)

    return dataset




#split dataset to src and trg
def split_dataset(dataset):
    src, trg = [], []

    for dial in dataset:
        for idx, seq in enumerate(dial):
            seq = "".join(seq.values())
            if idx % 2 == 0:
                src.append(seq)
            else:
                trg.append(seq)
    
    src_train, src_valid = src[:-1000], src[-1000:]
    trg_train, trg_valid = trg[:-1000], trg[-1000:]


    with open('HIMYM/orig/train.src', 'w') as f:
        f.write('\n'.join(src_train))
    with open('HIMYM/orig/valid.src', 'w') as f:
        f.write('\n'.join(src_valid))
    
    with open('HIMYM/orig/train.trg', 'w') as f:
        f.write('\n'.join(trg_train))
    with open('HIMYM/orig/valid.trg', 'w') as f:
        f.write('\n'.join(trg_valid))




def split_barney(dataset):
    barney_indice = []
    src, trg = [], []

    for i, dial in enumerate(dataset):
        for j, seq in enumerate(dial):
            speaker = ''.join(seq.keys()).lower()

            if speaker == 'barney' and j:
                barney_indice.append([i, j])


    src = [dataset[idx[0]][idx[1] - 1] for idx in barney_indice]
    trg = [dataset[idx[0]][idx[1]] for idx in barney_indice]

    src = [''.join(seq.values()).strip() for seq in src]
    trg = [''.join(seq.values()).strip() for seq in trg]


    src_train, src_valid = src[:-100], src[-100:]
    trg_train, trg_valid = trg[:-100], trg[-100:]

    with open('Barney/orig/train.src', 'w') as f:
        f.write('\n'.join(src_train))
    with open('Barney/orig/valid.src', 'w') as f:
        f.write('\n'.join(src_valid))
    
    with open('Barney/orig/train.trg', 'w') as f:
        f.write('\n'.join(trg_train))
    with open('Barney/orig/valid.trg', 'w') as f:
        f.write('\n'.join(trg_valid))




if __name__ == "__main__":
    os.makedirs('HIMYM/orig', exist_ok=True)
    os.makedirs('Barney/orig', exist_ok=True)
    
    links = get_links()
    dataset = crawl_dataset(links)
    split_dataset(dataset)
    split_barney(dataset)