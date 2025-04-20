from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
import time


def setup_driver():
    firefox_options = Options()
    firefox_options.add_argument("--headless")  # Фоновый режим
    driver = webdriver.Firefox(options=firefox_options)
    return driver


def get_paragraphs(driver):
    paragraphs = driver.find_elements(By.CSS_SELECTOR, 'div.mw-parser-output > p')
    return [p.text for p in paragraphs if p.text.strip()]


def get_links(driver):
    links = driver.find_elements(By.CSS_SELECTOR, 'div.mw-parser-output a[href^="/wiki/"]')
    return {link.text: link.get_attribute('href') for link in links if link.text.strip()}


def browse_article(driver, current_url):
    driver.get(current_url)
    while True:
        print("\nТекущая статья:", driver.title)
        print("\nВыберите действие:")
        print("1. Листать параграфы текущей статьи")
        print("2. Перейти на одну из связанных страниц")
        print("3. Выйти из программы")

        choice = input("Ваш выбор (1/2/3): ").strip()

        if choice == '1':
            paragraphs = get_paragraphs(driver)
            for i, p in enumerate(paragraphs, 1):
                print(f"\nПараграф {i}:")
                print(p)
                if i % 3 == 0:  # Показываем по 3 параграфа за раз
                    cont = input("\nПродолжить чтение? (y/n): ").lower()
                    if cont != 'y':
                        break
        elif choice == '2':
            links = get_links(driver)
            if not links:
                print("Нет доступных ссылок в этой статье.")
                continue

            print("\nДоступные ссылки:")
            link_items = list(links.items())
            for i, (text, _) in enumerate(link_items[:10], 1):  # Показываем первые 10 ссылок
                print(f"{i}. {text}")

            link_choice = input("\nВыберите номер ссылки (или 0 для отмены): ").strip()
            if link_choice == '0':
                continue

            try:
                link_num = int(link_choice) - 1
                if 0 <= link_num < len(link_items):
                    new_url = "https://ru.wikipedia.org" + link_items[link_num][1]
                    browse_article(driver, new_url)
                else:
                    print("Неверный номер ссылки.")
            except ValueError:
                print("Пожалуйста, введите число.")
        elif choice == '3':
            return
        else:
            print("Неверный ввод. Пожалуйста, выберите 1, 2 или 3.")


def main():
    driver = setup_driver()
    try:
        search_query = input("Введите ваш запрос для поиска в Википедии: ").strip()
        if not search_query:
            print("Запрос не может быть пустым.")
            return

        driver.get(f"https://ru.wikipedia.org/wiki/{search_query}")

        # Проверяем, есть ли статья
        if "Википедия:Поиск" in driver.title:
            print("Точной статьи не найдено. Перенаправление на страницу поиска.")
        elif "Wikipedia" in driver.title:
            print("Статья найдена.")

        browse_article(driver, driver.current_url)
    finally:
        driver.quit()
        print("Программа завершена.")


if __name__ == "__main__":
    main()