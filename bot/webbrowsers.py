import os
from selenium import webdriver
from chatbot import *
def open_webrowser():
    driver=webdriver.Chrome("chromedriver.exe")
    driver.maximize_window()
    data = driver.get("http://www.google.com")

    

