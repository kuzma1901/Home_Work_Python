# Напишите программу, удаляющую из текста все слова, содержащие заданную строку.

# Пример:
# Пугать ты галок пугай => заданная строка "пугай" => Пугать ты галок


text = input("Введите исходный текст: ")
find_word = "пугай"
lst_a = [i for i in text.split() if find_word not in i]
print(f'Результат: {"_".join(lst_a)}')