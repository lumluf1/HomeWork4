text = input("Введите строку: ")
glasnye = "аеёиоуыэюяaeiou"
glasnye += glasnye.upper()

result = ""
i = 0

while i < len(text):
    if text[i] not in glasnye:
        result += text[i]
    i += 1

print("Результат:", result)