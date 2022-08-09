#Made by FazeCT

#asm2(0x4,0x2d)

a = int('0x2d',16)
b = int('0x4',16)

while b <= int('0x5fa1',16):
    a += int('0x1',16)
    b += int('0xd1',16)

print(hex(a))
