import json

def score_load():
    try:
        with open('scores.json') as file:
            return json.load(file)
    except:
        return {
            'scores': [0]
        }



def score_save(a):
    with open('scores.json', 'w') as file:
        json.dump({"scores":a}, file)