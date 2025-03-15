from LocalStorage import LocalStorage
import pickle
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service
from selenium import webdriver

driver = webdriver.Firefox()
storage = LocalStorage(driver)

driver.get('https://vk.com/')
vk_phone = input('Enter phone number: ')


def save_data():
    with open(f"{vk_phone}_data", 'wb') as file:
        pickle.dump(storage.items(), file)


def load_data():
    with open(f"{vk_phone}_data", 'rb') as file:
        dataset = pickle.load(file)
        for key, value in dataset.items():
            storage.set(key, value)
