print('Задача 5. Вася хочет выигрывать')

# Вася вдохновился фильмом «Двадцать одно» и решил изучить математику игровых автоматов. Для анализа данных ему нужна информация о том, как часто в автомате выпадает три или две одинаковых картинки. Для сбора данных нужна программа, проверяющая это равенство. 

# Даны три целых числа. Определите, сколько среди них совпадающих. 
# Программа должна вывести один из вариантов: 
# 1) 3 (если все совпадают) 
# 2) 2 (если два совпадают)
# 3) 0 (если все числа разные)

# Решение: 

number_1 = int(input("Введите первое число: "))
number_2 = int(input("Введите второе число: "))
number_3 = int(input("Введите третье число: "))
if number_1 == number_2 == number_3:
  print("3")
elif number_1 == number_2 or number_1 == number_3 or number_2 == number_3:
  print('2')
else:
  print('0')