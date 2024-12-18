def is_asc(seq):
    return all(seq[i]<seq[i+1] for i in range(len(seq)-1))

def is_desc(seq):
    return all(seq[i]>seq[i+1] for i in range(len(seq)-1))

def dist(seq):
    return all(0<abs(seq[i]-seq[i+1])<=3 for i in range(len(seq)-1))

def safeornah(file):
    safe = 0
    with open(file) as f: # 'with' helps to automatically close the file and use it as 'f'
        for line in f:
            parts = list(map(int, line.strip().split()))
            if (is_desc(parts) or is_asc(parts)) and dist(parts):
                safe+=1

    return safe

res = safeornah("C:\\Users\\Daniella\\PycharmProjects\\advent calendar\\nums.txt")
print(res)