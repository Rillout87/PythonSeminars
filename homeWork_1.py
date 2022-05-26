# Сформировать список из N членов последовательности. Для N = 5: 1, -3, 9, -27, 81 и т.д.

from itertools import count
from math import factorial


def sequence (n):
    resultList = list()
    for member in range(n):
        resultList.append((-3)**member)
    return resultList

    
print(sequence(5))

# Пользователь задаёт две строки. Определить количество вхождений одной строки в другой.

text1 = "Рыла свинья белорыла, тупорыла; полдвора рылом изрыла, вырыла, подрыла"
text2 = "рыл"

res = text1.lower().count(text2.lower())
print(res)

#Подсчитать сумму цифр в вещественном числе.


def digitSum (floatNumber):
    result = 0  
    numbers = str(floatNumber).split('.')
    for number in numbers:
        for digit in number:
            result += int(digit)
    print(result)

digitSum(152.9614)

# Написать программу получающую набор произведений чисел от 1 до N. Пример: пусть N = 4, тогда [ 1, 2, 6, 24 ]

def seq (n):
    rslt = []
    for i in range(1,n+1):
        rslt.append(factorial(i))
    return rslt

print(seq(4))

