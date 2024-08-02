'''
problem statement: Generate #n groups from a list of students where each group has the least amount of occurrences

Data: a dictionary of dictionaries where each student will have a dictionary where the name is the key, 
    and the value is a dictionary where the other students' names are keys and their values are the number of occurrences. 

Problem Formulation: 

    Initial State: empty list [] with no students inside
    Actions: adds a student to the list, if [] is empty append randomly from the canadidates list
    Transional Model RESULT(State, Action): Calculate the occurrences factor
    GOAL TEST: #n groups with the least possible occurrences
    PATH COST: the sum of occurrences for each element in a group. 

    SOLUTION: sequence of students with the least occurrences

'''

import itertools 

names = ["Faisal", "Ziyad", "Salman", "Fahad", "Naif", "Firas", "Alaa", "Dania", "Hatoon", "Wadia", "Raghad", "Osama", "Sarraa", "Ashwag",
            "Ahmad", "Mosaab", "Abdulaziz", "Samer", "Ali", "mousa", "mohammed", "Abduallah"]

students = {

}

for name in names:
    students[name] = {key: 0 for key in names if key != name} 

groups = [["Ahmad", "Faisal", "Samer", "Ashwag", "Ziyad"], ["Ziyad", "Faisal"], [], []]


def increase_occurences(groups):
    for group in groups: 
        for member in group: 
            for i in range(0, len(group)):
                if group[i] in students[member]:
                    students[member][group[i]] += 1 
                    print(students[member][group[i]], group[i])
    # print(students)
print(students["Samer"])

print()

print()

print(students["Faisal"])


print()

print()

print(students["Ahmad"])
print()

print()

print(students['Ashwag'])
# print((list(itertools.combinations(elements, 4))))

[2 + 3 + 4, 1 + 3 + 4, 1 + 2 + 4,  ]
# import random

# class student: 
#     def __init__(self, occurrences, initial_state = ()):
#         self.initial_state = initial_state
#         self.occurrences = occurrences
#         self.students = occurrences.keys() 
    
#     def actions(self, state):
#         actions = [] 
#         if self.initial_state == (): 
#             actions.append(random.randint(0, len(self.occurrences)))
#             return actions 
#         last_name
#         pass 
