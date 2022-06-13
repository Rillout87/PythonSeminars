
def encode(text):
    result = []
    count = 0
 
    if len(text) == 1:
        result.append((1, int(text[0])))
        return result
 
    for i in range(len(text)):
        count += 1
        if (i + 1) == len(text) or text[i] != text[i + 1]:
            result.append(f'{count}|{text[i]}')
            count = 0
            
    return result


def decode(code: list):
    tuple_code = []
    for item in code:
        tuple_code.append((item.split('|')[0], item.split('|')[1]))
        
    result = ''
    for el in tuple_code:
        result += el[1]*int(el[0])
    
    return result