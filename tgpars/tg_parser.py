import time
import os
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from kiss import tg_phone, load_data, save_data, driver



def wait_until(byy, selector):
     try:        
          gry = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((byy, selector))) 
          gry.click()          
     except:
          pass        
     

def finder(byy, selector):
     if byy == By.ID or byy == By.XPATH:
          while True:
               try:
                     return driver.find_element(byy, selector)
               except:
                    pass
     else:
          while True:
               return driver.find_elements(byy, selector)

             
def check(chan):
     while True:
          try:
               chan.send_keys("channels")
               chan.clear()
               return
          except:
               pass



if os.path.exists(f"{tg_phone}_data"):
     load_data()
     time.sleep(3)
     driver.refresh()
     wait_until(By.XPATH, '/html/body/div[1]/div[2]/div/div/div[2]/div[2]/div/button')
     
     
else:
     
     wait_until(By.XPATH, "/html/body/div[2]/div/div/div/div/button[1]")
     p = finder(By.ID, "sign-in-phone-number")
     p.send_keys(tg_phone)
     p.send_keys(Keys.ENTER)

     code = input("Enter the code sent to your phone:")
     cod = finder(By.ID, 'sign-in-code')
     cod.send_keys(code)
     cod.send_keys(Keys.ENTER)
     
     tg_password = input("Enter your password: ")
     pass1 = finder(By.ID, 'sign-in-password')
     pass1.send_keys(tg_password)
     pass1.send_keys(Keys.ENTER)

     time.sleep(5)
     save_data()
     wait_until(By.XPATH, '/html/body/div[1]/div[2]/div/div/div[2]/div[2]/div/button')

channel = input("Enter parse channel @:")

chan = finder(By.XPATH, '//*[@id="telegram-search-input"]')
check(chan)
chan.send_keys(channel)
finder(By.XPATH, "/html/body/div[2]/div/div[1]/div/div[2]/div[2]/div/div[1]/div[2]").click()
time.sleep(2)
chan.send_keys(Keys.ENTER)

time.sleep(3)

finder(By.CLASS_NAME, "CommentButton")[0].click()
time.sleep(3)

file = open("shit.txt", "w", encoding="utf-8")
page_source = driver.page_source
soup = bs(page_source, 'html.parser')
comments = soup.select(".Message.message-list-item.first-in-group.allow-selection.last-in-group.shown.open")
for comment in comments:
     file.write(comment.text)
file.close()