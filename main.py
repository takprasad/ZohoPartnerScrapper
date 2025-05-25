from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import re
import json
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
chrome_options = Options()
chrome_options.add_argument("--headless=new") 
driver = webdriver.Chrome(options = chrome_options)
data = []
countries = [
    
    "Poland", "Portugal", "Puerto Rico", "Qatar", "Romania", "Russia",
    "San Marino", "Saudi Arabia", "Senegal", "Serbia", "Singapore", "Slovakia", "Slovenia",
    "South Africa", "Spain", "Sri Lanka", "Suriname", "Sweden", "Switzerland", "Taiwan",
    "Tanzania", "Thailand", "Tunisia", "Turkey", "Ukraine", "United Arab Emirates", "United Kingdom",
    "United States", "Uruguay", "Vietnam", "Yemen", "Zimbabwe"
]

for country in countries:
    driver.get('https://www.zoho.com/partners/find-partner.html')
    time.sleep(5)
    search = driver.find_element(By.XPATH,'//*[@id="search-partner"]').send_keys(country)
    button = driver.find_element(By.XPATH,'/html/body/main/div/div/div/div/div/div[1]/div/div/div[2]/ul/li[2]')
    button.click()
    try:
        links = WebDriverWait(driver, 15).until(
            EC.presence_of_all_elements_located((By.XPATH, '/html/body/main/div/div/div[2]/div/div[4]/div[2]/div[2]/div[4]/div[/*]/ul/li[/*]'))
        )
    except :
        print("\n")
    for i in range(len(links)):
        links[i].click()
        try:
            company_name_element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '/html/body/main/div/div/div[2]/div/div[2]/div[2]/div[2]/div[2]/h2'))
            )
            company_name = company_name_element.text
        except :
            print("\n")
            company_name = None
        try:
            partner_name = driver.find_element(By.XPATH, '//h3[@class="pp-partner-name"]').text
        except:
            partner_name = None

        try:
            email = driver.find_element(By.XPATH, '//span[@class="prof-email"]/a').get_attribute('href')
        except:
            email = None

        try:
            address = driver.find_element(By.XPATH, '//span[@class="prof-address"]').text
        except:
            address = None

        try:
            linked = driver.find_element(By.XPATH, '/html/body/main/div/div/div[2]/div/div[2]/div[2]/div[1]/div/div[2]/div[1]/div/ul/li/a').get_attribute('href')
        except:
            linked = None

        try:
            phone = driver.find_element(By.XPATH, '//span[@class="prof-phone"]').text
        except:
            phone = None

        try:
            website = driver.find_element(By.XPATH, '//span[@class="prof-web"]/a').get_attribute('href')
        except:
            website = None

        try:
            head = driver.find_element(By.XPATH, '//div[@class="branches-location head-office"]/ul/li').text
        except:
            head = None

        
        dic = {'Country':country,'Company_name':company_name,'Partner_name':partner_name,'Phone':phone,'Email':email,'Website':website,'LinkedIn':linked,'Head_office':head}
        print(dic)
        data.append(dic)
        back = driver.find_element(By.XPATH,'/html/body/main/div/div/div[2]/div/div[2]/div[1]/div[1]/a')
        back.click()
        try:
            links = WebDriverWait(driver, 15).until(
                EC.presence_of_all_elements_located((By.XPATH, '/html/body/main/div/div/div[2]/div/div[4]/div[2]/div[2]/div[4]/div[/*]/ul/li[/*]'))
            )
        except :
            print("\n")
df =pd.DataFrame(data).to_csv('lexyl.csv')        
