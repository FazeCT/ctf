from pwn import *

p = remote("137.184.215.151", 22602)

def solve(n,m,b):
    sum = 0
    ans = -999999999999999999
    cnt = 0
    for i in range(0,n):
        sum += b[i]
        cnt += 1
        if ans < sum and cnt <= m:
            ans = sum
        if sum < 0:
            sum = 0
            cnt = 0
    return ans
for i in range(10):
    p.recvlines(2)
    a = list(map(int,p.recvline().decode().split()))
    n = a[0]
    m = a[1]
    b = list(map(int,p.recvline().decode().split()))
    res = solve(n,m,b)
    p.sendline(str(res))
p.interactive()
