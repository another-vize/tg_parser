import time
import os
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from vk_kiss import vk_phone, load_data, save_data, driver



def wait_until(byy, selector):
     try:        
          gry = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((byy, selector))) 
          gry.click()          
     except:
          pass        
     

def finder(byy, selector):
     if byy == By.XPATH:
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



# if os.path.exists(f"{vk_phone}_data"):
#      load_data()
#      time.sleep(3)
#      driver.refresh()
     
     
# else:
     
wait_until(By.XPATH, "/html/body/div[14]/div/div/div/div[3]/div/div/div[2]/div[1]/div/div/section/div/div/div/div/div/div[2]/div/button[1]/span")
p = finder(By.XPATH, "/html/body/div[14]/div/div/div/div[3]/div/div/div[2]/div[1]/div/div/section/div/div/div/div/div/form/div[1]/div[3]/span/div/div[2]/input")
p.send_keys(vk_phone)
p.send_keys(Keys.ENTER)

code = input("Enter the code sent to your phone:")
cod = finder(By.XPATH, '/html/body/div[1]/div/div/div/div/div[1]/div[1]/div/div/div/div/form/div[2]/div')
cod.send_keys(code)
cod.send_keys(Keys.ENTER)
     
    #  tg_password = input("Enter your password: ")
    #  pass1 = finder(By.ID, 'sign-in-password')
    #  pass1.send_keys(tg_password)
    #  pass1.send_keys(Keys.ENTER)

time.sleep(5)
#save_data()


channel = input("Enter parse channel @:")

chan = finder(By.XPATH, '//*[@id="telegram-search-input"]')
check(chan)
finder(By.XPATH, "/html/body/div[2]/div/div[1]/div/div[2]/div[2]/div/div[1]/div[2]").click()

chan.send_keys(channel)
chan.send_keys(Keys.ENTER)


finder(By.XPATH, "/html/body/div[2]/div/div[1]/div/div[2]/div[2]/div/div[2]/div/div[1]/div[1]/div/div/div[2]").click()

print(finder(By.CLASS_NAME, 'text-content clearfix with-meta'))