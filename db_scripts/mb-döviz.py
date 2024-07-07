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
url = 'https://finans.mynet.com/doviz/merkezbankasi/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Tablodan verileri alıp PostgreSQL veritabanına kaydetme
table = soup.find('table', class_='scrollable')
rows = table.find_all('tr')[1:]  

for row in rows:
    columns = row.find_all('td')
    isim = columns[0].strong.get_text(strip=True)
    alis_deger = columns[2].text
    satis_deger = columns[3].text
    fark = columns[4].text
    tarih = columns[5].text
    
    # Döviz varsa güncelle, yoksa ekle
    cur.execute("SELECT * FROM dovizler WHERE isim = %s", (isim,))
    existing_row = cur.fetchone()
    if existing_row:
        cur.execute("UPDATE dovizler SET alis_deger = %s, satis_deger = %s, fark = %s, tarih = %s WHERE isim = %s",
                    (alis_deger, satis_deger, fark, tarih, isim))
    else:
        cur.execute("INSERT INTO dovizler (isim, alis_deger, satis_deger, fark, tarih) VALUES (%s, %s, %s, %s, %s)",
                    (isim, alis_deger, satis_deger, fark, tarih))

conn.commit()
conn.close()
