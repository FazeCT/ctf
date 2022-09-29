data = "2D++DEM	"
for i in range(255):
    for c in data:
        print(chr(ord(c) ^ i), end='')
    print()

#Missing a letter t, flag is Flag{x0r_is_s0meth1n9}
