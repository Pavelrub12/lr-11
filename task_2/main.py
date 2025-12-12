import requests
from bs4 import BeautifulSoup


print("Начинаем парсинг Quotes to Scrape")
print("-" * 50)
url = "https://quotes.toscrape.com/"
response = requests.get(url)
if response.status_code != 200:
    print(f"Ошибка: не удалось загрузить страницую/ Код ошибки: {responde.status_code}")

soup = BeautifulSoup(response.text, 'html.parser')
repos = soup.find_all('div', class_ = "quote")

if not repos:
    print("Не удалост найти репозитории на странице.")

print(f"Найдено репозиториев: {len(repos)}")
print('-' * 50)

for i, repo in enumerate(repos[:5], 1):
    main_text = repo.find('span', class_="text")
    if main_text:
        repo_text = main_text.get_text(strip = True)
    else:
        repo_text = "Неизвестно"

    author_name = repo.find('small', class_ = "author")
    if author_name:
        repo_author = author_name.get_text(strip = True)
    else:
        repo_author = "Неизвестно"

    print(f"{i}. Quote: {repo_text}; Author: {repo_author};")

print('-' * 50)
print("Парсинг завершён!")