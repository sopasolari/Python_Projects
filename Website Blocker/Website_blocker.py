import time
from datetime import datetime as dt

hosts_path=r"C:\Windows\System32\drivers\etc"
redirect="127.0.0.1"
website_list=["facebook.com","www.facebook.com","pronews.gr","www.pronews.gr"]

while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,10) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,18):
        print("Working hours...")
    else :
        print("Relaxing Time...")

    time.sleep(5)