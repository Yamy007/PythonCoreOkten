import re

# strings

# 1)написати прогу яка вибирає зі введеної строки цифри і виводить їх через кому,
# наприклад:
# st = 'as 23 fdfdg544' введена строка
# 2,3,5,4,4        #вивело в консолі.

st = 'as 23 fdfdg544'
# print((',').join([i for i in st if i.isdigit()]))


# #################################################################################
# 2)написати прогу яка вибирає зі введеної строки числа і виводить їх 
# так як вони написані
# наприклад:
st = 'as 23 fdfdg544 34' #введена строка
#   23, 544, 34              #вивело в консолі

# print((' ').join(re.sub(r'\D', ' ', st).split()))
# #################################################################################


# list comprehension

# 1)є строка:
# greeting = 'Hello, world'
# записати кожний символ як окремий елемент списку і зробити його заглавним:
# ['H', 'E', 'L', 'L', 'O', ',', ' ', 'W', 'O', 'R', 'L', 'D']
greeting = 'Hello, world'
# print([i for i in greeting.upper()])


# 2) з диапозону від 0-50 записати тільки не парні числа при цьому піднести їх до квадрату
# приклад:
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, ...]
# print([i **2 for i in range(50) if i %2 !=0 ]) # or i == 0  але 0  пофакту не мав би входити 

# function

# - створити функцію яка виводить ліст
def func():
  return [1,2,3]

# - створити функцію яка приймає три числа та виводить та повертає найбільше.
def func_0(a,b,c):
  return max(a,b,c)


# - створити функцію яка приймає будь-яку кількість чисел, повертає найменьше, а виводить найбільше
def func_1(*args):
  print("Max value", max(args))
  return  min(args)

# print("func_1 => ", func_1(2,3,4,5,6))
# - створити функцію яка повертає найбільше число з ліста

def func_2(list):
  return max(list)

# print("func_2 => ", func_2([2,3,5]))

# - створити функцію яка повертає найменьше число з ліста
def func_3(list):
  return min(list)

# print("func_3 => ", func_3([2,3,5]))
# - створити функцію яка приймає ліст чисел та складає значення елементів ліста та повертає його.

def func_4(list):
    return sum(list)
  
# print("func_4 => ", func_4([2,3,5]))
  
# - створити функцію яка приймає ліст чисел та повертає середнє арифметичне його значень.

def func_5(list):
  return sum(list)/len(list)

# print("func_5 => ", func_5([2,4,6]))


################################################################################################
# 1)Дан list:
list = [22, 3,5,2,8,2,-23, 8,23,5]
#   - знайти мін число
# print('list min', min(list))
#   - видалити усі дублікати
# print('set list', sorted(set(list))) # set to list back
#   - замінити кожне 4-те значення на 'X'
# print('change value',['X' if (i + 1) % 4 == 0 else x for i, x in enumerate(list)])
# 2) вивести на екран пустий квадрат з "*" сторона якого вказана як агрумент функції
def draw(a):
  print('*'*a)
  for _ in range(a-2):
    print('*', ' '*(a-4), '*')
  print('*'*a)

# 3) вывести табличку множення за допомогою цикла while

def num():
  i = 1
  while i <= 10:
      j = 1
      while j <= 10:
          result = i * j
          print(str(result).rjust(2), end=" ")
          j += 1
      print()
      i += 1


