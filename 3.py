# Создаем файл 'учебные_предметы.txt' с данными о учебных предметах и занятиях
with open('educational_subjects.txt', 'w') as data_file:
    data_file.write("Mathematics: Lectures(20) Practicals(10) Laboratories(5)\n")
    data_file.write("Physics: Lectures(15) Practicals(8)\n")
    data_file.write("History: Lectures(20) Seminars(15)\n")
    # Добавьте другие строки с данными о предметах по аналогии

# Открываем файл для чтения
with open('educational_subjects.txt', 'r') as f:
    subjects_dict = {}

    # Чтение строк из файла
    for line in f:
        subject_info = line.split(':')  # Разбиваем строку на название предмета и информацию о занятиях
        subject = subject_info[0].strip()  # Название предмета
        lessons_info = subject_info[1].split()  # Информация о занятиях

        total_lessons = 0  # Инициализируем общее количество занятий

        # Парсим информацию о занятиях
        for lesson_info in lessons_info:
            lesson_parts = lesson_info.split('(')  # Разбиваем строку на тип занятия и количество
            if len(lesson_parts) == 2:  # Убеждаемся, что строка содержит тип и количество
                num_lessons = int(lesson_parts[1].strip(')'))  # Количество занятий
                total_lessons += num_lessons

        subjects_dict[subject] = total_lessons  # Добавляем в словарь

    # Выводим словарь с названием предмета и общим количеством занятий
    print(subjects_dict)