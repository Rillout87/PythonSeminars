# Напишите программу, удаляющую из текста все слова содержащие "абв", которое регистронезависимо. Используйте знания с последней лекции. Выполните ее в виде функции. 
# Пример: «абвгдеж рабав копыто фабв Абкн абрыволк аБволк»

from functools import reduce


text = "абвгдеж рабав копыто фабв Абкн абрыволк аБволк"
subtext = "абв"


result = " ".join([i for i in text.split() if not subtext.lower() in i.lower()])


print (result)


# 3. 3. Вот вам текст:
#Отфильтруйте его, чтобы этот текст можно было нормально прочесть. Предусмотрите вариант, что мусорные слова могли быть написаны без использования запятых.

dirtyText = "«Ну, вышел я, короче, из подъезда. В общем, короче говоря, шел я, кажется, в магазин. Ну,эээ, в общем, было лето, кажется. \
Как бы тепло. Солнечно, короче. Иду я, иду, в общем, по улице, а тут, короче, яма. Я, эээээ…. Упал в нее. И снова вышел, короче, из подъезда.\
Ясен пень, в магазин. В общем, лето на дворе, жарко, солнечно, птицы, короче, летают. Кстати, иду я по улице, иду, а тут, короче, яма. \
Ну, я в нее упал, в общем. Вышел из подъезда, короче. Лето на дворе, ясен пень. Птицы поют, короче, солнечно. В общем, в магазин мне надо. \
Что-то явно не так, короче. «Рекурсия», - подумал я. Ээээ...короче, в общем, пошел другой дорогой и не упал в эту… ээээ… яму. Хлеба купил»."

dirtyWords = ['ну', 'короче говоря', 'короче', 'в общем', 'кажется', 'эээээ', 'ээээ', 'эээ', 'как бы', 'ясен пень', 'кстати']

dirtyText = dirtyText.lower()


for word in dirtyWords:
    while True:
        if dirtyText.find(word) == -1: break
        cutStartIndex = dirtyText.find(word)
        cutEndIndex = cutStartIndex + len(word)
        
        while True:
            if dirtyText[cutStartIndex] == '«': break
            cutStartIndex -= 1
            if dirtyText[cutStartIndex].isalpha() or dirtyText[cutStartIndex] == '.':
                break
        
        while True:
            if dirtyText[cutEndIndex] == '.' or dirtyText[cutEndIndex] == '»': break
            
            cutEndIndex += 1
            if dirtyText[cutEndIndex].isalpha():
                break

        dirtyText = dirtyText[:cutStartIndex + 1] + " " + dirtyText[cutEndIndex:]    

dirtyText = dirtyText.replace('«', '').replace('»', '').split('.')
dirtyText = '«' + '. '.join([sentence.strip().capitalize() for sentence in dirtyText if sentence.strip() != '']) + '»'


print(dirtyText)


# 4. Чисто для тренировки новый функций, ничего сложного. Создайте два списка — один с названиями языков программирования,
# другой — с числами от 1 до длины первого плюс 1. Вам нужно сделать две функции: первая из которых создаст список кортежей,
# состоящих из номера и языка, написанного большими буквами. Вторая — которая отфильтрует этот список следующим образом:
# если сумма очков слова имеет в делителях номер, с которым она в паре в кортеже, то кортеж остается, его номер заменяется на
# сумму очков. Если нет — удаляется. Суммой очков называется сложение порядковых номеров букв в слове. Порядковые номера смотрите
# в этой таблице, в третьем столбце: https://www.charset.org/utf-8
# Это — 16-ричная система, поищите, как правильнее и быстрее получать эти символы.
# С помощью reduce сложите получившиеся числа и верните из функции в качестве ответа.

languages = ['CSharp', 'Phyton', 'JavaScript', 'PHP', 'C++', 'Go', 'Arduino', 'R', 'C']
numbers = list(range(1, len(languages) + 1))


def tupleMaker (list1, list2: str):
   return list(map(lambda a,b: (a, b.upper()), list1, list2))


def myFilter(TupleList):
   pointsSum = []
   for tup in TupleList:
      pointsSum.append(sum([ord(i) for i in tup[1]]))

   TupleList = list(map(lambda a, b: (a[0], a[1], b), TupleList, pointsSum))
   TupleList = [i[2] for i in filter(lambda s: not s[2] % s[0], TupleList)]
   
   return reduce(lambda x, y: x + y, TupleList)

 

print(myFilter(tupleMaker(numbers, languages)))

