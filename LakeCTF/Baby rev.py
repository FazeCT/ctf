for v8 in range(0,2147418112+65536):
    v4 = v3 = 0
    while v3 != 32:
        v5 = v8 >> v3
        v3 += 1
        v4 = (v5 & 1) + 2 * v4
    if v8 == v4:
        print(v4)
        break
