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

    country_id = form.getfirst("country_id", "-default-")
    name = form.getfirst("name", "-default-")

    country_id = html.escape(country_id)
    name = html.escape(name)
    temp_list = []

    temp_list.append(country_id)
    temp_list.append(name)

    if country_id == "-default-" or name == "-default-":
        message = "<p>Запись не была вставленна. Пожалуйста, введите все данные корректно.</p>"
    else:
        cursorObj.execute("INSERT INTO Countries(country_id, name) VALUES(?, ?)", temp_list)
        message = f"<p>Страна  '{country_id, name}' успешно добавлена в базу данных.</p>"
    pattern = """<!DOCTYPE html>
<html lang = "ru">
    <head>
        <meta charset = "UTF-8">
        <title>Таблица Counrties</title>
    </head>
    <body>
        <div>
            {}
        </div>
        <div class = "buttonWrapper" style = "margin-right: 100px;">
            <a href = "http://localhost:8000/index.html"><button>Назад</button></a>
        </div>
    </body>
</html>"""
    print(pattern.format(message))
    con.commit()

con = sqlite3.connect("tourism_database.db")
insertData(con)
con.close()