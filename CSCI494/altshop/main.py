from selenium import webdriver
import os
import pandas as pd
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

df = pd.read_csv(r'C:\Users\Ben Farrell\Downloads\althshoptest - Sheet1 (1).csv')

search = str(input("Enter a product to search for: "))

browser = webdriver.Chrome(
    executable_path=os.path.abspath("C:/Users/Ben Farrell/Desktop/chromedriver.exe"))


for url in df['search_url']:
    browser.get(url.replace('soap', search))
    sleep(2)
    try:
        name = browser.find_element_by_xpath(df.loc[df['search_url'] == url, 'name_xpath'].values[0].replace('LOOP', '1'))
        price = browser.find_element_by_xpath(df.loc[df['search_url'] == url, 'price_xpath'].values[0].replace('LOOP', '1'))
        img = browser.find_element_by_xpath(df.loc[df['search_url'] == url, 'image_xpath'].values[0].replace('LOOP', '1'))
        # have to download images or use database
        print(name.text, price.text)
    except Exception:
        print("Product not available from " + str(url))





