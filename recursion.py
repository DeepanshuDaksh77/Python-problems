import sys
sys.setrecursionlimit(30000)

i = 0
def greet():
    global i
    i += 1

    print("hello world", i)
    greet()

greet()