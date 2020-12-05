from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome(executable_path="C:/Program Files/Python37/Drivers/chromedriver.exe")

driver.get("https://rahulshettyacademy.com/angularpractice")

driver.find_element_by_css_selector("a[href*='shop']").click()
products = driver.find_elements_by_xpath("//div[@class ='card h-100']")
print(products)

for product in products:
    print(product.find_element_by_xpath("div/h4/a").text)
    productName = product.find_element_by_xpath("div/h4/a").text
    if productName == "Blackberry":
        product.find_element_by_xpath("div/button").click()

driver.find_element_by_css_selector(".btn-primary").click()

Available = driver.find_element_by_css_selector("span.text-success").text

if Available == "In Stock":
    print("proceed further")
driver.find_element_by_xpath("//button[@class= 'btn btn-success']").click()
driver.find_element_by_id("country").send_keys('ind')

wait = WebDriverWait(driver, 7)
wait.until(EC.presence_of_element_located((By.LINK_TEXT, "India")))
driver.find_element_by_link_text("India").click()
driver.find_element_by_xpath("//div[@class= 'checkbox checkbox-primary']").click()
driver.find_element_by_css_selector("input[type='submit']").click()
print(driver.find_element_by_css_selector("div[class*='alert-success']").text)

success_text = driver.find_element_by_css_selector("div[class*='alert-success']").text
assert "Success! Thank you! " in success_text

driver.get_screenshot_as_file("screen.png")
