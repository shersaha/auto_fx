from selenium import webdriver
from time import sleep


path = "/home/nerd/Downloads/chromedriver"
driver = webdriver.Chrome(executable_path=path)

driver.get('https://supplier.meesho.com/panel/v2/new/login?distinct_id=')
driver.find_element_by_id('email').send_keys('your_email')
driver.find_element_by_id('password').send_keys('pass_word')
driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/form/div[3]/button').click()
driver.get('https://supplier.meesho.com/panel/v2/new/z81oq/catalogs')
driver.quit()