# 4) переробити це завдання під меню
run = True
while run:
  print("\n***************Menu***************")
  print('0) exit')
  print('1) написати прогу яка вибирає зі введеної строки цифри і виводить їх через кому,')
  print('2) написати прогу яка вибирає зі введеної строки числа і виводить їх так як вони написані')
  print('3) є строка: greeting = \'Hello, world\' аписати кожний символ як окремий елемент списку і зробити його заглавним')
  print('4) з диапозону від 0-50 записати тільки не парні числа при цьому піднести їх до квадрату')
  print('5) створити функцію яка виводить ліст')
  print('6) створити функцію яка приймає три числа та виводить та повертає найбільше.')
  print("7) створити функцію яка приймає будь-яку кількість чисел, повертає найменьше, а виводить найбільше")
  print('8) створити функцію яка повертає найбільше число з ліста')
  print('9) створити функцію яка повертає найменьше число з ліста')
  print('10) створити функцію яка приймає ліст чисел та складає значення елементів ліста та повертає його.')
  print('11) створити функцію яка приймає ліст чисел та повертає середнє арифметичне його значень.')
  print('12) знайти мін число')
  print('13) видалити усі дублікати')
  print('14) замінити кожне 4-те значення на "X"')
  print('15) вивести на екран пустий квадрат з "*" сторона якого вказана як агрумент функції')
  print('16) вывести табличку множення за допомогою цикла while')


  choise = input('>>> ')
  if choise == "1":
    print("Дано:\n st = 'as 23 fdfdg544'")
    print("Код => (',').join([i for i in st if i.isdigit()])")
    print("Результат: ")
    st = 'as 23 fdfdg544'
    print((',').join([i for i in st if i.isdigit()]))
    
  elif choise == "2":
    print("Дано:\n st = 'as 23 fdfdg544 34'")
    print("Код => (' ').join(re.sub(r'\D', ' ', st).split())")
    print("Результат: ")
    st = 'as 23 fdfdg544 34'
    print((' ').join(re.sub(r'\D', ' ', st).split()))

  elif choise == "3":
    print("Дано:\n greeting = 'Hello, world'")
    print("Код => [i for i in greeting.upper()]")
    print("Результат: ")
    greeting = 'Hello, world'
    print([i for i in greeting.upper()])

  elif choise == "4":
    print("Дано:\n [0...50]")
    print("Код => [i **2 for i in range(50) if i %2 !=0 ]")
    print("Результат: ")
    print([i **2 for i in range(50) if i %2 !=0 ])
    
  elif choise == "5":
    print('Результат: ')
    print("def func():\n  return [1,2,3]")
    print("func()")
    print(func())
    
  elif choise == "6":
    print('Результат: ')
    print('def func_0(a,b,c):\n  return max(a,b,c)')
    print("func_0(1,2,3)")
    print(func_0(1,2,3))

  elif choise == "7":
    print('Результат: ')
    print('def func_1(*args):\n  print("Max value", max(args))\n  return  min(args)')
    print("func_1(2,3,4,5,6)")
    print(func_1(2,3,4,5,6))

  elif choise == "8":
    print('Результат: ')
    print('def func_2(list):\n  return max(list)')
    print("func_2([2,3,5])")
    print(func_2([2,3,5]))
    
  elif choise == "9":
    print('Результат: ')
    print('def func_3(list):\n  return min(list)')
    print("func_3([2,3,5])")
    print(func_3([2,3,5]))

  elif choise == "10":
    print('Результат: ')
    print('def func_4(list):\n    return sum(list)')
    print("func_4([2,3,5])")
    print(func_4([2,3,5]))

  elif choise == "11":
    print('Результат: ')
    print('def func_5(list):\n  return sum(list)/len(list)')
    print("func_5([2,4,6])")
    print(func_5([2,4,6]))
    
  elif choise == "12":
    print('Результат: ')
    print('list = [22, 3,5,2,8,2,-23, 8,23,5]')
    print("min(list)")
    print(min(list))
    
  elif choise == "13":
    print('Результат: ')
    print('list = [22, 3,5,2,8,2,-23, 8,23,5]')
    print("sorted(set(list)) # set to list back")
    print(sorted(set(list)))
    
  elif choise =="14":
    print('Результат: ')
    print('list = [22, 3,5,2,8,2,-23, 8,23,5]')
    print("['X' if (i + 1) % 4 == 0 else x for i, x in enumerate(list)]")
    print(['X' if (i + 1) % 4 == 0 else x for i, x in enumerate(list)])
    
  elif choise == "15":
    print('Результат: ')
    print("def draw(a):\n  print('*'*a)\n  for _ in range(a-2):\n    print('*', ' '*(a-4), '*')\n  print('*'*a)\ndraw(8)")
    print("draw(8)")
    draw(8)
    
  elif choise == "16":
    print('Результат: ')
    print("i = 1\nwhile i <= 10:\n    j = 1\n    while j <= 10:\n        result = i * j\n        print(str(result).rjust(2), end=' ')\n        j += 1\n    print()\n    i += 1")
    num()
  elif choise == "0":
    run = False
  else: 
    print("Невірний вибір")
    


