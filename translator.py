import sys


fin = open("CCode/main.c", 'r')
fout = open("translation/main.py", 'w')

sys.stdout = fout

def parser(line_list):
    total_len = len(line_list)

    if len(line_list) == 0: 
        print("")
        return True
        
    if len(line_list[0]) == 1 and line_list[0][0] == '\n':
        print("")
        return True

    if len(line_list[0]) >= len("#include"):
        if line_list[0][:8] == "#include":
            print(line_list[0][:-1])
            return True

    white_space = 0
    last_line_len = len(line_list[-1])
    while last_line_len > white_space and (line_list[-1][-1 - white_space] in {' ', '\n'}):
        white_space += 1
    
    if len(line_list) == 1 and line_list[-1][ last_line_len - white_space - 1] == ';':
        print(line_list[0][:-1])
        return True
    
    print(line_list[0][:-1])
    if len(line_list) >= 2:
        if len(line_list) > 2:
            parser(line_list[1:-1])
        print(line_list[-1][:-1])
    return True


line_no = 0
lines = fin.readlines()
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