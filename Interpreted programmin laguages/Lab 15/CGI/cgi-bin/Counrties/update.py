
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

    country_id = form.getfirst("country_id", "-default-")
    name = form.getfirst("name", "-default-")

    country_id = html.escape(country_id)
    name = html.escape(name)

    if country_id != "-default-" or name != "-default-":
        temp_list = []
        temp_list.append(name)
        temp_list.append(country_id)

        cursorObj.execute(
            "UPDATE Countries SET name = ? WHERE country_id = ?",
            temp_list)
        message = f"<p>Запись с Id  '{country_id}' была изменена.</p>"
    else:
        message = "<p>Запись не была изменена. Пожалуйста, введите все данные корректо.</p>"
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
        <div>
            <div class = "buttonWrapper" style = "margin-right: 200px;">
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
