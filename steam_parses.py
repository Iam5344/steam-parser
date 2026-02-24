from bs4 import BeautifulSoup
import requests
import pandas as pd
from telegram import Bot
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

while True:
 chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

 options = webdriver.ChromeOptions()
 driver = webdriver.Chrome(
     service=Service(ChromeDriverManager().install()),
     options=options
 )

 driver.get("https://store.steampowered.com/search/?maxprice=free&supportedlang=russian&specials=1&ndl=1")
 time.sleep(10)

 games = driver.find_elements(By.CSS_SELECTOR, ".search_result_row")

 found = False

 for game in games:
     try:
         name = game.find_element(By.CSS_SELECTOR, ".title").text
         discount = game.find_element(By.CSS_SELECTOR, ".discount_pct").text

         if discount == "-100%":
             found = True
             print(f"игра найдена {name}")

     except:
         continue

 driver.quit()


 if not found: 
     print("игра не найдена")

 time.sleep(300)
