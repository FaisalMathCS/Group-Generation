def read_data(file_path = 'data.json'):
    import json
    with open(file_path, 'r') as f:
        data = json.load(f) 
        return data

def generate_candidates(names, num_groups):
    import random
    temp = names.copy() 
    canadidates = set()
    for i in range(num_groups):
        x = set()
        y = set() 
        for j in range(100): 
            name = temp[random.randint(0, len(temp) - 1)]
            if name in x:
                if name in y: 
                    canadidates.add(name)
                    temp.remove(name)
                    break
                y.add(name)
            x.add(name)
    return canadidates

data = read_data()

students = data['students']

names = data['names'] 

all_groups = data['all_groups'] 




for i in range(0, 1000):
    temp = 4 
    x = len(generate_candidates(names, 4))

    if x > 4: 
        print("Bigger than expected") 
    elif x < 4: 
        print("Less than expected")