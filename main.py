#Запрашивает у пользователя строку для поиска.
import io
with io.open("ipo-lr6-text.txt", "r", encoding="utf-8") as file:#с открытием файла читать его
    line = file.readlines()
search_string = input("введите строку для поиска -- ")

f_line = []  
a = 0

for i in line:#i в каждой строке файла
    if search_string in i:#если искомая подстрока в i
        f_line.append(i) #выводит строку
        a += 1

if f_line:
    f_sorted = sorted(f_line, key = len)#сортирует строки по длинк
    for f_i in f_sorted:
        print("Строка:  ", f_i)
else:
    print("нету :(")
print("Колво найденных строк -- ", a)
