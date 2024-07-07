from apscheduler.schedulers.background import BackgroundScheduler
import subprocess

# İlk script
def job1():
    subprocess.call(["python", "C:/Users/bilge/OneDrive/Masaüstü/GÖRSEL PROG POJE/db_scripts/altin.py"])


# İkinci script
def job2():
    subprocess.call(["python", "C:/Users/bilge/OneDrive/Masaüstü/GÖRSEL PROG POJE/db_scripts/hisseler.py"])


# Üçüncü script
def job3():
    subprocess.call(["python", "C:/Users/bilge/OneDrive/Masaüstü/GÖRSEL PROG POJE/db_scripts/kripto.py"])


# Dördüncü script
def job4(): 
    subprocess.call(["python", "C:/Users/bilge/OneDrive/Masaüstü/GÖRSEL PROG POJE/db_scripts/mb-döviz.py"])


# Beşinci script
def job5():
    subprocess.call(["python", "C:/Users/bilge/OneDrive/Masaüstü/GÖRSEL PROG POJE/db_scripts/parite.py"])


scheduler = BackgroundScheduler()

# Beş scripti de 1 dakikada bir çalıştırır.
scheduler.add_job(job1, 'interval', minutes=1)
scheduler.add_job(job2, 'interval', minutes=1)
scheduler.add_job(job3, 'interval', minutes=1)
scheduler.add_job(job4, 'interval', minutes=1)
scheduler.add_job(job5, 'interval', minutes=1)

scheduler.start()

try:
    while True:
        pass
except KeyboardInterrupt:
    
    scheduler.shutdown()
