#!/usr/bin/env python3

print("Content-Type: text/html;charset=utf-8\n")

import cgi
import cgitb
import sqlite3
import html

cgitb.enable()

message = ""

def insertData(con):
    global message
    cursorObj = con.cursor()
    form = cgi.FieldStorage()

    client_id = form.getfirst("client_id", "-default-")
    first_name = form.getfirst("first_name", "-default-")
    last_name = form.getfirst("last_name", "-default-")
    age = form.getfirst("age", "-default-")

    client_id = html.escape(client_id)
    first_name = html.escape(first_name)
    last_name = html.escape(last_name)
    age = html.escape(age)


    temp_list = []

    temp_list.append(client_id)
    temp_list.append(first_name)
    temp_list.append(last_name)
    temp_list.append(age)


    if first_name== "-default-" or last_name == "-default-" or age == "-default-":
        message = "<p>Запись не была вставленна. Пожалуйста, введите все данные корректно.</p>"
    else:
        cursorObj.execute("INSERT INTO Clients(client_id, first_name, last_name, age) VALUES(?, ?, ?, ?)", temp_list)
        message = f"<p>Клиент '{first_name, last_name, age}' успешно добавлен в базу данных.</p>"
    pattern = """<!DOCTYPE html>
<html lang = "ru">
    <head>
        <meta charset = "UTF-8">
        <title>Таблица Clients</title>
    </head>
    <body>
        <div>
            {}
        </div>
        <div style = "margin-right: 100px;">
            <a href = "http://localhost:8000/index.html"><button>Назад</button></a>
        </div>
    </body>
</html>"""
    print(pattern.format(message))
    con.commit()

con = sqlite3.connect("tourism_database.db")
insertData(con)
con.close()