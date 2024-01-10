import time
from PIL import Image
import requests
import base64
import io
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import os
yemekler =[]

def google(yemek):
    options = ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument("--no-sandbox")
    options.add_experimental_option("useAutomationExtension", False)
    options.add_experimental_option("excludeSwitches", ["enable-automation"])

    driver = webdriver.Chrome(options=options)

    url = ("https://www.google.com/search?q={s}&tbm=isch&tbs=sur%3Afc&hl=en&ved=0CAIQpwVqFwoTCKCa1c6s4-oCFQAAAAAdAAAAABAC&biw=1251&bih=568")

    driver.get(url.format(s=yemek))

    for x in range(10):
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
        time.sleep(2)

    imgResults = driver.find_elements(By.XPATH,"//img[contains(@class,'Q4LuWd')]")
    src = [img.get_attribute('src') for img in imgResults]
    try:
        os.mkdir(yemek.replace(" ","."))
    except FileExistsError:
        pass
    
    for i in range(len(src)):
    
        for src_item in src:
            if src_item is None:
                pass
        
                if src[i].startswith('data'):
                    imgdata = base64.b64decode(str(src[i]).split(',')[1])
                    img = Image.open(io.BytesIO(imgdata))
                    dosya_yolu = os.path.join(yemek.replace(" ","."),yemek.replace(" ",".")+f"{i}.png")
                    img.save(dosya_yolu, format='PNG')  
                else:
                    img = Image.open(requests.get(src, stream=True).raw).convert('RGB')
                    dosya_yolu = os.path.join(yemek.replace(" ","."),yemek.replace(" ",".")+f"{i}.jpg")
                    img.save(dosya_yolu, format='JPEG')
def pinterest(yemek):
    options = ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument("--no-sandbox")
    options.add_experimental_option("useAutomationExtension", False)
    options.add_experimental_option("excludeSwitches", ["enable-automation"])

    driver = webdriver.Chrome(options=options)

    url = ("https://tr.pinterest.com/search/pins/?q={s}&rs=typed")

    driver.get(url.format(s=yemek))
    try:
        os.mkdir(yemek.replace(" ","."))
    except FileExistsError:
        pass
        
    for x in range(10):
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
        time.sleep(2)

    imgResults = driver.find_elements(By.XPATH,"//img[contains(@class,'hCL kVc L4E MIw')]")
    src = [img.get_attribute('src') for img in imgResults]
    for i in range(len(src)):
    
        for src_item in src:
            if src_item is None:
                pass
            else:
                img = Image.open(requests.get(src_item, stream=True).raw).convert('RGB')
                dosya_yolu = os.path.join(yemek.replace(" ","."), yemek.replace(" ",".") + f"{i}.jpg")
                img.save(dosya_yolu, format='JPEG')
def pexels(yemek):
    options = ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument("--no-sandbox")
    options.add_experimental_option("useAutomationExtension", False)
    options.add_experimental_option("excludeSwitches", ["enable-automation"])

    driver = webdriver.Chrome(options=options)

    url = ("https://www.pexels.com/search/{s}/")

    driver.get(url.format(s=yemek))

    for x in range(6):
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
        time.sleep(2)
    foto1=driver.find_elements(By.XPATH,"//*[@id='-']/div[1]/div/div[1]/div")
    foto2=driver.find_elements(By.XPATH,"//*[@id='-']/div[1]/div/div[2]/div")
    foto3=driver.find_elements(By.XPATH,"//*[@id='-']/div[1]/div/div[3]/div")
    try:
        os.mkdir(yemek.replace(" ","."))
    except FileExistsError:
        pass
    
    for i in range(len(foto1)):
        
        try:
            imgResults = driver.find_element(By.XPATH, "//*[@id='-']/div[1]/div/div[1]/div["+str(i)+"]/article/a/img")
            src = imgResults.get_attribute('src')
            if src is None:
                pass
            else:
                img = Image.open(requests.get(src, stream=True).raw).convert('RGB')
                dosya_yolu = os.path.join(yemek.replace(" ","."),yemek.replace(" ",".")+f"{i}.jpg")
                img.save(dosya_yolu, format='JPEG')
        except NoSuchElementException:
            pass

    for i in range(len(foto2)):
        try:
            imgResults = driver.find_element(By.XPATH, "//*[@id='-']/div[1]/div/div[1]/div["+str(i)+"]/article/a/img")
            src = imgResults.get_attribute('src')
            if src is None:
                pass
            else:
                img = Image.open(requests.get(src, stream=True).raw).convert('RGB')
                dosya_yolu = os.path.join(yemek.replace(" ","."),yemek.replace(" ",".")+f"{i}.jpg")
                img.save(dosya_yolu, format='JPEG')
        except NoSuchElementException:
            pass  

    for i in range(len(foto3)):
        try:
            imgResults = driver.find_element(By.XPATH, "//*[@id='-']/div[1]/div/div[1]/div["+str(i)+"]/article/a/img")
            src = imgResults.get_attribute('src')
            if src is None:
                pass
            else:
                img = Image.open(requests.get(src, stream=True).raw).convert('RGB')
                dosya_yolu = os.path.join(yemek.replace(" ","."),yemek.replace(" ",".")+f"{i}.jpg")
                img.save(dosya_yolu, format='JPEG')
        except NoSuchElementException:
            pass  
