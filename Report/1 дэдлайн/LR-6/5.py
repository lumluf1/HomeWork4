text = input("Введите свой произвольный текст: ")
search = input("Введите своё слово из текста для поиска: ")

vstrochennoe = text.count(search)
index = text.find(search)

print("Количество встроченных слов: ", vstrochennoe)
print("Индекс первого встроченного слова: ", index)

text2 = text.replace(search,"")

print("Ваш полученный текст: ", text2)