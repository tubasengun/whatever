import requests, time, random
from bs4 import BeautifulSoup
from selenium import webdriver


browser=webdriver.Chrome('driver/chromedriver.exe')
PROXY_POOL_ENABLED = True
DOWNLOADER_MIDDLEWARES = {
    # ...
    'scrapy_proxy_pool.middlewares.ProxyPoolMiddleware': 610,
    'scrapy_proxy_pool.middlewares.BanDetectionMiddleware': 620,
    # ...
}

browser.get("https://www.webopedia.com/reference/data-formats-and-file-extensions/")
time.sleep(5)
src = browser.page_source

soup = BeautifulSoup(src, 'lxml')
veri=soup.find_all('tr')
file_extension=[]
for satir in range(2,len(veri)-1):
    uzanti=veri[satir].find('td').get_text().strip()
    if uzanti=="" and uzanti=="":
        pass
    else:
        file_extension.append(uzanti)
for extension in file_extension:
    f=open("f_extension.txt","a")
    f.write(extension[1:])
    f.write("\n")
    f.close()