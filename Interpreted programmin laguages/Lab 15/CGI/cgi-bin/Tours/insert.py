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

    tour_id = form.getfirst("tour_id", "-default-")
    name = form.getfirst("name", "-default-")
    price = form.getfirst("price", "-default-")


    tour_id = html.escape(tour_id)
    name = html.escape(name)
    price = html.escape(price)


    temp_list = []

    temp_list.append(tour_id)
    temp_list.append(name)
    temp_list.append(price)


    if tour_id == "-default-" or name == "-default-" or price == "-default-":
        message = "<p>Запись не была вставленна. Пожалуйста, введите все данные корректно.</p>"
    else:
        cursorObj.execute("INSERT INTO Tours(tour_id, name, price) VALUES(?, ?, ?)", temp_list)
        message = f"<p>Тур '{tour_id, name, price}' успешно добавлен в базу данных.</p>"
    pattern = """<!DOCTYPE html>
    <html lang = "ru">
        <head>
            <meta charset = "UTF-8">
            <title>Таблица Tours</title>
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