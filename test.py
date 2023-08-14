"""
TODO Check how to use pytest to make some of these processes simpler,
probably not of much use in IT, but we can use it in DT, for 
individual pieces. For individual functions.
"""

import os

test_path = "./IT/"
total_tests = 0
total_pass = 0

def compare():
    fout = open("output.txt", 'r')
    fres = open("res.txt", 'r')

    text_out = fout.readlines()
    text_res = fres.readlines()

    if len(text_out) != len(text_res):
        return False
    else:
        for i in range(len(text_out)):
            if text_out[i] != text_res[i]:
                print(f"{i+1}th line not same")
                print(f"{text_out[i], text_res[i]}")
                print(f"Test Failed")
                return False

    return True

def run_test(test_no):
    global total_pass
    os.chdir(f"./{test_no}")
    os.system("gcc -Wall -o main CCode/main.c")
    os.system("./main")
    os.system("python3 ../../translator.py")
    os.system("python3 translation/main.py")
    total_pass += compare()
    os.system("rm -rf ./main")
    os.chdir(f"./..")


def print_results():
    global total_pass, total_tests
    print(f"{total_pass} out of {total_tests} tests passed.\n"
          f"Accuracy is {(total_pass/total_tests) * 100}%.")

def main():
    global total_tests
    os.chdir(f"./{test_path}")

    for f in os.listdir('.'):
        if os.path.isdir(f):
            print(f"TEST {f}")
            total_tests += 1
            run_test(f)
    
    print_results()

main()
