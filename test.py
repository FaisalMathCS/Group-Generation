import itertools

# Sample data
names = [
    'Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace', 'Heidi', 
    'Ivy', 'Jack', 'Karen', 'Leo', 'Mona']

students = {name: {key: 0 for key in names if key != name} for name in names}

# Ensure every student has an entry for every other student with initial count of 0 if not already present
for student in students:
    for other_student in students:
        if other_student != student:
            students[student].setdefault(other_student, 0)

def sort_by_total_occurrences(students):
    total_occurrences = {student: sum(partners.values()) for student, partners in students.items()}
    sorted_students = sorted(total_occurrences, key=total_occurrences.get, reverse=True)
    return sorted_students

def find_least_occurrences(student, students, count):
    occurrences = students[student]
    sorted_partners = sorted(occurrences, key=occurrences.get)
    return sorted_partners[:count]

def form_groups(num_groups, students):
    sorted_students = sort_by_total_occurrences(students)
    groups = []
    candidate_leaders = sorted_students[:num_groups]
    remaining_students = [student for student in sorted_students if student not in candidate_leaders]
    
    for leader in candidate_leaders:
        group = [leader]
        least_occurrence_students = find_least_occurrences(leader, students, len(students) // num_groups - 1)
        for student in least_occurrence_students:
            if student in remaining_students:
                group.append(student)
                remaining_students.remove(student)
        groups.append(group)

    # Distribute remaining students if any
    for student in remaining_students:
        for group in groups:
            if len(group) < len(students) // num_groups + 1:
                group.append(student)
                break

    return groups

def update_occurrences(groups, students):
    for group in groups:
        for member in group:
            for other in group:
                if member != other:
                    students[member][other] += 1

num_groups = int(input("Enter the number of groups: "))
groups = form_groups(num_groups, students)
update_occurrences(groups, students)

print("Groups:")
for group in groups:
    print(group)
print("\nUpdated Occurrences Dictionary:")
for name, occurrences in students.items():
    print(f"{name}: {occurrences}")
