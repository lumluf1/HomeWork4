text = input("Введите свой произвольный текст: ")

otrezok = input("Введите отрезок, от какого символа до какого требуется вывести строку через пробел: ")

symbol1, symbol11 = map(int, otrezok.split())

print(text[symbol1:symbol11])
