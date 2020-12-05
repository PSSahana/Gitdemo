from selenium import webdriver


driver = webdriver.Chrome(executable_path="C:/Program Files/Python37/Drivers/chromedriver.exe")
driver.get("https://office365onboarding.fresco.me/")

driver.find_element_by_xpath("//a[@href ='/support']").click()