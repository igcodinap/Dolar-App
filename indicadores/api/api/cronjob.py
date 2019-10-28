import DBConnection from 'populatescript.py'
from datetime import date

def my_scheduled_job():
    date = date.today()
    todaydate = date.strftime("%d-%m-%Y")
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
