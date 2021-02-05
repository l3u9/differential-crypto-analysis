from toycipher import ToyCipher


f1 = open("PlainTextA.txt", "r")
f2 = open("PlainTextB.txt", "r")

data1 = f1.readlines()
data2 = f2.readlines()

for i in range(len(data1)):
    data1[i] = data1[i].strip("\n")
    data2[i] = data2[i].strip("\n")
    data1[i] = data1[i].strip("L")
    data2[i] = data2[i].strip("L")

for i in range(len(data1)):
    data1[i] = int(data1[i], 16)
    data2[i] = int(data2[i], 16)


f1 = open("CipherTextA.txt", "w")
f2 = open("CipherTextB.txt", "w")

cipher = ToyCipher()

for i in range(len(data1)):
    ret1 = str(hex(cipher.encrypt(data1[i]))) + "\n"
    ret2 = str(hex(cipher.encrypt(data2[i]))) + "\n"

    f1.write(ret1)
    f2.write(ret2)






