import json
names = ["Faisal", "Ziyad", "Salman", "Fahad", "Naif", "Firas", "Alaa", "Dania", "Hatoon", "Wadia", "Raghad", "Osama", "Sarraa", "Ashwag",
            "Ahmad", "Mosaab", "Abdulaziz", "Samer", "Ali", "Mousa", "Mohammed", "Abduallah", 'Hamad', 'Majed']


students = {

}




for name in names:
    students[name] = {key: 0 for key in names if key != name} 


def increase_occurences(groups):
    for group in groups: 
        for member in group: 
            for i in range(0, len(group)):
                if group[i] in students[member]:
                    students[member][group[i]] += 1 
                    
def check_equal_names(groups):
    visitid = []
    for group in groups:
        for name in group: 
            visitid.append(name)
    temp = sorted(visitid)
    temp2 = sorted(names)
    return temp == temp2 

groups1 = [['Faisal', 'Fahad', 'Abduallah', 'Firas'], ['Ahmad', 'Samer', 'Ali', 'Abdulaziz'], ['Mousa', 'Mohammed', 'Hatoon', "Salman", 'Raghad'], 
          ['Alaa', 'Wadia', 'Mosaab', 'Dania'], ['Ziyad', 'Osama', 'Naif', 'Ashwag', 'Sarraa']]
groups2 = [
    ["Ahmad", "Naif", "Alaa"],        # Team 1
    ["Mohammed", "Abdulaziz"],        # Team 2
    ["Abduallah", "Osama", "Mousa"],   # Team 3
    ["Salman", "Samer", "Wadia"],     # Team 4
    ["Mosaab", "Raghad", "Ashwag"],   # Team 5
    ["Hatoon", "Hamad", "Dania"],     # Team 6
    ["Fahad", "Sarraa", "Ziyad"],     # Team 7
    ["Ali", "Faisal", "Firas"]        # Team 8
]
groups3 = [
    ["Ziyad", "Faisal", "Dania", "Alaa"],        # Team 1
    ["Abduallah", "Firas", "Naif", "Salman"],     # Team 2
    ["Ashwag", "Mohammed", "Ali", "Osama"],      # Team 3
    ["Wadia", "Samer", "Sarraa", "Ahmad"],       # Team 4
    ["Mosaab", "Hatoon", "Hamad", "Raghad"],     # Team 5
    ["Mousa", "Abdulaziz", "Fahad"]              # Team 6
]
groups4 = [
    ["Osama", "Sarraa"],              # Team 1
    ["Wadia", "Ahmad"],               # Team 2
    ["Hamad", "Ziyad"],               # Team 3
    ["Majed", "Ashwag"],              # Team 4
    ["Dania", "Mohammed"],            # Team 5
    ["Abduallah", "Mosaab"],           # Team 6
    ["Alaa", "Naif"],                 # Team 7
    ["Fahad", "Hatoon"],              # Team 8
    ["Samer", "Ali"],                 # Team 9
    ["Mousa", "Abdulaziz"],           # Team 10
    ["Faisal", "Raghad"],             # Team 11
    ["Salman", "Firas"]               # Team 12
]
all_groups = [groups1, groups2, groups3, groups4]

for groups in all_groups:
    increase_occurences(groups)


data = {
    'students' : students, 
    'names' : names, 
    'all_groups': all_groups
}
with open('data.json', 'w') as f:

    json.dump(data, f, indent = 6)
