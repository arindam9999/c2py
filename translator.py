import sys

from utils import line_preprocessor, parser

fin = open("CCode/main.c", 'r')
fout = open("translation/main.py", 'w')

sys.stdout = fout


line_no = 0
lines = fin.readlines()
line_preprocessor(lines)

total_lines = len(lines)
flag = False
while line_no < total_lines:
    line_list = []
    while line_no < total_lines:
        line_list.append(lines[line_no])
        line_no += 1
        # print(line_list)
        flag = parser(tuple(line_list))
        if flag:
            break
    if not flag:
        print("# ERROR!! Unexpected End to file.")