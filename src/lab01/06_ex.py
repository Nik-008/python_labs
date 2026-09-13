N = int(input('N: '))

och = 0
zao = 0

for i in range(N):
    s = input(f'in_{i+1}: ')
    if 'True' in s:
        och+=1
    elif 'False' in s:
        zao+=1

print(f'out: {och} {zao}')