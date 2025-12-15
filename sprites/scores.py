import json

def options_load():
    try:
        with open('options.json') as file:
            return json.load(file)
    except:
        return {
            'volume_master': 1,
            'volume_shot': 0.1,
            'volume_explosion': 0.2
        }



def options_save(a):
    with open('options.json', 'w') as file:
        json.dump(a, file)

