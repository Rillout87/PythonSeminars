# 1. Задать список из N элементов, заполненных числами из [-N, N]. Найти произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число

import math
import random


def productPositions (lst, pos):
    return math.prod([lst[i] for i in pos])

with open('sem3.txt', 'r') as positionFile:
    position = positionFile.readlines()
    position = [int(position[i]) for i in range (len(position))]

n = max(position)  + 2  
numbers = [random.randint(-n, n) for i in range(n+1)]
print (numbers)
print (productPositions(numbers, position))



#Дано число. Составить список чисел Фибоначчи, в том числе для отрицательных индексов.
# Т е для k = 8, список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] Негафибоначчи

def fibonacciList (k):
    if k in (0, 1):
        return [abs(i) for i in range(-k, k+1)]
    else:
        lst = [0, 1]
        negList = [0, 1]
        for i in range(2, k+1):
           lst.append(lst[i-1] + lst[i-2])
           negList.append(negList[i-2] - negList[i-1])
        negList.reverse()

        return negList + lst[1:]

print(fibonacciList(8))


#Строка содержит набор чисел. Показать большее и меньшее число
# Символ-разделитель - пробел

str = '21 -234 199 1 17'
numb = [int(str.split(' ')[i]) for i in range(len(str.split(' ')))]
print(max(numb))
print(min(numb))
