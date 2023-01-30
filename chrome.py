from selenium import webdriver
import time
driver = webdriver.Chrome(executable_path="C:\webdriver\\chromedriver.exe")
driver.maximize_window()
driver.get("https://www.facebook.com/")

time.sleep(5)