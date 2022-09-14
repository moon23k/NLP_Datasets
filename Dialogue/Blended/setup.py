import os, json



def download_data():
	cmd = """
	mkdir -p data; 
	cd data; 
	python3 -m pip install parlai;
	python3 -m parlai.scripts.display_data --task blended_skill_talk --datapath data;
	mv blended_skill_talk/* .;
	rm -rf blended_skill_talk;
	"""

	os.system(cmd)


def load_data(split, save=False):
    assert split in ['train', 'valid', 'test']

    processed = []

    with open(f'data/{split}.json', 'r') as f:
        orig = json.load(f)

    for elem in orig:
        dials = defaultdict(list)

        dials['dialogue'].append(elem['free_turker_utterance'])
        dials['dialogue'].append(elem['guided_turker_utterance'])
        
        utters = elem['dialog']
        for utter in utters:
            dials['dialogue'].append(utter[-1])
        processed.append(dials)

    if save:
        os.makedirs('data/blended', exist_ok=True)
        save_json(processed, f"data/blended/{split}.json")

    return processed


def main()


if __name__ == '__main__':
    main()