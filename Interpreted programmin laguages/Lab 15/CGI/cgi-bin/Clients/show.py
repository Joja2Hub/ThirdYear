#!/usr/bin/env python3

import cgitb
import sqlite3

print("Content-Type: text/html;charset=utf-8\n")

cgitb.enable()

def showData(con):
    cursorObj = con.cursor()
    cursorObj.execute("SELECT * FROM Clients")
    rows = cursorObj.fetchall()
    table_rows = ""
    for row in rows:
        table_rows += f"""
        <tr>
            <th scope="row">{row[0]}</th>
            <td>{row[1]}</td>
            <td>{row[2]}</td>
            <td>{row[3]}</td>
        </tr>
        """
    #result = "\n".join(str(row) for row in cursorObj.fetchall())
    pattern = f"""<!DOCTYPE html>
<html lang = "ru">
    <head>
        <meta charset = "UTF-8">
        <title>Таблица nomenclature_of_medicines</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous">
    </head>
    <body>
        <div class = "container text-center">
            <h1 class="display-6">Окно вывода данных таблицы</h1>
        </div>
        <div>
            <table class="table table-bordered border-primary">
                <thead>
                    <tr>
                        <th scope="row">client_id</th>
                        <th scope="row">first_name</th>
                        <th scope="row">last_name</th>
                        <th scope="row">age</th>
                    </tr>
                </thead>
                <tbody>
                {table_rows}
                </tbody>
            </table>
        </div>
        <div >
            <a href = "http://localhost:8000/index.html"><button class="btn btn-primary">Назад</button></a>
        </div>
    </body>
</html>"""
    print(pattern)
    con.commit()

con = sqlite3.connect("tourism_database.db")
showData(con)
con.close()