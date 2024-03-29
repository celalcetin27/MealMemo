import time

from selenium import  webdriver
from selenium.webdriver.common.by import By
import requests
import io

from PIL import Image
import time


wd = webdriver.Edge(r'C:\\Users\\celal\\OneDrive\\Masaüstü\\scraping\\msedgedriver.exe')

def get_images_from_google(wd,delay,max_images):
    def scroll_down(wd):
        wd.execute_script("window.scrollTo(0 , document.body.scrollHeight);")
        time.sleep(delay)

    url = "https://www.google.com/search?q=pizza&sca_esv=592593278&tbm=isch&sxsrf=AM9HkKnDIZRL6kUmj8dF-BLGQ-GCHPhZEg:1703100082323&source=lnms&sa=X&ved=2ahUKEwjdr7Gb3p6DAxW4g_0HHYnOCTgQ_AUoAnoECAMQBA&biw=2133&bih=1050&dpr=0.9"
    wd.get(url)

    image_urls = set()
    skips =0
    while len(image_urls) < max_images:
        scroll_down(wd)

        thumbnails = wd.find_elements(By.CLASS_NAME , "Q4LuWd")

        for img in thumbnails[len(image_urls) + skips:max_images]:
            try:
                img.click()
                time.sleep(delay)

            except:
                continue

            images = wd.find_elements(By.CLASS_NAME, "iPVvYb")

            for image in images:
                if image.get_attribute("src") in image_urls:
                    max_images +=1
                    skips +=1
                    break
                if image.get_attribute('src') and 'http' in image.get_attribute('src'):
                    image_urls.add(image.get_attribute('src'))
                    print(f"Found {len(image_urls)}")


    return image_urls


def download_image(download_path , url  , file_name):
    try:
        image_content = requests.get(url).content
        image_file = io.BytesIO(image_content)
        image = Image.open(image_file)
        file_path = download_path + file_name

        with open(file_path , "wb") as f:
            image.save(f , "JPEG")


        print("Succes")
    except Exception as e:
        print("Faıled - " + e)


urls = get_images_from_google(wd, 1, 15)

for i, url in enumerate(urls):
	download_image("pizza/", url, str(i) + ".jpg")

wd.quit()