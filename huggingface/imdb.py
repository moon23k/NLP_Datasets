import os, re, json, random
from datasets import load_dataset




def fetch_imdb(orig_data):
    fetched = []
    max_len = 1000
    tot_volumn = 1200
    class_volumn = 1200 // 2
    neg_cnt, pos_cnt = 0, 0
    neg_data, pos_data = [], []

    train_data = [x for x in orig_data['train']]
    test_data = [x for x in orig_data['test']]
    concat_data = train_data + test_data

    for elem in concat_data:
        if neg_cnt + pos_cnt == tot_volumn:
            break
        text = elem['text'].replace('<br />', '').lower()
        if len(text) > max_len:
            continue
        label = elem['label']

        if label == 0 and pos_cnt < class_volumn:
            pos_cnt += 1
            neg_data.append({'x': text, 'y': label})

        elif label == 1 and neg_cnt < class_volumn:
            neg_cnt += 1
            pos_data.append({'x': text, 'y': label})

    for neg_elem, pos_elem in zip(neg_data, pos_data):
        fetched.append(neg_elem)
        fetched.append(pos_elem)

    return fetched



def split_shuffle(fetched):
    train_data = fetched[:-200]
    valid_data = fetched[-200:-100]
    test_data = fetched[-100:]

    random.shuffle(train_data)
    random.shuffle(valid_data)
    random.shuffle(test_data)

    return train_data, valid_data, test_data




def main():
    orig_data = load_dataset('imdb')
    fetched_data = fetch_imdb()
    train_data, valid_data, test_data = split_shuffle(fetched_data)



if __name__ == '__main__':
    main()