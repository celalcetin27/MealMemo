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
x=0
def google(yemek,sayı):
    xax=0
    yemek = yemek.lower()
    options = ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument("--no-sandbox")
    options.add_experimental_option("useAutomationExtension", False)
    options.add_experimental_option("excludeSwitches", ["enable-automation"])

    driver = webdriver.Chrome(options=options)

    url = ("https://www.google.com/search?q={s}&tbm=isch&tbs=sur%3Afc&hl=en&ved=0CAIQpwVqFwoTCKCa1c6s4-oCFQAAAAAdAAAAABAC&biw=1251&bih=568")

    driver.get(url.format(s=yemek))

    for x in range(5):
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
        time.sleep(1)

    imgResults = driver.find_elements(By.XPATH,"//img[contains(@class,'Q4LuWd')]")
    src = [img.get_attribute('src') for img in imgResults]
    try:
        os.mkdir("Google_"+yemek.replace(" ","."))
    except FileExistsError:
        pass
    
    for i in range(len(src)):
    # check if the image is None
        if xax==sayı:
            break
        else:
            if src[i] is None:
                pass
            else:
                # if it's base64 images
                if src[i].startswith('data'):
                    pass  

                else:
                    xax+=1
                    img = Image.open(requests.get(src[i], stream=True).raw).convert('RGB')
                    dosya_yolu = os.path.join("Google_"+yemek.replace(" ","."),yemek.replace(" ",".")+f"{xax}.jpg")
                    img.save(dosya_yolu, format='JPEG')        
def Pikwizard(yemek, sayı):
    yemek = yemek.lower()
    options = ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument("--no-sandbox")
    options.add_experimental_option("useAutomationExtension", False)
    options.add_experimental_option("excludeSwitches", ["enable-automation"])

    driver = webdriver.Chrome(options=options)

    url = ("https://pikwizard.com/s/photo/{s}/")

    driver.get(url.format(s=yemek))

    try:
        os.mkdir("Pikwizard_"+yemek.replace(" ","."))
    except FileExistsError:
        pass

    for x in range(4):
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
        time.sleep(1)

    time.sleep(2) 
    x=0
    i=0
    while True:
        i+=1
        if x==sayı:
            break
        else:
            salam_path = f"/html/body/div[2]/div/div/div[{i+1}]"
            try:
                salam_element = driver.find_element(By.XPATH, salam_path)
                img_element = salam_element.find_element(By.TAG_NAME, 'img')
                src = img_element.get_attribute('src')

                if src is not None:
                    x+=1
                    img = Image.open(requests.get(src, stream=True).raw).convert('RGB')
                    dosya_yolu = os.path.join(f"Pikwizard_{yemek.replace(' ', '.')}", f"{yemek.replace(' ', '.')}{x}.jpg")
                    img.save(dosya_yolu, format='JPEG')
            except NoSuchElementException:
                pass
def pexels(yemek,sayı):
    yemek = yemek.lower()
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
        time.sleep(1)
    foto1=driver.find_elements(By.XPATH,"//*[@id='-']/div[1]/div/div[1]/div")
    foto2=driver.find_elements(By.XPATH,"//*[@id='-']/div[1]/div/div[2]/div")
    foto3=driver.find_elements(By.XPATH,"//*[@id='-']/div[1]/div/div[3]/div")
    try:
        os.mkdir("Pexels_"+yemek.replace(" ","."))
    except FileExistsError:
        pass
    for i in range(len(foto1)):
        if i==(sayı+1):
            break
        else:

            try:
                imgResults = driver.find_element(By.XPATH, "//*[@id='-']/div[1]/div/div[1]/div["+str(i)+"]/article/a/img")
                src = imgResults.get_attribute('src')
                if src is None:
                    pass
                else:
                    img = Image.open(requests.get(src, stream=True).raw).convert('RGB')
                    dosya_yolu = os.path.join("Pexels_"+yemek.replace(" ","."),yemek.replace(" ",".")+f"{i}.jpg")
                    img.save(dosya_yolu, format='JPEG')
            except NoSuchElementException:
                pass
