# 1.Создать и заполнить файл случайными целыми значениями. Выполнить сортировку содержимого файла по возрастанию.

import random

numbers = [random.randint(0,100) for i in range(10)]

with open('hw4.txt', 'w') as createFile:
    for number in numbers:
        createFile.write(f'{str(number)} \n')

with open('hw4.txt', 'r') as readFile:
    numbs = readFile.readlines()
    numbs = [int(numbs[i]) for i in range(len(numbers))]
    numbs.sort()

with open('hw4.txt', 'w') as writeFile:
    
    for numb in numbs:
        writeFile.write(f'{str(numb)} \n')




# 2. Дан список чисел. Создать список в который попадают числа, описывающие возрастающую последовательность
# и содержащие максимальное количество элементов. 
# Пример: [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3, 4, 6, 7]
# [5, 2, 3, 4, 6, 1, 7] => [2, 3, 4, 6, 7]
# Порядок элементов менять нельзя

from typing import List


def maxRisingSequence (seq: List):
    # in this list we will write length of gotten subsequences. The default value for all subsequence is 1 (1 element's subsequence length)
    allSeqsLen = [1]*len(seq)
    # in this list we will write index of penult element of subsequence. The default value for all subsequence is -1 (for the stop of iterate)
    lastElemOfSeq = [-1]*len(seq)

    for i in range(1, len(seq)):
        #j = i - 1
        j = 0
        while j < i:
            if seq[i] > seq[j] and allSeqsLen[j] >= allSeqsLen[i]:
                allSeqsLen[i] = allSeqsLen[j] + 1
                lastElemOfSeq[i] = j
                
            j += 1
    
    resultSeq = []
    currentResultIndex = allSeqsLen.index(max(allSeqsLen))
    resultSeq.append(seq[currentResultIndex])
    
    while True:
        currentResultIndex = lastElemOfSeq[currentResultIndex]
        resultSeq.append(seq[currentResultIndex])
        if lastElemOfSeq[currentResultIndex] == -1:
            break
    
    resultSeq.reverse()
    return resultSeq


mysequence = [5, 2, 3, 4, 6, 1, 7]

print(maxRisingSequence(mysequence))



            
        
        

