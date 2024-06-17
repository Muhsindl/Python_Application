import requests
from bs4 import BeautifulSoup

url=input("Web site adresi https formasında (Ör. https://www.example.com):\n ") #Example:("https://www.example.com")

result=requests.get(url)

try:
    if result.status_code==200:
        html=result.content
        soup = BeautifulSoup(html, "html.parser")
        # p etiketi içerisinde yer alan metini ekrana getirir
        print("p etiketi içeriği:\n")
        print("-"*50)
        print(soup.find("p").text)
    else:
        print("Bağlantı hatası")

except Exception:
    print("Hata")