def shutterstock(yemek):
    options = ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument("--no-sandbox")
    options.add_experimental_option("useAutomationExtension", False)
    options.add_experimental_option("excludeSwitches", ["enable-automation"])

    driver = webdriver.Chrome(options=options)

    url = ("https://www.shutterstock.com/tr/search/{s}")

    driver.get(url.format(s=yemek))
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight/5);")
    time.sleep(1)
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight/3);")
    time.sleep(1)
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight/2);")
    time.sleep(1)
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight/1.5);")
    time.sleep(1)
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight/1.2);")
    time.sleep(1)
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
    time.sleep(1)
    imgResults = driver.find_elements(By.XPATH,"//*[@id='__next']/div[3]/div/div/div[1]/div/div[6]/div[1]/div[2]/div")
    time.sleep(3)
    try:
        os.mkdir(yemek.replace(" ","."))
    except FileExistsError:
        pass
    
    for i in range(len(imgResults)):
        
        try:
            imgResults = driver.find_element(By.XPATH, "//*[@id='__next']/div[3]/div/div/div[1]/div/div[6]/div[1]/div[2]/div["+str(i)+"]/div[2]/div/picture/img")
            src = imgResults.get_attribute('src')
            if src is None:
                pass
            else:
                img = Image.open(requests.get(src, stream=True).raw).convert('RGB')
                dosya_yolu = os.path.join(yemek.replace(" ","."),yemek.replace(" ",".")+f"{i}.jpg")
                img.save(dosya_yolu, format='JPEG')
        except NoSuchElementException:
            pass
    time.sleep(3)
def freepik(yemek):
    options = ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument("--no-sandbox")
    options.add_experimental_option("useAutomationExtension", False)
    options.add_experimental_option("excludeSwitches", ["enable-automation"])

    driver = webdriver.Chrome(options=options)

    url = ("https://www.freepik.com/search?format=search&query={s}&type=photo")

    driver.get(url.format(s=yemek))
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight/5);")
    time.sleep(1)
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight/3);")
    time.sleep(1)
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight/2);")
    time.sleep(1)
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight/1.5);")
    time.sleep(1)
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight/1.2);")
    time.sleep(1)
    
    imgResults = driver.find_elements(By.XPATH,"//*[@id='main']/div[3]/div/div[2]/section/figure")
    try:
        os.mkdir(yemek.replace(" ","."))
    except FileExistsError:
        pass
    
    for i in range(len(imgResults)):
        try:
            imgResults = driver.find_element(By.XPATH, "/html/body/main/div[3]/div/div[2]/section/figure["+str(i)+"]/div/a/img")
            src = imgResults.get_attribute('src')
            if src is None:
                pass
            else:
                img = Image.open(requests.get(src, stream=True).raw).convert('RGB')
                dosya_yolu = os.path.join(yemek.replace(" ","."),yemek.replace(" ",".")+f"{i}.jpg")
                img.save(dosya_yolu, format='JPEG')
        except NoSuchElementException:
            pass
def alamy(yemek):
    options = ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument("--no-sandbox")
    options.add_experimental_option("useAutomationExtension", False)
    options.add_experimental_option("excludeSwitches", ["enable-automation"])

    driver = webdriver.Chrome(options=options)

    url = ("https://www.alamy.com/stock-photo/{s}.html")

    driver.get(url.format(s=yemek))
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight/5);")
    time.sleep(1)
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight/3);")
    time.sleep(1)
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight/2);")
    time.sleep(1)
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight/1.5);")
    time.sleep(1)
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight/1.2);")
    time.sleep(1)
    imgResults = driver.find_elements(By.XPATH,"//*[@id='__next']/div/div[6]/div/div[3]/div[1]/div/div/div[1]/div")
    try:
        os.mkdir(yemek.replace(" ","."))
    except FileExistsError:
        pass
    
    for i in range(len(imgResults)):
        try:
            imgResults = driver.find_element(By.XPATH, "//*[@id='__next']/div/div[6]/div/div[3]/div[1]/div/div/div[1]/div["+str(i)+"]/img")
            src = imgResults.get_attribute('src')
            if src is None:
                pass
            else:
                img = Image.open(requests.get(src, stream=True).raw).convert('RGB')
                dosya_yolu = os.path.join(yemek.replace(" ","."),yemek.replace(" ",".")+f"{i}.jpg")
                img.save(dosya_yolu, format='JPEG')
        except NoSuchElementException:
            pass
def onetwothreerf(yemek):
    options = ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument("--no-sandbox")
    options.add_experimental_option("useAutomationExtension", False)
    options.add_experimental_option("excludeSwitches", ["enable-automation"])

    driver = webdriver.Chrome(options=options)

    url = ("https://www.123rf.com/stock-photo/{s}.html")

    driver.get(url.format(s=yemek))
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight/5);")
    time.sleep(1)
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight/3);")
    time.sleep(1)
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight/2);")
    time.sleep(1)
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight/1.5);")
    time.sleep(1)
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight/1.2);")
    time.sleep(1)
    imgResults = driver.find_elements(By.XPATH,"/html/body/div/div[2]/div[5]/div[1]/div/div/div")
    try:
        os.mkdir(yemek.replace(" ","."))
    except FileExistsError:
        pass
    
    for i in range(len(imgResults)):
        try:
            imgResults = driver.find_element(By.XPATH, "/html/body/div/div[2]/div[5]/div[1]/div/div/div["+str(i)+"]/div[1]/a/img")
            src = imgResults.get_attribute('src')
            if src is None:
                pass
            else:
                
                img = Image.open(requests.get(src, stream=True).raw).convert('RGB')
                dosya_yolu = os.path.join(yemek.replace(" ","."),yemek.replace(" ",".")+f"{i}.jpg")
                img.save(dosya_yolu, format='JPEG')
        except NoSuchElementException:
            pass
with open ('deneme.txt','r') as dosya:
 for line in dosya.read().splitlines():
    yemekler.append(line)
    
for i in yemekler:
    shutterstock(i)
