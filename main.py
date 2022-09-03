from selenium.webdriver.firefox.options import Options
from selenium import webdriver
import time
import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

phone = "89250000000"
pwd = "Password"

options = Options()
options.add_argument("--headless")
driver = webdriver.Firefox(executable_path="geckodriver.exe", options=options)
driver.get('https://hh.ru/account/login')

logwithpass = driver.find_element_by_xpath('//*[@id="HH-React-Root"]/div/div[3]/div[1]/div/div/div/div/div/div[1]/div[1]/div[1]/div[2]/div/div/form/div[4]/button[2]')
logwithpass.click()

username = driver.find_element_by_xpath("/html/body/div[5]/div/div[3]/div[1]/div/div/div/div/div/div[1]/div[1]/div[1]/div[2]/div/form/div[1]/fieldset/input")
password = driver.find_element_by_xpath("/html/body/div[5]/div/div[3]/div[1]/div/div/div/div/div/div[1]/div[1]/div[1]/div[2]/div/form/div[2]/fieldset/input")
username.send_keys(phone)
password.send_keys(pwd)
submit_button = driver.find_element_by_xpath("/html/body/div[5]/div/div[3]/div[1]/div/div/div/div/div/div[1]/div[1]/div[1]/div[2]/div/form/div[4]/div/button[1]")

os.system('cls')
print("Логин...")

submit_button.click()
time.sleep(2)

driver.execute_script("window.stop();")
driver.get('https://hh.ru/applicant/resumes')
time.sleep(2)
#refresh_button = driver.find_element_by_xpath('/html/body/div[5]/div/div[3]/div[1]/div/div/div[1]/div[3]/div[2]/div/div[6]/div/div/div/div[1]/span/button')
wait = WebDriverWait(driver, 10)
delay = 600

os.system('cls')
print("Поднятие.")

while 1==1:
    try:
        myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#HH-React-Root > div > div.HH-MainContent.HH-Supernova-MainContent > div.main-content > div > div > div.bloko-column.bloko-column_container.bloko-column_xs-4.bloko-column_m-8.bloko-column_l-11 > div.bloko-column.bloko-column_xs-4.bloko-column_s-8.bloko-column_m-8.bloko-column_l-11 > div.bloko-gap.bloko-gap_top.bloko-gap_bottom > div > div.bloko-gap.bloko-gap_top > div > div > div > div:nth-child(1) > span > button")))
        print("Появилось, жмаю!")
        driver.find_element_by_xpath('/html/body/div[5]/div/div[3]/div[1]/div/div/div[1]/div[3]/div[2]/div/div[6]/div/div/div/div[1]/span/button').click
        driver.refresh()
    except TimeoutException:
        print("Ожидаем.")

    #wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.applicant-resumes-actions-content > div:nth-child(1) > div:nth-child(1) > span:nth-child(1) > button:nth-child(1)'))).click()
    #WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".applicant-resumes-actions-content > div:nth-child(1) > div:nth-child(1) > span:nth-child(1) > button:nth-child(1)"))).click()
    #time.sleep(1800)

driver.close()
