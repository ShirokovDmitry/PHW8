import csv
import operator

def sort_st(file):

    with open(file, 'r', encoding="utf-8") as f:
        print('Введите номер столбца для вывода:\n1. id\n2. Фамилия\n3. Имя\n4. Отчество\n5. Телефон\n6. Отдел\n7. Должность')
        num = int(input())
        csvf = csv.reader(f, delimiter = ',')
        sortedlist = sorted(csvf, key=operator.itemgetter(num -1))
        for row in sortedlist:
            col = row[num -1]
            print(col)