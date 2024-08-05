import random
import math

class StudentGroupingProblem:
    def __init__(self, students_dict, num_groups):
        self.students_dict = students_dict
        self.num_groups = num_groups
        self.student_list = list(students_dict.keys())
        self.min_group_size = math.ceil(len(self.student_list) / num_groups)
        self.initial_state = self.random_initial_state()

    def random_initial_state(self):
        state = [[] for _ in range(self.num_groups)]
        students = list(self.students_dict.keys())
        random.shuffle(students)
        for i, student in enumerate(students):
            state[i % self.num_groups].append(student)
        return state

    def actions(self, state):
        actions = []
        for i in range(self.num_groups):
            if len(state[i]) > self.min_group_size:
                for j in range(len(state[i])):
                    for k in range(self.num_groups):
                        if i != k and len(state[k]) < self.min_group_size:
                            actions.append((i, j, k))
        return actions

    def result(self, state, action):
        i, j, k = action
        new_state = [group.copy() for group in state]
        student = new_state[i].pop(j)
        new_state[k].append(student)
        return new_state

    def is_goal(self, state):
        return all(len(group) >= self.min_group_size for group in state) and sum(len(group) for group in state) == len(self.student_list)

    def action_cost(self, state):
        cost = 0
        for group in state:
            for i in range(len(group)):
                for j in range(i + 1, len(group)):
                    student = group[i]
                    other_student = group[j]
                    cost += self.students_dict[student].get(other_student, 0)
        return cost

    def neighbor(self, state):
        valid_actions = self.actions(state)
        if not valid_actions:
            return state
        action = random.choice(valid_actions)
        return self.result(state, action)

    def acceptance_probability(self, old_cost, new_cost, temperature):
        if new_cost < old_cost:
            return 1.0
        else:
            return math.exp((old_cost - new_cost) / temperature)

def simulated_annealing(problem, initial_temp, min_temp, alpha, max_iter):
    current_state = problem.initial_state
    current_cost = problem.action_cost(current_state)
    temperature = initial_temp

    best_state = current_state
    best_cost = current_cost

    while temperature > min_temp and max_iter > 0:
        neighbor_state = problem.neighbor(current_state)
        neighbor_cost = problem.action_cost(neighbor_state)

        if problem.acceptance_probability(current_cost, neighbor_cost, temperature) > random.random():
            current_state = neighbor_state
            current_cost = neighbor_cost

            if current_cost < best_cost:
                best_state = current_state
                best_cost = current_cost

        temperature *= alpha
        max_iter -= 1

    return best_state, best_cost

def update_occurrences(groups, students):
    for group in groups:
        for member in group:
            for other in group:
                if member != other:
                    students[member][other] += 1


import json 
with open('data.json', 'r') as f:
    data = json.load(f)
students_dict = data['students']

num_groups = int(input("Enter the number of groups: "))
initial_temp = 100000
min_temp = 1
alpha = 0.999995
max_iter = 1000000
while True: 
    problem = StudentGroupingProblem(students_dict, num_groups)
    solution_state, solution_cost = simulated_annealing(problem, initial_temp, min_temp, alpha, max_iter)


    print("Groups:", solution_state)
    print("Cost:", solution_cost)
    flag = int(input("IS this group okay? enter 0 if no, 1 if yes: \t"))
    if flag: 
        update_occurrences(solution_state, students_dict)
        print("New Group Occurrences has been updated!")
        data['students'] = students_dict
        with open('data.json', 'w') as f:
            json.dump(data, f) 
        break


