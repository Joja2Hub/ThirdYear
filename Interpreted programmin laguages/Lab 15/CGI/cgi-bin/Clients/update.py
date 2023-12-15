
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

    client_id = form.getfirst("client_id", "-default-")
    first_name = form.getfirst("first_name", "-default-")
    last_name = form.getfirst("last_name", "-default-")
    age = form.getfirst("age", "-default-")

    client_id = html.escape(client_id)
    first_name = html.escape(first_name)
    last_name = html.escape(last_name)
    age = html.escape(age)

    if client_id != "-default-" or first_name != "-default-" or last_name != "-default-" or age != "-default-":
        temp_list = []
        temp_list.append(first_name)
        temp_list.append(last_name)
        temp_list.append(age)
        temp_list.append(client_id)

        cursorObj.execute(
            "UPDATE Clients SET first_name = ?, last_name = ?, age = ? WHERE client_id = ?",
            temp_list)
        message = f"<p>Запись с Id = '{client_id}' была изменена.</p>"
    else:
        message = "<p>Запись не была изменена. Пожалуйста, введите все данные корректо.</p>"
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
        <div>
            <div style = "margin-right: 200px;">
                <a href = "http://localhost:8000/index.html"><button>Назад</button></a>
            </div>
        </div>
    </body>
</html>"""
    print(pattern.format(message))
    con.commit()

def showById(con):
    global message
    result = []
    cursorObj = con.cursor()
    form = cgi.FieldStorage()

    id = form.getfirst("first_name", "-default-")
    id = html.escape(id)
    if id == "-default-":
        cursorObj.execute("SELECT FROM Clients WHERE clients_id = " + id + ";")
        con.commit()
        result = cursorObj.fetchall()
    return result

con = sqlite3.connect("tourism_database.db")
changeData(con)
con.close()
