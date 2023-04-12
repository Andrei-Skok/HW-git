import requests
from bs4 import BeautifulSoup
from unicodedata import normalize
import pandas as pd

av = requests.get('https://cars.av.by/citroen/c5')
print(av)  # смотрим ответ сервера
soup_av = BeautifulSoup(av.content, 'html.parser')
# парсим данные и форматируем кодировку
models = soup_av.findAll(class_="listing-item__title")
models = [normalize('NFKC', str(model.text)) for model in models]
prices_byn = soup_av.findAll(class_="listing-item__price")
prices_byn = [normalize('NFKC', str(price.text)) for price in prices_byn]
prices_usd = soup_av.findAll(class_="listing-item__priceusd")
prices_usd = [normalize('NFKC', str(price.text)) for price in prices_usd]
# удаление лишних символов из цены в USD и перевод к числовому типу
for price in prices_usd:
    price_formated = str()
    for symbol_ in price:
        if symbol_.isdigit():
            price_formated += symbol_
    prices_usd[prices_usd.index(price)] = int(price_formated)

params = soup_av.findAll(class_="listing-item__params")
params = [param.contents for param in params]
# каждую строку в params разбиваем на 6 отдельных списков
years, gearbox_type, engine_capacity, fuel_type, body_type, mileage = list(), list(), list(), list(), list(), list(),
for param in params:
    years.append(normalize('NFKC', str(param[0].text)))
    gearbox_type.append(((normalize('NFKC', str(param[1].text))).split(' ')[0])[:-1])
    engine_capacity.append((normalize('NFKC', str(param[1].text)).split(' ')[1]))
    fuel_type.append(((normalize('NFKC', str(param[1].text))).split(' ')[3])[:-1])
    body_type.append((normalize('NFKC', str(param[1].text))).split(' ')[-1])
    mileage.append(normalize('NFKC', str(param[2].text)))
links = [link.get('href') for link in soup_av.findAll(class_="listing-item__link")]

# собираем словарь всех данных об авто
total_dict = {'model': models, 'BYN': prices_byn, 'USD': prices_usd, 'year': years,
              'gearbox_type': gearbox_type, 'engine_capacity': engine_capacity, 'fuel_type': fuel_type,
              'body_type': body_type, 'mileage': mileage, 'link': links}
# переводим словарь в DataFrame для удобства сортировки, записи в файл
data = pd.DataFrame(total_dict)
data_sort_usd = data.sort_values(by='USD')

with open('av.csv', 'w', encoding='UTF-8') as file_csv:
    data_sort_usd.to_csv(file_csv)