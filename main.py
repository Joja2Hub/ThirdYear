import sqlite3

# Подключение к базе данных (если файла нет, он будет создан)
conn = sqlite3.connect('tourism_database.db')

# Создание курсора
cursor = conn.cursor()

# Создание таблицы Туры
cursor.execute(
    "CREATE TABLE IF NOT EXISTS Tours (tour_id INTEGER PRIMARY KEY AUTOINCREMENT,name TEXT,price REAL)")

# Вставка данных в таблицу Туры
tours_data = [
    ('Тур 1', 1000),
    ('Тур 2', 1500),
    ('Тур 3', 1200),
    ('Тур 4', 800),
    ('Тур 5', 2000),
    ('Тур 6', 1300),
    ('Тур 7', 900),
    ('Тур 8', 1100),
    ('Тур 9', 1600),
    ('Тур 10', 1800)
]

cursor.executemany('''INSERT INTO Tours (name, price) VALUES (?, ?)''', tours_data)

# Создание таблицы Страны
cursor.execute(
    "CREATE TABLE IF NOT EXISTS Countries(country_id INTEGER PRIMARY KEY AUTOINCREMENT,name TEXT)")


# Вставка данных в таблицу Страны
countries_data = [
    ('Страна 1',),
    ('Страна 2',),
    ('Страна 3',),
    ('Страна 4',),
    ('Страна 5',),
    ('Страна 6',),
    ('Страна 7',),
    ('Страна 8',),
    ('Страна 9',),
    ('Страна 10',),
]

cursor.executemany('INSERT INTO Countries (name) VALUES (?)', countries_data)

# Создание таблицы Клиенты
cursor.execute(
    "CREATE TABLE IF NOT EXISTS Clients (client_id INTEGER PRIMARY KEY AUTOINCREMENT,first_name TEXT,last_name TEXT,age INTEGER)")

# Вставка данных в таблицу Клиенты
clients_data = [
    ('Иван', 'Иванов', 25),
    ('Мария', 'Петрова', 30),
    ('Алексей', 'Сидоров', 28),
    ('Екатерина', 'Козлова', 22),
    ('Дмитрий', 'Федоров', 35),
    ('Анна', 'Смирнова', 29),
    ('Сергей', 'Павлов', 26),
    ('Ольга', 'Морозова', 32),
    ('Павел', 'Васнецов', 31),
    ('Елена', 'Кузнецова', 27)
]

cursor.executemany('INSERT INTO Clients (first_name, last_name, age) VALUES (?, ?, ?)', clients_data)

# Создание таблицы Журнал регистрации продаж туров
cursor.execute(
    "CREATE TABLE IF NOT EXISTS SalesLog (sale_id INTEGER PRIMARY KEY AUTOINCREMENT,client_id INTEGER,tour_id INTEGER,price REAL,FOREIGN KEY (client_id) REFERENCES Clients (client_id),FOREIGN KEY (tour_id) REFERENCES Tours (tour_id))")

# Вставка данных в таблицу Журнал регистрации продаж туров
sales_data = [
    (1, 1, 1000),
    (2, 3, 1200),
    (4, 2, 1500),
    (6, 5, 2000),
    (8, 7, 900),
    (10, 9, 1600),
    (3, 4, 800),
    (5, 6, 1300),
    (7, 8, 1100),
    (9, 10, 1800)
]

cursor.executemany('INSERT INTO SalesLog (client_id, tour_id, price) VALUES (?, ?, ?)', sales_data)

# Сохранение изменений и закрытие соединения

#Обновление:
cursor.execute("UPDATE Tours SET price=1200 WHERE tour_id=1")

cursor.execute("UPDATE Clients SET age=40 WHERE client_id=5")

cursor.execute("UPDATE Countries SET name='Новая страна' WHERE country_id=3")
#Удаление данных:

cursor.execute("DELETE FROM Tours WHERE tour_id=2")

cursor.execute("DELETE FROM Clients WHERE client_id=8")

cursor.execute("DELETE FROM Countries WHERE country_id=6")

cursor.execute("DROP TABLE ")
#Добавление данных:


cursor.execute("INSERT INTO Tours (name, price) VALUES ('Тур 11', 1500)")

cursor.execute("INSERT INTO Clients (first_name, last_name, age) VALUES ('Андрей', 'Ковалев', 33)")

cursor.execute("INSERT INTO Countries (name) VALUES ('Страна 11')")

conn.commit()
conn.close()