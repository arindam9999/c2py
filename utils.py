def remove_whitespace_and_endline(lines):
    for i in range(len(lines)):
        line_length = len(lines[i])
        pointer = 0
        while (pointer < line_length) and (lines[i][pointer] in {'\n', ' ', '\t'}):
            pointer += 1
        
        if pointer == line_length:
            lines[i] = " "
            continue
        bpointer = line_length - 1
        while (bpointer >= 0) and (lines[i][bpointer] in {'\n', ' ', '\t'}):
            bpointer -= 1
        
        lines[i] = lines[i][pointer:(bpointer + 1)]
        
def line_preprocessor(lines):
    remove_whitespace_and_endline(lines)


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
            print(line_list[0])
            return True

    if len(line_list) == 1 and line_list[0][-1] == ';':
        print(line_list[0])
        return True
    
    print(line_list[0])
    if len(line_list) >= 2:
        if len(line_list) > 2:
            parser(line_list[1:-1])
        print(line_list[-1])
    return True