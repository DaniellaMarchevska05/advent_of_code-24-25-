# def makeSortedList(file, col):
#     lst = []
#     for line in file:
#         line = line.strip()
#         parts = line.split()
#         value = int(parts[col - 1])
#         lst.append(value)
#     lst.sort()
#     return lst
#
# def sumOfDistances(list1, list2):
#     out = []
#     for x in range(len(list1)):
#         dist = abs(list1[x] - list2[x])
#         out.append(dist)
#     res = sum(out)
#     return res

# def sortlist(file, col):
#     lst = []
#     for line in file:
#         parts = line.strip().split()
#         lst.append(int(parts[col - 1]))
#     return lst
#
# def sumofdist(l1, l2):
#     return sum(abs(a-b) for a,b in zip(sorted(list1), sorted(list2)))

def calcul1(file):
    lst1, lst2 = [], []
    with open(file) as f: # 'with' helps to automatically close the file and use it as 'f'
        for line in f:
            parts = line.strip().split()
            if len(parts) >= 2:
                lst1.append(int(parts[0]))
                lst2.append(int(parts[1]))
    return sum(abs(a-b) for a,b in zip(sorted(lst1), sorted(lst2)))

def calcul2(file_path):
    lst1, lst2 = [], []
    with open(file_path) as f: # 'with' helps to automatically close the file and use it as 'f'
        for line in f:
            parts = line.strip().split()
            if len(parts) >= 2:
                lst1.append(int(parts[0]))
                lst2.append(int(parts[1]))
        total_sum = 0
        for i in lst1:
            varia = lst2.count(i)
            total_sum+=varia*i
    return total_sum


# with open("C:\\Users\\Daniella\\Documents\\advent\\nums.txt") as fhand:
#     lines = fhand.readlines()  #list of lists in which each list is a line from file ([[sd  sd\n], [fgh gh\n], [fghj ghj]n]...])
# list1 = sortlist(lines, 1)
# list2 = sortlist(lines, 2)
# summ = sumofdist(list1, list2)
summ = calcul2("C:\\Users\\Daniella\\PycharmProjects\\advent calendar\\nums.txt")
print(summ)




