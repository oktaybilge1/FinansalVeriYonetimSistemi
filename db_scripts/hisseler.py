import requests
from bs4 import BeautifulSoup
import psycopg2

# PostgreSQL bağlantı bilgileri
DB_NAME = 'doviz'
DB_USER = 'postgres'
DB_PASSWORD = 'abc123'
DB_HOST = 'localhost'
DB_PORT = '5432'

# PostgreSQL veritabanı bağlantısı
conn = psycopg2.connect(database=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST, port=DB_PORT)
cur = conn.cursor()

# Web sitesinden verileri çekme
url = 'https://finans.mynet.com/borsa/hisseler/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Tablodan verileri alıp PostgreSQL veritabanına kaydetme
table = soup.find('table', class_='scrollable')
rows = table.find_all('tr')[1:]  #

for row in rows:
    columns = row.find_all('td')
    hisse = columns[0].strong.get_text(strip=True)
    son_deger = columns[2].text
    degisim_yuzde = columns[3].text
    hacim = columns[4].text
    saat = columns[5].text
    
    # Hisse varsa güncelle, yoksa ekle
    cur.execute("SELECT * FROM hisseler WHERE hisse = %s", (hisse,))
    existing_row = cur.fetchone()
    if existing_row:
        cur.execute("UPDATE hisseler SET son_deger = %s, degisim_yuzde = %s, hacim = %s, saat = %s WHERE hisse = %s",
                    (son_deger, degisim_yuzde, hacim, saat, hisse))
    else:
        cur.execute("INSERT INTO hisseler (hisse, son_deger, degisim_yuzde, hacim, saat) VALUES (%s, %s, %s, %s, %s)",
                    (hisse, son_deger, degisim_yuzde, hacim, saat))


conn.commit()
conn.close()
