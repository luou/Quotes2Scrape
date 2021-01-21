import sqlite3
import json

conn = sqlite3.connect('scrapy_mini_project/json_converted.db')
curr = conn.cursor()
curr.execute("""DROP TABLE IF EXISTS json_converted""")
curr.execute("""create table json_converted(
                text text,
                author text, 
                tag text
            )""")

with open('scrapy_mini_project/css-scraper-results.json') as f:
    data = json.load(f)

for row in data:
    curr.execute("""insert into json_converted values(?,?,?)""", (
        row['text'],
        row['author'],
        ','.join(map(str, row['tags'])),
    ))
    conn.commit()

conn.close()
