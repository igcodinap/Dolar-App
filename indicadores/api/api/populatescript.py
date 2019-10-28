from datetime import timedelta, date
import requests
import sqlite3
import time
from statistics import mean

conn = sqlite3.connect('../db.sqlite3')
c = conn.cursor()


def daterange(start_date, end_date):
    for n in range(int ((end_date - start_date).days)):
        yield start_date + timedelta(n)

def DBConnection(f, v):
    c.execute("INSERT INTO core_dolar(fecha, valor) VALUES(?,?)",(f,v))
    conn.commit()
    c.execute('SELECT * FROM core_dolar')
    print(c.fetchall())

start_date = date(2018, 1, 1)
end_date = date(2019, 10, 27)
for single_date in daterange(start_date, end_date):
    todaydate = single_date.strftime("%d-%m-%Y")
    response = requests.get('https://mindicador.cl/api/dolar/'+todaydate)
    time.sleep(20)
    dolardata = response.json()
    if dolardata['serie']:
        date = dolardata['serie'][0]['fecha'][0:10]
        value = dolardata['serie'][0]['valor']
        print(date)
        print(value)
        DBConnection(date, value)

conn.close()
