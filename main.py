import os

def s():
    a = (input())
    if a == "":
        return
    p = os.fork()
    if p == 0:
        s()
    else:
        os.waitpid(p, 0)
        print(a)


s() 