
#!/usr/bin/env python3

print("Content-Type: text/html;charset=utf-8\n")

import cgi
import cgitb
import sqlite3
import html

cgitb.enable()

message = ""

def changeData(con):
    global message
    cursorObj = con.cursor()
    form = cgi.FieldStorage()

    tour_id = form.getfirst("tour_id", "-default-")
    name = form.getfirst("name", "-default-")
    price = form.getfirst("price", "-default-")

    tour_id = html.escape(tour_id)
    name = html.escape(name)
    price = html.escape(price)


    if tour_id != "-default-" or name != "-default-" or price != "-default-":
        temp_list = []
        temp_list.append(name)
        temp_list.append(price)
        temp_list.append(tour_id)

        cursorObj.execute(
            "UPDATE Tours SET name = ?, price = ? WHERE tour_id = ?",
            temp_list)
        message = f"<p>Запись с Id  '{tour_id}' была изменена.</p>"
    else:
        message = "<p>Запись не была изменена. Пожалуйста, введите все данные корректо.</p>"
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
        <div>
            <div style = "margin-right: 200px;">
                <a href = "http://localhost:8000/index.html"><button>Назад</button></a>
            </div>
        </div>
    </body>
</html>"""
    print(pattern.format(message))
    con.commit()


con = sqlite3.connect("tourism_database.db")
changeData(con)
con.close()
