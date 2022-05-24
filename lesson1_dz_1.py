 ##Пользователь вводит продолжительность duration в секундах:
duration = int(input('Укажите продолжительность в секундах: '))
day = duration // 86400
hour = duration // 3600 % 24
minute = duration // 60 % 60 
second = duration % 60
print(day, 'дн', hour, 'час', minute,  'мин', second, 'cек')