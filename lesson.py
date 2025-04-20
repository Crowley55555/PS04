import time  # модуль для работы со временем (паузы)
import random
from selenium import webdriver  # основной модуль Selenium для управления браузером
from selenium.webdriver import Keys  # модуль для эмуляции нажатия клавиш клавиатуры
from selenium.webdriver.common.by import By  # модуль для поиска элементов на странице

# browser.get("https://ru.tradingview.com/chart/")
# browser.save_screenshot("trading.png")
# time.sleep(5)
# browser.get("https://ru.wikipedia.org/wiki/Selenium")
# browser.save_screenshot("wiki.png")
# time.sleep(3)
# browser.refresh()
# browser.quit()
# ---------------------------------------------------------------------------------------------
# # Создаем экземпляр браузера Firefox
# browser = webdriver.Firefox()
#
# # Открываем главную страницу Википедии
# browser.get("https://ru.wikipedia.org/wiki/%D0%97%D0%B0%D0%B3%D0%BB%D0%B0%D0%B2%D0%BD%D0%B0%D1%8F_%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0")
#
# # Проверяем, что заголовок страницы содержит слово "Википедия"
# assert "Википедия" in browser.title
#
# # Ждем 5 секунд, чтобы страница полностью загрузилась
# time.sleep(5)
#
# # Находим поле поиска по его ID
# search_box = browser.find_element(By.ID, "searchInput")
#
# # Вводим текст "солнечная система" в поле поиска
# search_box.send_keys("солнечная система")
#
# # Эмулируем нажатие клавиши Enter (RETURN)
# search_box.send_keys(Keys.RETURN)
#
# # Ждем 5 секунд для загрузки результатов поиска
# time.sleep(5)
#
# # Находим ссылку с текстом "Солнечная система" среди результатов поиска
# a = browser.find_element(By.LINK_TEXT, "Солнечная система")
#
# # Кликаем по найденной ссылке
# a.click()

# ---------------------------------------------

# Создаем экземпляр браузера Firefox
browser = webdriver.Firefox()
# Открываем главную страницу Википедии
browser.get("https://ru.wikipedia.org/wiki/%D0%A1%D0%BE%D0%BB%D0%BD%D0%B5%D1%87%D0%BD%D0%B0%D1%8F_%D1%81%D0%B8%D1%81%D1%82%D0%B5%D0%BC%D0%B0")

# paragraphs = browser.find_elements(By.TAG_NAME, "p")
#
# for paragraph in paragraphs:
#     print(paragraph.text)
#     input()
# ---------------------------------------
# Создаем пустой список для хранения "примечаний" (hatnotes)
hatnotes = []

# Ищем все элементы div на странице (возвращается список элементов)
for element in browser.find_elements(By.TAG_NAME, 'div'):
    # Получаем значение атрибута "class" у текущего элемента div
    cl = element.get_attribute("class")

    # Проверяем, совпадает ли класс элемента с искомым классом примечания
    if cl == "hatnote navigation-not-searchable ts-main":
        # Если совпадает - добавляем элемент в наш список
        hatnotes.append(element)

# Выводим список найденных примечаний (для отладки)
print(hatnotes)

# Выбираем случайное примечание из списка (требуется import random в начале файла)
hatnotes = random.choice(hatnotes)

# В выбранном примечании находим тег <a> (ссылку) и получаем её атрибут href (адрес)
link = hatnotes.find_element(By.TAG_NAME, "a").get_attribute("href")

# Переходим по полученной ссылке
browser.get(link)