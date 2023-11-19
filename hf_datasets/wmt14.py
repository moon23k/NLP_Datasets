import os, re, json, argparse
from datasets import load_dataset
from collections import Counter




def data_processing(data_obj, trg_lang):    
    min_len = 10 
    max_len = 300
    max_diff = 50
    processed = []
    
    for elem in data_obj:
        temp_dict = dict()
        x, y = elem['en'].strip().lower(), elem[trg_lang].strip().lower()
        x_len, y_len = len(x), len(y)

        #Filtering Conditions
        min_condition = (x_len >= min_len) & (y_len >= min_len)
        max_condition = (x_len <= max_len) & (y_len <= max_len)
        dif_condition = abs(x_len - y_len) < max_diff

        if max_condition & min_condition & dif_condition:
            processed.append({'x': x, 'y':y})

    return processed



def word_count():
    return word_cnt



def data_report():
    report = {
        
        'orig_data': {
            'data_volum': 0,
            'avg_x_len': 0,
            'avg_y_len': 0,
            'word_cnt': 0
        },

        'processed_data': {
            'data_volum': 0,
            'avg_x_len': 0,
            'avg_y_len': 0,
            'word_cnt': 0
        }

    }

    with open(f'data/{lang_pair}/report.json', 'w') as f:
        json.dump(report, f)        
    return




def main():
    #Data Processing
    ende_data = load_dataset('wmt14', 'de-en')
    ende_data, ende_corpus = data_processing(ende_data, 'de')

    encs_data = load_dataset('wmt14', 'cs-en')
    encs_data, encs_corpus = data_processing(encs_data, 'cs')

    enru_data = load_dataset('wmt14', 'ru-en')
    enru_data, enru_corpus = data_processing(enru_data, 'ru')        


    #For Multi Lingual Training Data
    multi_data = []
    for de_elem, cs_elem, ru_elem in zip(ende_data, encs_data, enru_data):
        multi_data.append({'x': de_elem['x'], 'y': de_elem['y']})
        multi_data.append({'x': cs_elem['x'], 'y': cs_elem['y']})
        multi_data.append({'x': ru_elem['x'], 'y': ru_elem['y']})

    multi_data = multi_data[:303000]




if __name__ == '__main__':   
    parser = argparse.ArgumentParser()
    parser.add_argument('-lang_pair', required=True)
    args = parser.parse_args()

    assert args.lang_pair in ['ende', 'encs', 'enru']

    main(args.lang_pair)