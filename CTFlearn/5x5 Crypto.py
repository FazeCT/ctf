#Made by FazeCT

data = ['1-3','4-4','2-1','{','4-4','2-3','4-5','3-2','1-2','4-3','_','4-5','3-5','}']

cipher = [['A','B','C','D','E'],['F','G','H','I','J'],['L','M','N','O','P'],['Q','R','S','T','U'],['V','W','X','Y','Z']]

for c in data:
    if c == '{' or c == '}' or c == '_':
        print(c,end='')
        continue
    else:
        print(cipher[int(c[0])-1][int(c[2])-1],end='')
