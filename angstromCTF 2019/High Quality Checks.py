#Made by FazeCT

from Crypto.Util.number import bytes_to_long, long_to_bytes,getPrime, inverse

a1 = ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
a1[12] = long_to_bytes(808531811).decode()[::-1]
a1[0] = chr(172//2 ^ int(str(0x37)))
a1[16] = chr(220//2)
for i in range(0,256):
    if i > 96: v1 = i - 87
    else: v1 = i - 48
    if 65537 * (v1 + (i << 8)) == 889533701:
        a1[17] = chr(i)
    if 65537 * (v1 + (i << 8)) == 1712285199:
        a1[5] = a1[9] = chr(i)
    if 65537 * (v1 + (i << 8)) == 1596940079:
        a1[8] = chr(i)
a1[18] = chr(246//2 + 2*(18%4//2))
a1[4] = chr(246//2 + 2*(4%4//2))
v5 = v6 = 0
for i in range(8):
    v7 = ((1 << i) & 108) >> i
    if i & 1 != 0:
        v5 += v7 << (i//2)
    else:
        v6 += v7 << (i//2)
a1[v5] = chr(117)
a1[v5+1] = chr(220//2)
a1[v6] = chr(234//2)
a1[v6+1] = chr(110)

hex = '0x667463'
a1[1] = chr(int(str(0x63)))
a1[2] = chr(int(str(0x74)))
a1[3] = chr(int(str(0x66)))
for c in a1: print(c,end='')

#Flag is: actf{fun_func710n5}
