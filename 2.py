# Создаем файл
with open('childrens_products.txt', 'w') as data_file:
            # Write the names of children's products and their prices, one product per line
            data_file.write("Toy1 55.99\n")
            data_file.write("Book1 12.50\n")
            data_file.write("Puzzle1 25.00\n")
            data_file.write("Ball1 80.99\n")
            data_file.write("Building 19.95\n")
            data_file.write("Doll1 14.75\n")
            data_file.write("Toy2 111.99\n")
            data_file.write("Book2 9.50\n")
            data_file.write("Puzzle2 29.00\n")
            data_file.write("Ball2 12.99\n")

# Открываем файл 'childrens_products.txt' для чтения
with open('childrens_products.txt', 'r') as f:
    # Создаем пустой список для хранения товаров с ценой от 10 до 50 рублей
    affordable_products = []

    total_cost = 0  # Инициализируем сумму стоимостей
    num_products = 0  # Инициализируем количество товаров

    # Чтение строк из файла
    for line in f:
        name, cost = line.split()  # Разбиваем строку на название и стоимость
        cost = float(cost)  # Преобразуем стоимость в число

        total_cost += cost  # Добавляем стоимость к общей сумме
        num_products += 1  # Увеличиваем счетчик товаров

        if 10 <= cost <= 50:  # Проверяем, что стоимость от 10 до 50 рублей
            affordable_products.append(name)  # Добавляем товар в список

    # Выводим товары с подходящей стоимостью
    if affordable_products:
        print("Products with prices from 10 to 50 rubles:", ', '.join(affordable_products))
    else:
        print("No products with prices from 10 to 50 rubles.")

    # Calculate the average cost of products
    if num_products > 0:
        avg_cost = total_cost / num_products
        print("Average product cost:", avg_cost)
    else:
        print("No data available for product prices.")