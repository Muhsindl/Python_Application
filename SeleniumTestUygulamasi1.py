import requests
from bs4 import BeautifulSoup
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

#Chrome olarak tarayıcıyı seçtik ve tam ekranda açılmasını istedik
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")

driver = webdriver.Chrome(options)

#Web site linkini belirttik
driver.get("https://books.toscrape.com/")
time.sleep(2)
#Web sitemizde yer alan a etiketlerinden "Travel" ya da "Nonfiction" yazılarını seçtik
category_elements_xpath ="//a[contains(text(),'Travel') or contains(text(),'Nonfiction')]"
category_elements=driver.find_elements(By.XPATH,category_elements_xpath)
#Linkleri category_urls isimli dizinin içerisine ekledik
category_urls=[element.get_attribute("href") for element in category_elements]
print(category_urls)

#Kitapları aldık
book_elements_xpath="//div[@class='image_container']//a"
book_elements=driver.find_elements(By.XPATH,book_elements_xpath)
book_urls=[element.get_attribute("href") for element in book_elements]
#Toplam kitap sayısını ve kitap bağlantılarını ekrana yazdırdık
print(book_urls)
print("Bulunan kitap sayısı:",len(book_urls))

#Dinamik olarak sayfalar arası geçiş yaparak bağlantı bilgilerini topladık
url=category_urls[0]
for i in range(1,3):
    update_url=url if i==1 else url.replace("index",f"page-{i}")
    driver.get(update_url)
    book_elements=driver.find_elements(By.XPATH,book_elements_xpath)
    if not book_elements:
        break
    temp_urls=[element.get_attribute("href") for element in book_elements]
    book_urls.extend(temp_urls)
#Kitap bağlantılarını ve kaç adet kitap olduğunu ekrana yazdırdık
print(book_urls)
print(len(book_urls))

driver.get(book_urls[0])
time.sleep(2)
content_div=driver.find_elements(By.XPATH,"//div[@class='content']")

inner_html=content_div[0].get_attribute("innerHTML")

soup=BeautifulSoup(inner_html,"html.parser")

#Kitap adını getirir
name_elem=soup.find("h1")
book_name=name_elem.text

#Kitap fiyatını getirir
price_elem=soup.find("p",attrs={"class":"price_color"})
book_price=price_elem.text

#Kitap yıldınızını getirir
import re
regex=re.compile("^star-rating ")
star_elem=soup.find("p",attrs={"class":regex})
print(star_elem)
book_star_count=star_elem["class"][-1]

#Kitap açıklaması
desc_elem=soup.find("div",attrs={"id":"product_description"}).find_next_sibling()
book_desc=desc_elem.text

#Product Information Başlığı altında kalan tabloda ki bilgiler
product_info={}
table_rows=soup.find("table").find_all("tr")
for row in table_rows:
    key=row.find("th").text
    value=row.find("td").text
    product_info[key]=value

