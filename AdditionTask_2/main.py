from typing import Dict

# вивести послідовність Фібоначі, кількість вказана в знінній,
#   наприклад: x = 10 -> 1 1 2 3 5 8 13 21 34 55
#   (число з послідовності - це сума попередніх двох чисел)

# порахувати кількість парних і непарних цифр числа,
#   наприклад: х = 225688 -> п = 5, н = 1;
#          х = 33294 -> п = 2, н = 3


# прога, що виводить кількість кожного символа з введеної строки,
#   наприклад:
#   st = 'as 23 fdfdg544' #введена строка

#   'a' -> 1  #вивело в консолі
#   's' -> 1
#   ' ' -> 2
#   '2' -> 1
#   '3' -> 1
#   'f' -> 2
#   'd' -> 2
#   'g' -> 1
#   '5' -> 1
#   '4' -> 2


# генерируем лист с непарных чисел в порядке возрастания [1,3,5,7,9.....n]
# задача сделать c него лист листов такого плана:

# [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]  => [ [1], [3,5], [7,9,11], [13,15,17,19] ]
# [1, 3, 5, 7, 9, 11] => [[1], [3, 5], [7, 9, 11]]
# [1, 3, 5, 7, 9]  => [ [1], [3,5], [7,9]]
# [1, 3, 5, 7, 9, 11, 13]  => [[1], [3, 5], [7, 9, 11], [13]]


# найти со списка только уникальные числа

# пример [1,2,3,4,2,5,1] => [ 3, 4, 5 ]

def fibonacci(length: int) -> str:
    arr = [1, 1]
    [arr.append(arr[-2]+arr[-1]) for _ in range(length-2)]
    return ','.join(str(i) for i in arr)


def calculate(num: int) -> dict[int, int]:
    even = len([i for i in str(num) if int(i) % 2 == 0])
    odd = len(str(num)) - even
    return {"even": even, "odd": odd}


def count_word(st: str) -> dict:
    result = {}
    [result.update({i: result.get(i)+1}) if result.get(i)
     else result.update({i: 1}) for i in st]
    return result


def generator(n: int) -> list:
    result = []
    arr = [i for i in range(n+1) if i % 2 != 0]
    j = 0
    for count in range(len(arr)):
        i = j
        j = i+1+count
        if arr[i:j+count]:
            result.append(arr[i:j])
        else:
            break
    return result


def unique_list(arr: list) -> list:
    result = {}
    [result.update({i: result.get(i)+1}) if result.get(i)
     else result.update({i: 1}) for i in arr]
    return [i for i in result if result.get(i) == 1]


print(fibonacci(22))
print(calculate(33294))
print(count_word('as 23 fdfdg544'))
print(generator(19))
print(unique_list([1, 2, 3, 4, 2, 5, 1]))


