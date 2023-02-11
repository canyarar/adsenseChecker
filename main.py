import time
import requests
from bs4 import BeautifulSoup

while True:
    # Belirli bir URL'yi isteyin
    url = "https://www.website.net"
    page = requests.get(url)

    # Sayfanın HTML kaynağını çekin
    soup = BeautifulSoup(page.content, 'html.parser')

    # AdSense reklamlarını arayın
    if soup.find("ins", class_="adsbygoogle"):
        print("\033[92m AdSense reklamı bulundu.\033[0m")
    else:
        print("\033[91m AdSense reklamı bulunamadı.\033[0m")

    # 5 dakika bekleyin
    time.sleep(300)
