from selenium import webdriver

driver = webdriver.Chrome('/Users/jssvs/Downloads/chromedriver')
driver.implicitly_wait(3)

driver.get('https://google.com')

#Instagram Login
