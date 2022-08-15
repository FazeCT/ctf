#Made by FazeCT

local_a8 =[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
local_a8[0] = 0x1cc
local_a8[1] = 0x1a0
local_a8[2] = 0x194
local_a8[3] = 0x1b0
local_a8[4] = 0x1b0
local_a8[5] = 0x18c
local_a8[6] = 0x1d0
local_a8[7] = 0x198
local_a8[8] = 0x1ec
local_a8[9] = 0x188
local_a8[10] = 0xc4
local_a8[11] = 0x1d0
local_a8[12] = 0x15c
local_a8[13] = 0x1a4
local_a8[14] = 0xd4
local_a8[15] = 0x194
local_a8[16] = 0x17c
local_a8[17] = 0xc0
local_a8[18] = 0x1c0
local_a8[19] = 0xcc
local_a8[20] = 0x1c8
local_a8[21] = 0x104
local_a8[22] = 0x1d0
local_a8[23] = 0xc0
local_a8[24] = 0x1c8
local_a8[25] = 0x14c
local_a8[26] = 500

for i in range(26):
    n = str(local_a8[i])
    print(chr(int(n)//4),end='')
print(chr(local_a8[26]//4),end='')

#Flag is: shellctf{b1tWi5e_0p3rAt0rS}
