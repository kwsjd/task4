name = input('Введите своё имя: ')
secondname = input('Введите свою фамилию: ')
date = int(input('Введите дату рождения: '))
print(name, secondname, date, sep = '_')
name, secondname = secondname, name
print(name, secondname, date + 60, sep = '_')
