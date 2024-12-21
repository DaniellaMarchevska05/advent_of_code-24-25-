def parse_data(file_path):
    with open(file_path) as file: # 'with' helps to automatically close the file and use it as 'f'
        data = file.read()
        sections = data.strip().split("\n\n")
        rules = [tuple(map(int, line.split('|'))) for line in sections[0].split('\n')]
        updates =[list(map(int, line.split(','))) for line in sections[1].split('\n')]
        return rules, updates

def middle_in_line(update):
    middle_index = len(update)//2
    return update[middle_index]

def find_correct_updates(update, rules):
    position = {page: idx for idx, page in enumerate(update)}

    for before, after in rules:
        # Check only if both pages are in the update
        if before in position and after in position:
            if position[before] > position[after]:
                return False

    return True

def sum_of_middle_updates(file_path):
    rules, updates = parse_data(file_path)

    correct_updates = list()

    for update in updates:
        if find_correct_updates(update, rules):
            correct_updates.append(update)

    middle_sum = sum(middle_in_line(update) for update in correct_updates)
    return middle_sum

res = sum_of_middle_updates("C:\\Users\\Daniella\\PycharmProjects\\advent calendar\\nums.txt")
print(res)