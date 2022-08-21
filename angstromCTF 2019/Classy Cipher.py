#Made by FazeCT

data = ":<M?TLH8<A:KFBG@V"
for i in range(0,255):
    flag=""
    for c in data:
        flag+=chr((ord(c)-i+10000)%255)
    if "actf" in flag:
        print(flag)
        break
