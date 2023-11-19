import json, argparse
from datasets import load_dataset




def data_processing(data_type, resp_type):
    processed = []
    blend_data = load_dataset('blended_skill_talk')


	resp_dict = {
		'guided': 'guided_messages', 
		'convai2': 'convai2', 
		'empathetic': 'empathetic_dialogues', 
		'wikipedia': 'wizard_of_wikipedia'
	}
	resp_type = resp_dict[resp_type]

	#Single Turn Data Processing
    if data_type == 'single_turn':

		for split in ['train', 'validation', 'test']:
		    for elem in blend_data[split]:
		        dial_list = []
		        dial_list.extend(elem['previous_utterance'])

		        for uttr, resp in zip(elem['free_messages'], elem[resp_type]):
		            dial_list.append(uttr.lower().strip())
		            dial_list.append(resp.lower().strip())

		        if max([len(x) for x in dial_list]) > max_len:
		            continue

		        dial_turns = len(dial_list)
		        #Incase of dial_turns is even
		        if dial_turns % 2 == 0:
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

	#Multi Turn Data Processing
	elif data_type == 'multi_turn':
		pass



    return processed






def main(args):
	data_type, resp_type = **args
    processed = data_processing(args.data_type, args.resp_type)



if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-data_type', required=True)
    parser.add_argument('-resp_type', required=True)
    
    args = parser.parse_args()
    assert args.data_type in ['single_turn', 'multi_turn']
    assert args.resp_type in ['guided', 'convai2', 'empathetic', 'wikipedia']

    main(args)    