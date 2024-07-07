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
url = 'https://finans.mynet.com/kripto-para/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Tablodan verileri alıp PostgreSQL veritabanına kaydetme
table = soup.find('div', class_='table-scrollable-mobil').find('table', class_='scrollable')
rows = table.find_all('tr')[1:] 

for row in rows:
    columns = row.find_all('td')
    adi = columns[0].strong.a.get_text(strip=True)
    son_deger = columns[2].text.replace('.', '').replace(',', '.')  # Veriyi doğru formatta almak için
    degisim_yuzde = columns[3].text.replace(',', '.')
    tarih = columns[4].text.strip()
    
    # Kripto para varsa güncelle, yoksa ekle
    cur.execute("SELECT * FROM kripto_para WHERE adi = %s", (adi,))
    existing_row = cur.fetchone()
    if existing_row:
        cur.execute("UPDATE kripto_para SET son_deger = %s, degisim_yuzde = %s, tarih = %s WHERE adi = %s",
                    (son_deger, degisim_yuzde, tarih, adi))
    else:
        cur.execute("INSERT INTO kripto_para (adi, son_deger, degisim_yuzde, tarih) VALUES (%s, %s, %s, %s)",
                    (adi, son_deger, degisim_yuzde, tarih))

conn.commit()
conn.close()