def shutterstock(yemek,sayı):
    yemek = yemek.lower()
    x=0
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
    imgResults = driver.find_elements(By.XPATH,"//*[@id='__next']/div[3]/div/div/div[1]/div/div[6]/div[1]/div[2]/div")
    time.sleep(3)
    try:
        os.mkdir("Shutterstock_"+yemek.replace(" ","."))
    except FileExistsError:
        pass
    
    for i in range(len(imgResults)):
        if x==sayı:
            break
        else:
            try:
                imgResults = driver.find_element(By.XPATH, "//*[@id='__next']/div[3]/div/div/div[1]/div/div[6]/div[1]/div[2]/div["+str(i)+"]/div[2]/div/picture/img")
                src = imgResults.get_attribute('src')
                if src is None:
                    pass
                else:
                    x+=1
                    img = Image.open(requests.get(src, stream=True).raw).convert('RGB')
                    dosya_yolu = os.path.join("Shutterstock_"+yemek.replace(" ","."),yemek.replace(" ",".")+f"{x}.jpg")
                    img.save(dosya_yolu, format='JPEG')
            except NoSuchElementException:
                pass
def freepik(yemek,sayı):
    yemek = yemek.lower()
    options = ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument("--no-sandbox")
    options.add_experimental_option("useAutomationExtension", False)
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    driver = webdriver.Chrome(options=options)

    url = ("https://www.freepik.com/search?format=search&query={s}&type=photo")
    time.sleep(1)
    driver.get(url.format(s=yemek))
    time.sleep(1)
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
        os.mkdir("Freepik_"+yemek.replace(" ","."))
    except FileExistsError:
        pass
    
   
    for i in range(len(imgResults)):
        if sayı+1==i:
            break
        else:
            try:
                imgResults = driver.find_element(By.XPATH, "/html/body/main/div[3]/div/div[2]/section/figure["+str(i)+"]/div/a/img")
                src = imgResults.get_attribute('src')
                if src is None:
                    pass
                else:
                    img = Image.open(requests.get(src, stream=True).raw).convert('RGB')
                    dosya_yolu = os.path.join("Freepik_"+yemek.replace(" ","."),yemek.replace(" ",".")+f"{i}.jpg")
                    img.save(dosya_yolu, format='JPEG')
            except NoSuchElementException:
                pass
def alamy(yemek,sayı):
    yemek = yemek.lower()
    xax=0
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
        os.mkdir("Alamy_"+yemek.replace(" ","."))
    except FileExistsError:
        pass
    for i in range(len(imgResults)):
        if sayı==xax:
            break
        else:
            try:
                imgResults = driver.find_element(By.XPATH, "//*[@id='__next']/div/div[6]/div/div[3]/div[1]/div/div/div[1]/div["+str(i)+"]/img")
                src = imgResults.get_attribute('src')
                if src is None:
                    pass
                else:
                    xax+=1
                    img = Image.open(requests.get(src, stream=True).raw).convert('RGB')
                    dosya_yolu = os.path.join("Alamy_"+yemek.replace(" ","."),yemek.replace(" ",".")+f"{xax}.jpg")
                    img.save(dosya_yolu, format='JPEG')
            except NoSuchElementException:
                pass
def onetwothreerf(yemek,sayı):
    yemek = yemek.lower()
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
        os.mkdir("123RF_"+yemek.replace(" ","."))
    except FileExistsError:
        pass
    
    for i in range(len(imgResults)):
        if sayı+2==i:
            break
        else:
            try:
                imgResults = driver.find_element(By.XPATH, "/html/body/div/div[2]/div[5]/div[1]/div/div/div["+str(i)+"]/div[1]/a/img")
                src = imgResults.get_attribute('src')
                if src is None:
                    pass
                else:
                
                    img = Image.open(requests.get(src, stream=True).raw).convert('RGB')
                    dosya_yolu = os.path.join("123RF_"+yemek.replace(" ","."),yemek.replace(" ",".")+f"{i-1}.jpg")
                    img.save(dosya_yolu, format='JPEG')
            except NoSuchElementException:
                pass
