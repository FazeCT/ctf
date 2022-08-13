#Made by FazeCT

def revtea(pwd):
    part1 = ""
    for i in range(0,16):
        part1 += chr(ord(pwd[i]) + 3*i//2)

    part2 = ""
    for i in range(16,32):
        part2 += chr(ord(pwd[i]) - i//6)
    return part1 + part2

def revsugar(pwd):
    l38 = pwd[len(pwd)-16:len(pwd)]
    l58 = pwd[0:len(pwd)-16]
    rpwd = ""
    i = 0
    j = 0
    for _ in range(len(pwd)):
        if _ & 1 == 0:
            rpwd += l38[i]
            i += 1
        else:
            rpwd += l58[j]
            j += 1
    return rpwd

data = "R;crc75ihl`cNYe`]m%50gYhugow~34i"
l78 = "50gYhugow~34i"
for i in range(0,19):
    pwd = ""
    l48 = data[0:i]
    la8 = data[i:19]
    pwd = la8 + l78 + l48
    #print(l48,"|",la8,"|",l78)
    print(revsugar(revtea(pwd)))

l78 = "5ihl`cNYe`]m%50gYhugow~34i"
for i in range(0,7):
    pwd = ""
    l48 = data[0:i]
    la8 = data[i:7]
    pwd = la8 + l78 + l48
    #print(l48,"|",la8,"|",l78)
    print(revsugar(revtea(pwd)))
    
 #Flag is: shellctf{T0_1nfiNi7y_4nd_B3y0nd}
