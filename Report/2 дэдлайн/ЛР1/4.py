from random import randint
random_num = randint(1, 100)

print("Программа загадала число от 1 до 100. Угадай это число!")

while True:
    popytka = int(input("Попытка: "))
    
    if popytka == random_num:
        print("Угадал!")
        break
    
    elif popytka > random_num:
        print("Меньше")
        
    else:
        print("Больше")
        
    