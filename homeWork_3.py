import math

# 1. Найти НОК (наименьшее общее кратное) двух чисел

def nok (a, b):
    temp_a, temp_b = a, b # сначала найдем наибольший общий делитель, для этого значения a и b скопируем во временные переменные
    while temp_a != 0 and temp_b != 0:
        if temp_a > temp_b:
            temp_a %= temp_b
        else: temp_b %= temp_a
    return int(a*b/(temp_a + temp_b)) # нок = произведение чисел разделить на нод
    

print(nok (6,8))

# 2. Вычислить число Пи c заданной точностью d
#Пример: при d = 0.001,  c= 3.141




def myPi (length: str):
    length = len(length.split('.')[1])
    return round(math.pi, length)
    


print (myPi('0.000001'))

#3. Составить список простых множителей натурального числа N

def simpleNumberList (n):
    i = 2
    res = []
    while i <= n:
        if n%i == 0:
            res.append(i)
            n/=i
        else: i+=1
    return res


print(simpleNumberList(125))

#4. Дана последовательность чисел. Получить список неповторяющихся элементов исходной последовательности
#Пример: [1, 2, 3, 5, 1, 5, 3, 10] => [1, 2, 3, 5, 10]

sequence = [1, 2, 3, 5, 1, 5, 3, 10]
print(set(sequence))

#5. Дан текстовый файл, содержащий целые числа. Удалить из него все четные числа.
'''
23
6
9
13
55
32
7
86
100
1123
'''

with open('hw3.txt', 'r') as numbersFile:
    numbers = numbersFile.readlines()
    numbers = [int(numbers[i]) for i in range(len(numbers))]
    
with open('hw3.txt', 'w') as numbersFile:
    numbers = [number for number in numbers if number%2 != 0]
    for number in numbers:
        numbersFile.write(f'{str(number)} \n')




