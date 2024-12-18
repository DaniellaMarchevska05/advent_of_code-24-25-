import re
from turtledemo.sorting_animate import instructions1

def multi(file_path):
    with open(file_path) as file: # 'with' helps to automatically close the file and use it as 'f'
        data = file.read()
        instructions = re.findall(r'(do\(\))|(don\'t\(\))|(mul\(\d+,\d+\))', data)
        mul_enable = True
        total_sum = 0
        for do_inst, dont_inst, mul_inst in instructions:
            if do_inst:
                mul_enable = True
            elif dont_inst:
                mul_enable = False
            elif mul_inst and mul_enable:
                x, y = map(int, re.findall(r'\d+', mul_inst))
                total_sum+=x*y
    return total_sum

res = multi("C:\\Users\\Daniella\\PycharmProjects\\advent calendar\\nums.txt")
print(res)

# def part_2(file_path):
#     with open(file_path, 'r') as file:
#         data = file.read()
#
#     instructions = re.findall(r'(do\(\))|(don\'t\(\))|(mul\(\d+,\d+\))', data)
#
#     total_sum = 0
#     mul_enabled = True
#     for do_instr, dont_instr, mul_instr in instructions:
#         if do_instr:
#             mul_enabled = True
#         elif dont_instr:
#             mul_enabled = False
#         elif mul_instr and mul_enabled:
#             x, y = map(int, re.findall(r'\d+', mul_instr))
#             total_sum += x * y
#
#     return total_sum