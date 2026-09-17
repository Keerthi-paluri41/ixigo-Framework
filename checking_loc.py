from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://www.ixigo.com/")

wait = WebDriverWait(driver, 20)

from_location = wait.until(
    EC.presence_of_element_located(
        (By.XPATH, "//input")
    )
)

print("INPUT FOUND")
print("Tag:", from_location.tag_name)
print("Value:", from_location.get_attribute("value"))
print("Placeholder:", from_location.get_attribute("placeholder"))

driver.quit()