from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

service = Service(executable_path="chromedriver.exe")
driver= webdriver.Chrome(service=service)

page = "https://universalis.app/market/"
pageNumber = "44141"

for i in range(6):

    url = page + pageNumber

    driver.get(url)

    if (pageNumber == "44141"):
        WebDriverWait(driver, 5).until (
            EC.presence_of_all_elements_located((By.CLASS_NAME, "servers"))
        )

        selectServer = driver.find_element(By.CLASS_NAME, "servers").click()

        WebDriverWait(driver, 5).until (
            EC.presence_of_all_elements_located((By.XPATH, '//*[@value="Siren"]'))
        )

        selectServer = driver.find_element(By.XPATH, '//*[@value="Siren"]').click()
        selectServer = driver.find_element(By.CLASS_NAME, "btn-green").click()

    getPrice = driver.find_elements(By.CLASS_NAME, "price-current")

    priceList = []
    for i in range(len(getPrice)):
        if (getPrice[i].text != ""):
            priceList.append(getPrice[i].text)

    notLess = 0
    total = 0
    counter = 0
    for i in range(len(priceList)):
        if "," in priceList[i]:
            priceList[i] = priceList[i].replace(",", "")
        if (int(priceList[i]) >= notLess):
            notLess = int(priceList[i])
            total += int(priceList[i])
            counter += 1

    getName = driver.find_element(By.CLASS_NAME, "rarity-1")

    print(getName.text.replace("710 ", "") + ":")
    print(total/counter)


    pageNumber = str(int(pageNumber) + 1)
    print("")

time.sleep(1000)

driver.quit()