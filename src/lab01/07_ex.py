s = input('in: ')

start = 0
for i in range(len(s)):
    if s[i].isupper():
        start = i
        break

digit = 0
for i in range(start+1, len(s)):
    if s[i].isdigit():
        digit = i
        break

step = (digit + 1) - start

ans = ''
i = start
while i < len(s):
    ans+=s[i]
    if s[i]=='.':
        break
    i+=step

print(f'out: {ans}')