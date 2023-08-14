import sys

def main():
    preprocess()
    print("Hello, World!")
    return 0

def preprocess():
    sys.stdin = open('input.txt', 'r')
    sys.stdout = open('res.txt', 'w')


main()