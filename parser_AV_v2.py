import requests
from bs4 import BeautifulSoup
import csv


class Parser:
    def __init__(self, url):
        self.url = url
        self.counter_page = 0

    def req(self):
        self.response = requests.get(self.url)
        print(f"Ответ сайта: {self.response} для {self.url[self.url.find('page='):]}")
        return self.response

    # метод сохранения страницы в файл
    def to_file(self):
        with open('index.html', 'w', encoding='UTF-8') as file:
            file.write(self.response.text)

    def soup(self):
        self._soup = BeautifulSoup(self.response.text, 'lxml')
        return self._soup

    def parsing(self):
        self.titles = self._soup.find_all('h3', class_=['listing-top__title', 'listing-item__title'])
        self.prices = self._soup.find_all(class_=['listing-top__price', 'listing-item__prices'])
        self.params = self._soup.find_all(class_=['listing-top__params', 'listing-item__params'])
        if bool(self.titles) and bool(self.prices) and bool(self.params):
            return zip(self.titles, self.prices, self.params)
        else:
            return False

    def next_page(self):
        self.counter_page += 1
        self.url = self.url[:self.url.find('page=')] + 'page=' + str(self.counter_page)
        self.req()
        self.soup()
        return self.parsing()


class Auto:

    def __init__(self, model=None, price_byn=None, price_usd=None, year=None, gearbox_type=None,
                 engine_capacity=None, fuel_type=None, body_type=None, mileage=None, link=None, ):
        self.model = model
        self.price_byn = price_byn
        self.price_usd = price_usd
        self.year = year
        self.gearbox_type = gearbox_type
        self.engine_capacity = engine_capacity
        self.fuel_type = fuel_type
        self.body_type = body_type
        self.mileage = mileage
        self.link = link
        self.list_auto = list()

    def get_list_auto(self, parser):
        page_data = parser.next_page()
        while page_data:
            for title, price, param in page_data:
                if 'listing-top__params' in str(param):
                    param_list = param.text.split(',')
                elif 'listing-item__params' in str(param):
                    param_list = [param.find_next().text] + param.find_next().find_next().text.split(',') + [
                        param.find_next('span').text]
                self.list_auto.append(Auto(model=title.text,
                                           price_byn=price.find_next(
                                               class_=['listing-top__price-byn', 'listing-item__price']).text,
                                           price_usd=price.find_next(
                                               class_=['listing-top__price-usd', 'listing-item__priceusd']).text,
                                           link='https://cars.av.by' + title.find_next()['href'],
                                           year=param_list[0].format(),
                                           gearbox_type=param_list[1].format(),
                                           engine_capacity=param_list[2].format(),
                                           fuel_type=param_list[3].format(),
                                           body_type=param_list[4].format(),
                                           mileage=param_list[5].format()
                                           ))
            page_data = parser.next_page()
        return self.list_auto

    def get_data(self):
        self.line = (
            self.model,
            self.price_byn,
            self.price_usd,
            self.year,
            self.gearbox_type,
            self.engine_capacity,
            self.fuel_type,
            self.body_type,
            self.mileage,
            self.link
        )
        return self.line

    def to_csv_file(self):
        with open('all_citroen_c5_from_av.csv', 'w', encoding='UTF-8') as file:
            writer = csv.writer(file)
            for auto in self.list_auto:
                writer.writerow(auto.get_data())


if __name__ == '__main__':
    url = 'https://cars.av.by/filter?brands[0][brand]=43&brands[0][model]=181&page=1'
    parser_av = Parser(url=url)
    c5 = Auto()
    c5.get_list_auto(parser_av)
    c5.to_csv_file()
