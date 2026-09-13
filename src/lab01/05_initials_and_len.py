fio = input('ФИО: ').split()

initials = ''

for word in fio:
    initials += word[0].upper()

ln = len(' '.join(fio))

print(f'Инициалы: {initials}.')
print(f'Длина (символов): {ln}')