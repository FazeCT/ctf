#Made by FazeCT

v = ['0xF4', '0xC0','0x97','0xF0', '0x77', '0x97', '0xC0', '0xE4', '0xF0', '0x77', '0xA4', '0xD0','0xC5', '0x77', '0xF4', '0x86', '0xD0', '0xA5', '0x45', '0x96', '0x27', '0xB5', '0x77', '0xE0', '0x95', '0xF1', '0xE1', '0xE0', '0xA4', '0xC0', '0x94', '0xA4']

def switchBits(n,a,b):
    l = [char for char in n]
    l[a],l[b] = l[b],l[a]
    return ''.join(l)

for i in range(len(v)):
    c = bin(int(v[i],16))[2:].zfill(8)
    c = switchBits(c, 6, 7)
    c = switchBits(c, 2, 5)
    c = switchBits(c, 3, 4)
    c = switchBits(c, 0, 1)
    c = switchBits(c, 4, 7)
    c = switchBits(c, 5, 6)
    c = switchBits(c, 0, 3)
    c = switchBits(c, 1, 2)
    print(bytes.fromhex(hex(int(c,2))[2:]).decode('utf-8'),end='')




