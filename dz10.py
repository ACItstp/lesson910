import requests
import sqlite3
from datetime import datetime

url = "https://wttr.in/Kyiv?format=%t"

response = requests.get(url)
temperature = response.text.strip()

now = datetime.now()

date = now.strftime("%Y-%m-%d")
time = now.strftime("%H:%M:%S")

conn = sqlite3.connect("weather.db")
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS weather (
    date TEXT,
    time TEXT,
    temperature TEXT
)
""")

cur.execute("""
INSERT INTO weather (date, time, temperature)
VALUES (?, ?, ?)
""", (date, time, temperature))


conn.commit()
conn.close()

print("Збережено:")
print("Дата:", date)
print("Час:", time)
print("Температура:", temperature)
