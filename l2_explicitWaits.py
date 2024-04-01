from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

browser = webdriver.Chrome()
browser.implicitly_wait(5)
browser.get("https://suninjuly.github.io/explicit_wait2.html")

# говорим Selenium проверять в течение 12 секунд, пока цена не упадет
price_element = WebDriverWait(browser, 12).until(
    EC.text_to_be_present_in_element((By.XPATH, "//*[@id='price']"), '100')
)
button = browser.find_element(By.XPATH, "//*[@id='book']")
button.click()

x_element = browser.find_element(By.XPATH, "//*[@id='input_value']").text
x = int(x_element)

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

answer = calc(x)

input1 = browser.find_element(By.XPATH, "//*[@id='answer']")
input1.send_keys(answer)

button = browser.find_element(By.XPATH, "//*[@id='solve']")
button.click()

time.sleep(3)
