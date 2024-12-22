from collections import defaultdict, deque


# Parse the input data
def parse_data(file_path):
    with open(file_path) as file:
        data = file.read()
        sections = data.strip().split("\n\n")
        rules = [tuple(map(int, line.split('|'))) for line in sections[0].split('\n')]
        updates = [list(map(int, line.split(','))) for line in sections[1].split('\n')]
        return rules, updates


# Find if the update is correct according to the rules
def find_correct_updates(update, rules):
    position = {page: idx for idx, page in enumerate(update)}
    for before, after in rules:
        if before in position and after in position:
            if position[before] > position[after]:
                return False
    return True


# Perform a topological sort to find the correct order for an incorrect update
def topological_sort(update, rules):
    # Create adjacency list and in-degree map
    adj = defaultdict(list)
    in_degree = defaultdict(int)

    for before, after in rules:
        if before in update and after in update:
            adj[before].append(after)
            in_degree[after] += 1
            if before not in in_degree:
                in_degree[before] = 0

    # Kahn's algorithm for topological sort
    queue = deque([node for node in update if in_degree[node] == 0])
    sorted_update = []

    while queue:
        node = queue.popleft()
        sorted_update.append(node)

        for neighbor in adj[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return sorted_update


# Find the middle page number from a given update
def middle_in_line(update):
    middle_index = len(update) // 2
    return update[middle_index]


# Sum of middle page numbers from correct updates
def sum_of_middle_updates(file_path):
    rules, updates = parse_data(file_path)
    correct_updates = [update for update in updates if find_correct_updates(update, rules)]
    return sum(middle_in_line(update) for update in correct_updates)


# Sum of middle page numbers from incorrect updates after correcting their order
def sum_middle_incorrect(file_path):
    rules, updates = parse_data(file_path)
    corrected_updates = [topological_sort(update, rules) for update in updates if
                         not find_correct_updates(update, rules)]
    return sum(middle_in_line(update) for update in corrected_updates)


# Main program
file_path = "C:\\Users\\Daniella\\PycharmProjects\\advent calendar\\nums.txt"
res_correct = sum_of_middle_updates(file_path)
res_incorrect = sum_middle_incorrect(file_path)

print(res_correct)
print(res_incorrect)
