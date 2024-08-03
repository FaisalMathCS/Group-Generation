import heapq

class Node: 
    def __init__(self, state, parent_node=None, action_from_parent=None, path_cost=0): 
        self.state = state
        self.parent_node = parent_node
        self.action_from_parent = action_from_parent
        self.path_cost = path_cost
        self.depth = 0 if self.parent_node is None else (self.parent_node.depth + 1)
    
    def __lt__(self, other):
        return self.state < other.state

class PriorityQueue:
    def __init__(self, items=(), priority_function=(lambda x: x)):
        self.priority_function = priority_function
        self.pqueue = []
        for item in items:
            self.add(item)
    
    def add(self, item):
        pair = (self.priority_function(item), item)
        heapq.heappush(self.pqueue, pair)
    
    def pop(self):
        return heapq.heappop(self.pqueue)[1]
    
    def __len__(self):
        return len(self.pqueue)

def expand(problem, node): 
    s = node.state 
    for action in problem.actions(s):
        s1 = problem.result(s, action)
        cost = node.path_cost + problem.action_cost(s, action, s1)
        yield Node(state=s1, parent_node=node, action_from_parent=action, path_cost=cost)
    
def get_path_actions(node): 
    if node is None or node.parent_node is None: 
        return [] 
    else: 
        actions = [] 
        actions.append(node.action_from_parent)
        node = node.parent_node
        while node.parent_node is not None: 
            actions.append(node.action_from_parent)
            node = node.parent_node
        return actions[::-1]

def get_path_states(node):
    if node is None: 
        return [] 
    else: 
        states = []
        states.append(node.state)
        node = node.parent_node
        while node is not None: 
            states.append(node.state)
            node = node.parent_node
        return states[::-1] 

def best_first_search(problem, f):
    node = Node(state=problem.initial_state)
    frontier = PriorityQueue((node,), f)
    reached = {tuple(tuple(group) for group in node.state): node} 

    while len(frontier) > 0: 
        curr = frontier.pop()

        if problem.is_goal(curr.state):
            return curr

        for child in expand(problem, curr):
            child_state = tuple(tuple(group) for group in child.state)
            if child_state not in reached or child.path_cost < reached[child_state].path_cost:
                frontier.add(child)
                reached[child_state] = child 
    return None

def best_first_search_treelike(problem, f): 
    node = Node(state=problem.initial_state)
    frontier = PriorityQueue((node,), f)

    while len(frontier) > 0: 
        curr = frontier.pop()

        if problem.is_goal(curr.state):
            return curr

        for child in expand(problem, curr):
            child_state = tuple(tuple(group) for group in child.state)
            frontier.add(child)

    return None

def breadth_first_search(problem, treelike=False): 
    f = (lambda n: n.depth)
    if not treelike:
        return best_first_search(problem, f)
    else:
        return best_first_search_treelike(problem, f)
    
def depth_first_search(problem, treelike=False):
    f = (lambda n: - n.depth)
    if treelike:
        return best_first_search_treelike(problem, f)
    else: 
        return best_first_search(problem, f)

def uniform_cost_search(problem, treelike=False): 
    f = (lambda n: n.path_cost)
    if not treelike: 
        return best_first_search(problem, f)
    else: 
        return best_first_search_treelike(problem, f)

def greedy_search(problem, h, treelike=False):
    f = (lambda n: h(n))
    if treelike: 
        return best_first_search_treelike(problem, f)
    else:
       return best_first_search(problem, f)
    
def astar_search(problem, h, treelike=False):
    f = (lambda n: n.path_cost + h(problem, n))
    if treelike: 
        return best_first_search_treelike(problem, f)
    else: 
        return best_first_search(problem, f)

class StudentGroupingProblem:
    def __init__(self, students_dict, num_groups):
        self.students_dict = students_dict
        self.num_groups = num_groups
        self.initial_state = [[] for _ in range(self.num_groups)]
        self.student_list = list(students_dict.keys())

    def actions(self, state):
        actions = []
        for student in self.student_list:
            for group_index in range(self.num_groups):
                if all(student not in group for group in state):
                    actions.append((student, group_index))
        return actions

    def result(self, state, action):
        new_state = [group.copy() for group in state]
        student, group_index = action
        new_state[group_index].append(student)
        return new_state

    def is_goal(self, state):
        return all(len(group) > 0 for group in state) and sum(len(group) for group in state) == len(self.student_list)

    def action_cost(self, state, action, result_state):
        student, group_index = action
        cost = 0
        for group in result_state:
            for other_student in group:
                if other_student != student:
                    cost += self.students_dict[student].get(other_student, 0)
        return cost

def heuristic(problem, node):
    state = node.state
    cost = 0
    for group in state:
        for i, student in enumerate(group):
            for j in range(i + 1, len(group)):
                other_student = group[j]
                cost += problem.students_dict[student].get(other_student, 0)
    return cost

import json 
with open('data.json', 'r') as f:
    data = json.load(f) 

students_dict = data['students']
import time 
t0 =time.time()
num_groups = 5
problem = StudentGroupingProblem(students_dict, num_groups)
solution_node = astar_search(problem, heuristic)
t1 = time.time()
if solution_node:
    print("Groups:", solution_node.state)
    print("Cost:", solution_node.path_cost)
elif not solution_node:
    print("No solution found")

print(t1 - t0)