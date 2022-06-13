# 1. Написать программу вычисления арифметического выражения заданного строкой. Используются операции +,-,/,*.
# приоритет операций стандартный. Функцию eval не использовать!
# Пример: 2+2 => 4; 1+2*3 => 7; 1-2*3 => -5;
# Дополнительно: Добавить возможность использования скобок, меняющих приоритет операций. 
# Пример: 1+2*3 => 7; (1+2)*3 => 9;


def operate(numb1, numb2, op):

    if op == '*':
        return numb1 * numb2
    elif op == '/':
        return numb1 / numb2
    elif op == '+':
        return numb1 + numb2
    elif op == '-':
        return numb1 - numb2

def calculate (exp_list: list):

    if '(' in exp_list: #проверка на наличие скобок
        left_parentheses_index = exp_list.index('(') # ищем первое вхождение открывающихся скобок
        right_parentheses_index = len(exp_list) - exp_list[::-1].index(')') - 1 # ищем последнее вхождение закрывающихся скобок
        exp_list[left_parentheses_index] = calculate (exp_list[left_parentheses_index + 1: right_parentheses_index]) # рекурсивно передаем все, что внутри скобок, возвращая на месте левой скобки результат вычисления
        while left_parentheses_index < right_parentheses_index: # удаляем из нашего списка все элементы, которые были внутри скобок
            exp_list[left_parentheses_index + 1] = ''
            left_parentheses_index += 1

    
    
    for op in ['/', '*', '+', '-']:
        
        global index_op
        
        while op in exp_list: # здесь находим в списке индекс оператора и ищем слева и справа непустые значения (числа)
            index_op = exp_list.index(op)
            index_prev = index_op - 1
            index_next = index_op + 1
            while exp_list[index_prev] == '':
                index_prev -= 1
            while exp_list[index_next] == '':
                index_next += 1
            exp_list[index_op] = operate(int(exp_list[index_prev]), int(exp_list[index_next]), exp_list[index_op]) # вычисляем найденные числа с текущим оператором, результат кладем на место оператора
            exp_list[index_prev] = '' # удаляем из списка посчитанные числа
            exp_list[index_next] = ''
        
    return exp_list[index_op]


def calc_expression (user_exp: str):
    
    exp = ''
    for char in user_exp:   # удаляем из строки с выражением пробелы и =
        if char != ' ' and char != '=':
            exp = exp + char
    
    signs = ['+', '-', '/', '*', '(', ')'] # далее строку конвертируем в список из чисел, операторов и скобок
    expr =[]
    i, prev_match_index = 0, 0
    while i < len(exp):
        if exp[i] not in signs:
            i += 1
        else:    
            expr.append(exp[prev_match_index : i])
            expr.append(exp[i])
            prev_match_index = i+1
            i += 1
    else:
        expr.append(exp[prev_match_index : i+1])
    
    
    calculate(expr) 
    
    print(calculate(expr))
    

calc_expression('7 +(1+2*(3+4))/3*4/2')
    
    
# 2. Реализовать RLE алгоритм. реализовать модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных файлах (в одном файлике отрывок из какой-то книги,
# а втором файлике — сжатая версия этого текста).


import homeWork_6_RLE_Encoder as rle

with open('hw6_text.txt', 'r') as file:
    text = file.readline()

with open ('hw6_compressedText.txt', 'w') as compressed_file:
    code = rle.encode(text)
    for item in code:
        compressed_file.write(f'{item}\n')

with open('hw6_compressedText.txt', 'r') as comp_file:
    encoded_text = comp_file.readlines()
    
    readed_code = []
    for string in encoded_text:
        readed_code.append(string.rstrip('\n'))
    
    
print(rle.decode(readed_code))

# 3.ROT13 - это простой шифр подстановки букв, который заменяет букву буквой, которая идет через 13 букв после нее в алфавите.
# ROT13 является примером шифра Цезаря.
# Создайте функцию, которая принимает строку и возвращает строку, зашифрованную с помощью Rot13 .
# Если в строку включены числа или специальные символы, они должны быть возвращены как есть.
# Также создайте функцию, которая расшифровывает эту строку обратно (некий начальный аналог шифрования сообщений). 
# Не использовать функцию encode.


def rot13_en_decode (text, key: dict):
    result = ''
    for char in text:
        if char.isupper() and char.lower() in key.keys():
            result += key[char.lower()].upper()
        elif char not in key.keys():
            result += char
        else:
            result += key[char]

    return result


rot13_key = {\
'a':'n',
'b':'o',
'c':'p',
'd':'q',
'e':'r',
'f':'s',
'g':'t',
'h':'u',
'i':'v',
'j':'w',
'k':'x',
'l':'y',
'm':'z',
'n':'a',
'o':'b',
'p':'c',
'q':'d',
'r':'e',
's':'f',
't':'g',
'u':'h',
'v':'i',
'w':'j',
'x':'k',
'y':'l',
'z':'m'}


with open('hw6_text.txt', 'r') as file:
    my_string = file.readline()

my_string = rot13_en_decode(my_string, rot13_key)
print (my_string)

my_string = rot13_en_decode(my_string, rot13_key)
print (my_string)

