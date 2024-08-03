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

def test_candidates(num_groups, names):
    temp = num_groups 
    for i in range(0, 1000):
        x = len(generate_candidates(names, 4))
        if x > 4: 
            print("Bigger than expected") 
        elif x < 4: 
            print("Less than expected")

'''
TODO: 
1- Generate groups based on Canidadates
2- Implemented an interface on CLI for users 
3- save new data with updated occurances on the json file
'''

def generate_groups(students, candidates, names): 
    taken = []
    groups= []
    for candi in candidates:
        
        occ = [(key, value) for key, value in sorted(students[candi].items(), key = lambda item: item[1])]
        occ = occ[0:8] 
        taken.append(set([val[0] for val in occ]))
        results = []
    print(candidates)
    print(taken)
    for i, current_set in enumerate(taken):
        # Create a union of all sets except the current one
        rest_union = set().union(*[s for j, s in enumerate(taken) if i != j])
        # Compute the difference between the current set and the rest_union
        difference = current_set.difference(rest_union)
        results.append(difference)
    return results
    

    pass 

data = read_data()

students = data['students']

names = data['names'] 

all_groups = data['all_groups'] 


# x = generate_candidates(names, 4)
# print()
# print(generate_groups(students, x, names))

for i in range(1000000000):
    pass
print("Done")

