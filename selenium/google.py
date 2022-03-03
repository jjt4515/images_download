from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import urllib.request
from selenium.webdriver.common.by import By
import os 

while True:

    driver = webdriver.Chrome()
    driver.get("https://www.google.co.kr/imghp?hl=ko&tab=ri&ogbl")

    search = driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input")
    search.clear()
    print("****     검색어를 입력하세요 ex)OOO 사복    ****")
    print("***        'X'를 입력하시면 중지됩니다.      ***")
    search_name = input()
    if search_name == "X":
        break
    search.send_keys(search_name)
    search.send_keys(Keys.RETURN)
    driver.implicitly_wait(3)
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')

    images = driver.find_elements(By.CSS_SELECTOR, "img.rg_i.Q4LuWd")
    img_url = []
    for image in images:
        try:
            url = image.get_attribute('src')
            img_url.append(url)
        except:
            pass     

    outpath = "./" + search_name
    if not os.path.isdir(outpath) :
        os.mkdir(outpath)
    try:
        for index, img in enumerate(img_url) :
            outfile = "/" + str(index) + ".jpg"
            urllib.request.urlretrieve(img, outpath + outfile)
    except:
        pass

driver.close()
