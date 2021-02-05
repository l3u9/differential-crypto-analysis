
pm = [17, 22, 27, 28, 21, 26, 31, 0, 25, 30, 3, 4, 29, 2, 7, 8, 1, 6, 11, 12, 5, 10, 15, 16, 9, 14, 19, 20, 13, 18, 23, 24]
invpm = [7, 16, 13, 10, 11, 20, 17, 14, 15, 24, 21, 18, 19, 28, 25, 22, 23, 0, 29, 26, 27, 4, 1, 30, 31, 8, 5, 2, 3, 12, 9, 6]

# sbox = [1, 10, 4, 12, 6, 15, 3, 9, 2, 13, 11, 7, 5, 0, 8, 14]
# invsbox = [13, 0, 8, 6, 2, 12, 4, 11, 14, 7, 1, 10, 3, 9, 15, 5]

sbox = [12, 5, 6, 11, 9, 0, 10, 13, 3, 14, 15, 8, 4, 7, 1, 2]
invsbox = [5, 14, 15, 8, 12, 1, 2, 13, 11, 4, 6, 3, 0, 7, 9, 10]


class ToyCipher:
    
    def __init__(self):
        self.key = 0x98756456
        


    def invpermutation(self,data):
        ret= 0x00000000

        for i in range(32):
            ret |= (((data >> i) & 0x1) << (invpm[i]))

        return ret

    def permutation(self, data):
        ret= 0x00000000

        for i in range(32):
            ret |= ((data >> i) & 0x1) << (pm[i])

        return (ret)

    def iSbox(self, data):
        ret = 0x00000000

        for i in range(8):
            tmp = (data >> ((4*i))) & 0xf
            ret |= invsbox[tmp] << (4*i)
        return ret
    def Sbox(self, data):
        ret = 0x00000000

        for i in range(8):
            tmp = (data >> ((4*i))) & 0xf
            ret |= sbox[tmp] << (4*i)
        #print(hex(ret))
        return ret

    def key_xor(self, data):
        
        data = data ^ self.key
        return data

    def encrypt_oneround(self, data):

        data = self.key_xor(data)
        data = self.Sbox(data)
        data = self.permutation(data)

        return data

    def decrypt_oneround(self, data):
        data = self.invpermutation(data)
        data = self.iSbox(data)
        data = self.key_xor(data)
        return data


    def encrypt(self, data):
        

        for i in range(4):
            data = self.encrypt_oneround(data)
        data = self.key_xor(data)

        return data

    def decrypt(self, data):
        
    
        data = self.key_xor(data)

        for i in range(4):
            data = self.decrypt_oneround(data)

        return data
