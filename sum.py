from eth_utils import to_checksum_address
import csv

# Укажите путь к вашему CSV файлу
input_file_path = 'TOP 1-50K STAKERS1.csv'
output_file_path = 'TOP 1-50K STAKERS.csv'

# Чтение адресов из CSV файла
addresses = []
with open(input_file_path, 'r') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        if row:  # Проверка на пустую строку
            addr = row[0].strip().rstrip(';')  # Удаление пробелов и символа ';'
            if addr:  # Проверка на пустую строку после обработки
                addresses.append(addr)

# Конвертация
checksum_addresses = [to_checksum_address(addr) for addr in addresses]

# Вывод или сохранение в файл
with open(output_file_path, 'w') as f:
    for addr in checksum_addresses:
        f.write(f"{addr}\n")
