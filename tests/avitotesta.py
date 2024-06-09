from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import os

output_folder = r'C:\py.projects\autotestsAvito\output'
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

browser = webdriver.Chrome()
browser.get('https://www.avito.ru/avito-care/eco-impact')

wait = WebDriverWait(browser, 10)  # Используем явное ожидание до 10 секунд

# Чтение и обновление номера папки
folder_number_file = "folder_number.txt"

current_folder_number = 1
if os.path.exists(folder_number_file):
    with open(folder_number_file, "r") as file:
        current_folder_number = int(file.read().strip())

def save_screenshot(element, filename_base, testcase_number, screenshot_number):
    testcase_folder = os.path.join(output_folder, f'Test_{testcase_number}_{current_folder_number}')
    if not os.path.exists(testcase_folder):
        os.makedirs(testcase_folder)
        
    filename = f'{filename_base}_{screenshot_number}.png'
    filepath = os.path.join(testcase_folder, filename)
    element.screenshot(filepath)
    print(f"Скриншот сохранен в: {filepath}")

def test_first_case(testcase_number):
    try:
        water = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='desktop-impact-item-eeQO3' and contains(., 'было сохранено')]")))
        save_screenshot(water, 'water', testcase_number, 1)
    except:
        print("Элемент 'water' не найден на странице.")
    
    try:
        carbon_dioxide = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='desktop-impact-item-eeQO3' and contains(., 'не попало в атмосферу')]")))
        save_screenshot(carbon_dioxide, 'carbon_dioxide', testcase_number, 1)
    except:
        print("Элемент 'carbon_dioxide' не найден на странице.")
    
    try:
        electricity = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='desktop-impact-item-eeQO3' and contains(., 'было сэкономлено')]")))
        save_screenshot(electricity, 'electricity', testcase_number, 1)
    except:
        print("Элемент 'electricity' не найден на странице.")

    sleep(5)  # Добавим небольшую задержку

# Запускаем тест и присваиваем каждой новой папке увеличенный номер
test_first_case(1)  # Например, запускаем первый тест-кейс

# Увеличиваем номер папки и обновляем файл
current_folder_number += 1
with open(folder_number_file, "w") as file:
    file.write(str(current_folder_number))

# Закрываем браузер после выполнения теста
browser.quit()