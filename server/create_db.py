import sqlite3
from datetime import datetime

def create():
    connection = sqlite3.connect('covid.sqlite')
    connection.execute("PRAGMA foreign_keys = ON")
    connection.execute("""
        CREATE TABLE IF NOT EXISTS city (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            name TEXT
        )""")

    connection.execute("""
        CREATE TABLE IF NOT EXISTS cases (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            date_case TEXT NOT NULL,
            cases_num INTEGER NOT NULL,
            city_id INTEGER NOT NULL,
            FOREIGN KEY(city_id) REFERENCES city(id)
        )""")

    connection.execute("""
        CREATE TABLE IF NOT EXISTS recommendations (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            date_recomm TEXT NOT NULL,
            recom_data FLOAT NOT NULL,
            city_id INTEGER NOT NULL,
            FOREIGN KEY(city_id) REFERENCES city(id)
        )""")
    connection.close()

def city_find(city):
    try:
        sqlite_connection = sqlite3.connect('covid.sqlite')
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite 1")
        cursor.execute(f'SELECT id FROM city WHERE name = "{city}" ')
        city_id = cursor.fetchone()
        print(city_id[0])
        return city_id

    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if sqlite_connection:
            cursor.close()
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")

def cases_in(current_date,cases,city_id):
    try:
        sqlite_connection = sqlite3.connect('covid.sqlite')
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite 2")
        cursor.execute(f'INSERT INTO cases(date_case, cases_num, city_id) VALUES (? ,?, ?)', (current_date, cases, city_id))
        sqlite_connection.commit()
        cursor.close()

    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")


def recomm_in(current_date,rec_data,city_id):
    try:
        sqlite_connection = sqlite3.connect('covid.sqlite')
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite 3")
        cursor.execute(f'INSERT INTO recommendations(date_recomm, recom_data, city_id) VALUES (? ,?, ?)', (current_date, rec_data, city_id))
        sqlite_connection.commit()
        cursor.close()

    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")


def cases_check(current_date, city_id):
    try:
        sqlite_connection = sqlite3.connect('covid.sqlite')
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite 4")
        cursor.execute(f'SELECT * FROM cases WHERE city_id = ? AND date_case = ?', (city_id, current_date))
        result = cursor.fetchall()
        if result == []:
            return False
        else:
            return result[0][2]

    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if sqlite_connection:
            cursor.close()
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")


def rec_check(current_date, city_id):
    try:
        sqlite_connection = sqlite3.connect('covid.sqlite')
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite 5")
        cursor.execute(f'SELECT * FROM recommendations WHERE city_id = ? AND date_recomm = ?', (city_id, current_date))
        result = cursor.fetchall()
        if result == []:
            return False
        else:
            return result[0][2]

    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if sqlite_connection:
            cursor.close()
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")
