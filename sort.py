import csv
import operator

def sort_bd(file):
    print('Введите номер столбца для сортировки:\n1. id\n2. Фамилия\n3. Имя\n4. Отчество\n5. Телефон\n6. Отдел\n7. Должность')
    num = int(input())
    reader = open(file, 'r', encoding="utf-8")
    csvf = csv.reader(reader, delimiter = ',')
    sortedlist = sorted(csvf, key=operator.itemgetter(num -1))
    for line in sortedlist:
        print(line)
