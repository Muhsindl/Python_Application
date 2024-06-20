import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from urllib.parse import urljoin

url = "https://www.kitapsec.com/Products/KPSS-Kitaplari/"

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")

driver = webdriver.Chrome(options=options)
driver.get(url)
time.sleep(4)

kitap_elements = driver.find_elements(By.XPATH, "//div[@class='Ks_UrunSatir']//a[@href]")
kitap_urls = [element.get_attribute("href") for element in kitap_elements]

# URL'leri kontrol et ve eksik protokol varsa ekle
base_url = "https://www.kitapsec.com"
kitap_urls = [urljoin(base_url, href) for href in kitap_urls]

name = []
price = []

for kitap_url in kitap_urls:
    try:
        driver.get(kitap_url)
        time.sleep(2)  # Sayfanın yüklenmesi için bekle

        # Kitap ismini al
        elem = driver.find_element(By.XPATH, "//h1[@itemprop='name']")
        name.append(elem.text)

        # Kitap fiyatını al
        eleman = driver.find_element(By.XPATH, "//span[@class='piyasa2']/following-sibling::*[1]")
        price.append(eleman.text)
    except Exception as e:
        print(f"Hata {kitap_url} URL'sinde: {e}")

driver.quit()

print("Kitap İsimleri:", name)
print("Kitap Fiyatları:", price)
