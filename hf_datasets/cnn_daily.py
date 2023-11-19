import json
from datasets import load_dataset



def process_summarization_data(data_volumn=101100):    
    volumn_cnt = 0
    corpus, processed = [], []
    min_len, max_len = 500, 3000

    #Load Original Dataset
    cnn_data = load_dataset('cnn_dailymail', '3.0.0')

    for split in ['train', 'validation', 'test']:
        for elem in cnn_data[split]:

            x, y = elem['article'], elem['highlights']

            if min_len < len(x) < max_len:
                if len(y) < min_len:
                    
                    #Lowercase
                    x, y = x.lower(), y.lower()

                    #Remove unnecessary characters in trg sequence
                    y = re.sub(r'\n', ' ', y)                 #remove \n
                    y = re.sub(r"\s([.](?:\s|$))", r'\1', y)  #remove whitespace in front of dot

                    processed.append({'x': x, 'y': y})
                    corpus.append(x)
                    corpus.append(y)

                    #End Condition
                    volumn_cnt += 1
            if volumn_cnt == data_volumn:
                break

    with open('data/summarization/corpus.txt', 'w') as f:
        f.write('\n'.join(corpus))
    
    return processed           






def main(task):

    #PreProcess Data
    if task == 'translation':
        processed = process_translation_data()
    elif task == 'dialogue':
        processed = process_dialogue_data()
    elif task == 'summarization':
        processed = process_summarization_data()        

    #Train Tokenizer
    train_tokenizer(task)

    #Save Data
    save_data(task, processed)



if __name__ == '__main__':
	main()