import requests
import json
from bs4 import BeautifulSoup

with open("data.json", "r", encoding='utf-8') as f:
    data = json.load(f)
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
    newRecord = {
        "id": i,
        'Quote': repo_text,
        'Author': repo_author,
    }
    data.append(newRecord)
    with open('data.json', 'w', encoding = 'utf-8') as file:
        json.dump(data, file, ensure_ascii = False)
print('-' * 50)
print("Парсинг завершён!")

html_content = '''<!DOCTYPE html>
<html>
<head>
    <title>Quotes Collection</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
            padding: 20px;
            margin: 0;
        }
        h1 {
            color: #333;
            text-align: center;
            margin-bottom: 30px;
        }
        table {
            width: 100%;
            border-collapse: collapse;
            background: white;
            box-shadow: 0 4px 12px rgba(0,0,0,0.1);
            border-radius: 8px;
            overflow: hidden;
        }
        th {
            background: #4a6fa5;
            color: white;
            padding: 15px;
            text-align: left;
        }
        td {
            padding: 12px 15px;
            border-bottom: 1px solid #ddd;
        }
        tr:hover {
            background-color: #f5f9ff;
        }
        tr:nth-child(even) {
            background-color: #f9f9f9;
        }
        .source-link {
            margin-top: 30px;
            text-align: center;
        }
        .source-link a {
            color: #4a6fa5;
            text-decoration: none;
            font-weight: bold;
        }
    </style>
</head>
<body>
    <h1>Коллекция цитат</h1>
    <table>
        <thead>
            <tr>
                <th>№</th>
                <th>Цитата</th>
                <th>Автор</th>
            </tr>
        </thead>
        <tbody>'''

for quote in data:
    html_content += f'''
            <tr>
                <td><strong>{quote["id"]}</strong></td>
                <td>"{quote['Quote']}"</td>
                <td>{quote['Author']}</td>
            </tr>'''

html_content += '''
        </tbody>
    </table>
    <div class="source-link">
        <p>Источник: <a href="https://quotes.toscrape.com/" target="_blank">Quotes to Scrape</a></p>
    </div>
</body>
</html>'''

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)
print("✓ HTML страница создана: index.html")
print("\n=== ВСЕ ЗАДАНИЯ ВЫПОЛНЕНЫ ===")