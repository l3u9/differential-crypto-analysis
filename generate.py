from random import *

f1 = open("PlainTextA.txt", "w")
f2 = open("PlainTextB.txt", "w")

for i in range(4096):
    p0 = (randint(0, 0xffffffff))
    p1 = str(hex(p0 ^ 0x000000B0))
    p0 = str(hex(p0))  

    p0 = p0 + "\n"
    p1 = p1 + "\n"
    

    f1.write(p0)
    f2.write(p1)
