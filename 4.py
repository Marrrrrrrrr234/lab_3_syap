import json

# Создаем файл 'companies.rtf' с данными о фирмах
with open('companies.rtf', 'w') as data_file:
    data_file.write("firm_1 ООО 10000 5000\n")
    data_file.write("firm_2 ОАО 15000 8000\n")
    data_file.write("firm_3 ИП 3000 2000\n")
    # Добавьте другие строки с данными о фирмах по аналогии

# Теперь ваш код, который читает файл 'companies.rtf' и выполняет расчеты
with open('companies.rtf', 'r') as f:
    companies_list = []
    total_profit = 0
    average_profit = 0
    for line in f:
        name, ownership, revenue, costs = line.split()
        revenue = int(revenue)
        costs = int(costs)
        profit = revenue - costs
        if profit > 0:
            total_profit += profit
        company_dict = {'name': name, 'profit': profit}
        companies_list.append(company_dict)

    num_companies = len(companies_list)

    if num_companies > 0:
        average_profit = total_profit / num_companies

    average_dict = {'average_profit': average_profit}

    result_list = [companies_list, average_dict]

    with open('result.json', 'w') as f:
        json.dump(result_list, f)