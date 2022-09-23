data = [ord('W'),ord('B'),ord('K'),ord('E'),-52,-69,-127,-52,113,122,113,102,-33,-69,-122,-51,100,111,110,92,-14,-83,-102,-40,ord('~'),ord('o')]
for i in range(0, len(data) - 1, 2):
    data[i], data[i+1] = data[i+1], data[i]
enc = [1,3,3,7,222,173,190,239]
for i in range(len(data)):
    data[i] ^= enc[i % 8]
    if data[i] > 0: print(chr(data[i]), end='')
    else: print(chr(256 + data[i]), end='')
