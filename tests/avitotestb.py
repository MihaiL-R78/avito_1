import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()
browser.get('https://www.avito.ru/avito-care/eco-impact')

wait = WebDriverWait(browser, 20)  # Увеличим время ожидания до 20 секунд

# Ваши данные для входа
login_text = "123"
password_text = "123"

# Находим элементы для ввода логина и пароля, вводим данные и нажимаем кнопку "Войти"
login_input = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div[3]/div/div/a')))
login_input.click()

login = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[4]/div/div/div/div/div/div/div/div[1]/form/div/div[1]/label/div/div/input')))
login.send_keys(login_text)

password = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[4]/div/div/div/div/div/div/div/div[1]/form/div/label/div/div/input')))
password.send_keys(password_text)

login_button = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[4]/div/div/div/div/div/div/div/div[1]/form/button/span')))
login_button.click()

time.sleep(20)  # Пауза в 1 секунду

# Ждем загрузки страницы после входа
water = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div[8]/div/div/div/div/div[3]/div/div[2]/div[4]')))
carbon_dioxide = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div[8]/div/div/div/div/div[3]/div/div[2]/div[2]')))
electricity = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div[8]/div/div/div/div/div[3]/div/div[2]/div[6]')))

# Создаем скриншоты
water.screenshot(r"C:\py.projects\autotestsAvito\output\2_water.png")
carbon_dioxide.screenshot(r"C:\py.projects\autotestsAvito\output\2_co2.png")
electricity.screenshot(r"C:\py.projects\autotestsAvito\output\2_electricity.png")

browser.quit()