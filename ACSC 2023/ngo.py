data = [0x01, 0x19, 0xEF, 0x5A, 0xFA, 0xC8, 0x2E, 0x69, 0x31, 0xD7,
  0x81, 0x21]
key = 0x3D2964F0
cnt = 0
total = 0
print('ACSC{', end='')
for i in data:
    total = pow(42,cnt)
    rnd = total % 0xFFFFFFFF
    for j in range(rnd):
        key = (key >> 1) ^ (-(key & 1) & 0x80200003)
    print(chr((key ^ data[cnt]) & 0xFF),end='')
    cnt += 1
print('}')
