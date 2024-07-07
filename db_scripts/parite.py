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
url = 'https://finans.mynet.com/parite/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Tablodan verileri alıp PostgreSQL veritabanına kaydetme
table = soup.find('table', class_='scrollable')
rows = table.find_all('tr')[1:] 

for row in rows:
    columns = row.find_all('td')
    kod = columns[0].strong.a['title']
    isim = columns[1].strong.a['title']
    son_deger = columns[3].text
    alis_deger = columns[4].text
    satis_deger = columns[5].text
    fark = columns[6].text
    tarih = columns[7].text
    
    # Parite varsa güncelle, yoksa ekle
    cur.execute("SELECT * FROM pariteler WHERE kod = %s", (kod,))
    existing_row = cur.fetchone()
    if existing_row:
        cur.execute("UPDATE pariteler SET isim = %s, son_deger = %s, alis_deger = %s, satis_deger = %s, fark = %s, tarih = %s WHERE kod = %s",
                    (isim, son_deger, alis_deger, satis_deger, fark, tarih, kod))
    else:
        cur.execute("INSERT INTO pariteler (kod, isim, son_deger, alis_deger, satis_deger, fark, tarih) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                    (kod, isim, son_deger, alis_deger, satis_deger, fark, tarih))


conn.commit()
conn.close()
