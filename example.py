#import sqlite3 

# открываем файл с базой данных
#con = sqlite3.connect('marvel.db')

# создаём таблицу 
#with con:
#    con.execute("""
#        CREATE TABLE marvel (
#            ID INTEGER PRIMARY KEY,
#            name TEXT,
#            superpower TEXT,
#            status TEXT);""")

#with con:
#    con.execute("DROP TABLE marvel")

# подготавливаем запрос
#sql = 'INSERT INTO marvel (ID, name, superpower, status) values(?, ?, ?, ?)'

# указываем данные для запроса
#data = [
#    (1, 'Халк', 'Суперсила', 'За добро'),
#    (2, 'Тор', 'Молот', 'За добро'),
#]

# добавляем с помощью множественного запроса все данные сразу
#with con:
#    con.executemany(sql, data)

# Обновляем статус Халка
# with con:
#     con.execute("UPDATE marvel SET status = 'За зло' WHERE name = ?",('Халк',))

# Удаляем запись с Тором
# with con:
#     con.execute("DELETE FROM marvel WHERE name = ?",('Тор',))



# ДОП ЗАДАНИЕ
#foods = [("Цезарь", "150 руб", "100 гр"), ("Крабовый салат", "125 руб", "100 гр"), ("Салат с курицей и ананасами", "300 руб", "100 гр")]
foods = {150 : "Цезарь", 125 : "Крабовый салат", 300 : "Салат с курицей и ананасами"}
sortedfood = sorted(foods.items())
sorted_dict = dict(sortedfood)

print(sorted_dict)

foods2 = {"150 руб": ("Цезарь", "100 гр"), "125 руб" : ("Крабовый салат", "100 гр"), "300 руб" : ("Салат с курицей и ананасами", "100 гр")}
sortedfood2 = sorted(foods2.items())
sorted_dict2 = dict(sortedfood2)

print(sorted_dict2)
