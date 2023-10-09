# Открываем файл F1 для записи данных
with open('F1.txt', 'w') as f:
    pass
    while True:
        line = input("Введите строку (пустая строка - окончание ввода): ")
        if not line:
            break
        f.write(line + '\n')

max_digit_count = 0
max_digit_word = ''
max_word_num = -1

# Открываем файлы F1 и F2 для чтения и записи соответственно
with open('F1.txt', 'r') as f1, open('F2.txt', 'w') as f2:
    # Создаем словарь для отслеживания количества цифр в каждом слове
    word_digit_count = {}

    # Инициализируем счетчик слов
    word_number = 0

    # Чтение строк из F1 и запись в F2, учитывая условие наличия не менее двух одинаковых слов
    for line in f1:
        words = line.split()

        # Подсчет количества цифр в каждом слове и сохранение информации о словах
        for word in words:
            word_number += 1
            digit_count = sum(1 for char in word if char.isdigit())

            if word not in word_digit_count:
                word_digit_count[word] = (1, digit_count, word_number)
            else:
                word_count, _, _ = word_digit_count[word]

                word_digit_count[word] = (word_count + 1, digit_count, word_number)

        # Проверка на наличие не менее двух одинаковых слов в строке
        for word, (word_count, count, word_num) in word_digit_count.items():
            if word_count >= 2:
                f2.write(line)
                break

        # Определение слова с наибольшим количеством цифр и номера этого слова
        if len(word_digit_count) > 0:
            word, (_, digit_count, word_num) = max(word_digit_count.items(), key=lambda x: x[1])

            if digit_count > max_digit_count:
                max_digit_count = digit_count
                max_word_num = word_num
                max_digit_word = word

        word_digit_count.clear()



# Вывод результата
print(f"Строки с одинаковыми словами из F1 были скопированы в F2.")

if (max_digit_count > 0):
    print(f"Слово с наибольшим количеством цифр: {max_digit_word}, количество цифр: {max_digit_count}")
    print(f"Номер слова с наибольшим количеством цифр: {max_word_num}")
else:
    print("Слова с цифрами не найдено!")