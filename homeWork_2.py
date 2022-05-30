# 1. Найти сумму чисел списка стоящих на нечетной позиции Пример:[1,2,3,4] -> 4

from decimal import Decimal
import math
import random

def oddPlaceSum (lst):
    result = 0
    for i in range(0, len(lst), 2):
        result += lst[i]
    return result


print (oddPlaceSum ([1,2,3,4]))

# 2. Найти произведение пар чисел в списке. Парой считаем первый и последний элемент, второй и предпоследний и т.д. 
# Пример: [2, 3, 4, 5, 6] => [12, 15, 16]; [2, 3, 5, 6] => [12, 15]

def prudoctOfPair (lst):
    resultList = []
    for i in range(0, math.ceil(len(lst)/2)):
        resultList.append(lst[i] * lst[-i-1])
    return resultList


print (prudoctOfPair([2, 3, 4, 5, 6]))

# 3. В заданном списке вещественных чисел найдите разницу между максимальным и минимальным значением дробной части элементов. 
# Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19

def frictPartList (lst):
    resList = []
    for number in lst:
        if type(number) == float:
            resList.append(round(number%1, 2))
    return resList

numbrs = frictPartList([1.1, 1.2, 3.1, 5, 10.01])

print (max(numbrs) - min(numbrs))

# 4. Написать программу преобразования десятичного числа в двоичное

def binaryFormat (decimalNumb):
    return format(decimalNumb, 'b')


print(binaryFormat(125))

'''2. Создайте программу, которая будет играть в игру “коровы и быки” с пользователем. Игра работает так:
Случайным образом генерируйте 4-значное число. Попросите пользователя угадать 4-значное число.
За каждую цифру, которую пользователь правильно угадал в нужном месте, у них есть “корова”. За каждую цифру,
которую пользователь угадал правильно, в неправильном месте стоит “бык”. Каждый раз, когда пользователь делает
предположение, скажите им, сколько у них “коров” и “быков”. Как только пользователь угадает правильное число, игра окончена.
Следите за количеством догадок, которые пользователь делает на протяжении всей игры, и сообщите пользователю в конце.'''

# НЕ РЕШИЛ ПОКА, ПРОШУ НЕ ПРОВЕРЯТЬ

def bullsAndCows (nmr):
    count = 0
    playerNumber = ""
    nmrString = str(nmr)
    
    while playerNumber != nmrString:
        cows, bulls = 0, 0
        
        playerNumber = input('Угадайте черетырехзначное число: ')
        if len(playerNumber) != 4:
            continue
        
        for i in range (4):
            if playerNumber[i] == nmrString[i]:
                playerNumber[i] = "x"
                cows += 1
            elif playerNumber[i] in nmrString:
                playerNumber[i] = "x"
                bulls += 1
        print (f"Вы угадали {cows} коров и {bulls} быка")
    
    else: print ("Вы угадали!")

            
number = random.randint(1000, 9999)
bullsAndCows(number)