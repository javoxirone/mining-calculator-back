import sqlite3

with open('', mode='r', encoding='utf-8') as file:
    for line in file:
        record = line.strip().split(',')
        record.append('cpu')
        print(record)
        db = sqlite3.connect('../db.sqlite3')
        cursor = db.cursor()
        cursor.execute('''
            INSERT INTO main_device(name, energy_rate, income, type) VALUES (?,?,?,?)
        ''', record)
        db.commit()
        db.close()