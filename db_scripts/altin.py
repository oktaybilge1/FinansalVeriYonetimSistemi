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
url = 'https://finans.mynet.com/altin/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Tablodan verileri alıp PostgreSQL veritabanına kaydetme
table = soup.find('table', class_='scrollable')
rows = table.find_all('tr')[1:]  

#Her bir satırı parse edip, veritabanına ekle veya güncelle.
for row in rows:
    columns = row.find_all('td')
    altin = columns[0].h3.a.get_text(strip=True)
    son_deger = columns[2].text
    alis_deger = columns[3].text
    satis_deger = columns[4].text
    fark = columns[5].text
    tarih = columns[6].text.strip()
    
    # Altın varsa güncelle, yoksa ekle
    cur.execute("SELECT * FROM altin WHERE altin = %s", (altin,))
    existing_row = cur.fetchone()
    if existing_row:
        cur.execute("UPDATE altin SET son_deger = %s, alis_deger = %s, satis_deger = %s, fark = %s, tarih = %s WHERE altin = %s",
                    (son_deger, alis_deger, satis_deger, fark, tarih, altin))
    else:
        cur.execute("INSERT INTO altin (altin, son_deger, alis_deger, satis_deger, fark, tarih) VALUES (%s, %s, %s, %s, %s, %s)",
                    (altin, son_deger, alis_deger, satis_deger, fark, tarih))


conn.commit()
conn.close()
