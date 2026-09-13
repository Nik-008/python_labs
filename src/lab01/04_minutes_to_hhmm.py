m = int(input('Минуты: '))

h = m//60
minutes = m%60

print(f'{h}:{minutes:02d}')