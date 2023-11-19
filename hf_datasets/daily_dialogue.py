import json, argparse
from datasets import load_dataset




def process_dialogue_data():
    processed = []

    #Load original Datasets
    daily_data = load_dataset('daily_dialog')


    #Single Turn Data Processing
    if data_type == 'single_turn':
        x_data, y_data = [], []
        for split in ['train', 'validation', 'test']:
            for dial in daily_data[split]['dialog']:
                dial_list = []
                dial_turns = len(dial)

                if max([len(d) for d in dial]) > 300:
                    continue
                
                for uttr in dial:
                    _uttr = re.sub(r"\s([?,.!’](?:\s|$))", r'\1', uttr)
                    _uttr = re.sub(r'([’])\s+', r'\1', _uttr).strip().lower()
                    if len(_uttr) > 300:
                        break
                    dial_list.append(_uttr)
                
                if dial_turns < 2:
                    continue

                elif dial_turns == 2:
                    x_data.append(dial_list[0])
                    y_data.append(dial_list[1])
                    continue  #To avoid duplicate on below condition

                #Incase of dial_turns is even
                elif dial_turns % 2 == 0:
                    x_data.extend(dial_list[0::2])
                    y_data.extend(dial_list[1::2])

                    x_data.extend(dial_list[1:-1:2])
                    y_data.extend(dial_list[2::2])
                
                #Incase of dial_turns is odds
                elif dial_turns % 2 == 1:
                    x_data.extend(dial_list[0:-1:2])
                    y_data.extend(dial_list[1::2])
                    
                    x_data.extend(dial_list[1::2])
                    y_data.extend(dial_list[2::2])   


        assert len(x_data) == len(y_data)
        for x, y in zip(x_data, y_data):        
            processed.append({'x': x, 'y': y})



    #Single Turn Data Processing
    elif data_type == 'multi_turn':
        pass    

    return processed





def main(task):
    processed = process_dialogue_data()




if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-data_type', required=True)
    
    args = parser.parse_args()
    assert args.data_type in ['single_turn', 'multi_turn']
    
    main(args)    