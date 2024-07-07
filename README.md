# FinansalVeriYonetimSistemi
Altın, döviz, hisse senetleri, kripto para ve parite verilerini toplayan ve yöneten web uygulaması.

Kullanım Kılavuzu
Gereksinimler
Java Development Kit (JDK): Java uygulamasını çalıştırmak için gereklidir.
Maven: Proje bağımlılıklarını yönetmek ve projeyi derlemek için kullanılır.
Python: Veritabanı betiklerini çalıştırmak için gereklidir.
PostgreSQL: Veritabanı işlemleri için gereklidir.

Kurulum

Java Projesi Kurulumu

Maven kullanarak bağımlılıkları yükleyin:
mvn clean install
Uygulamayı başlatın:
mvn spring-boot:run

Python Betikleri Kurulumu
Gerekli bağımlılıkları yükleyin:

pip install -r requirements.txt

Betikleri çalıştırın:
python db_scripts/altin.py
python db_scripts/cronjob.py
...

Veritabanı Ayarları
PostgreSQL veritabanınızı yapılandırın ve bağlantı ayarlarını Java ve Python projelerine ekleyin.
Kullanım
Web Arayüzü: http://localhost:8080 adresine giderek uygulamayı web tarayıcınızda görüntüleyebilirsiniz.
Veritabanı İşlemleri: Python betiklerini çalıştırarak veritabanı işlemlerini gerçekleştirebilirsiniz.
