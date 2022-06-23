import time
from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd

def get_link(city):
    link = 'https://datalens.yandex/p2vmrzdwh4c6h?state='
    city_data = {"Адыгея": "9a230c76135", "Алтай": "da9cfcff134", "Амурская обл.": "3182e4a5142",
                 "Архангельская обл.": "47c6cd65147", "Астраханская обл.": "8cf40052146", "Башкортостан": "60067dc3141",
                 "Белгородская обл.": "760c2e42146", "Брянская обл.": "9a918b6f142", "Бурятия": "9cc36822136",
                 "Владимирская обл.": "2523979b146", "Вологодская обл.": "4d943bd0145", "Дагестан": "f604725e137",
                 "Еврейская АО": "e6bebe37141", "Ингушетия": "774892e5138", "Кабардино-Балкария": "aa733162147",
                 "Калмыкия": "2c31c6fc137", "Карелия": "9eb3034b136", "Краснодарский край": "da8f0a45147",
                 "Красноярский край": "088dbed4146", "Крым": "06a83904133", "Курганская обл.": "4dd8015b144",
                 "Ленинградская обл.": "590b1bf4147", "Москва": "ec31637b135", "Московская обл.": "6e7f7203144",
                 "Нижегородская обл.": "1d5c45af147", "Новгородская обл.": "4b024fdf146",
                 "Новосибирская обл.": "b0745765147",
                 "Пермский край": "9cdfecfc142", "Псковская обл.": "d5b82945143", "Ростовская обл.": "b5ccbd23144",
                 "Самарская обл.": "a58ad6a7143", "Санкт-Петербург": "05c59d0e144", "Саха (Якутия)": "4cca8969142",
                 "Свердловская обл.": "5f5bd1fb146", "Севастополь": "ab6e20ed140", "Татарстан": "d3a335eb138",
                 "Томская обл.": "416a56f8141", "Тюменская обл.": "fed109a9143", "ХМАО – Югра": "1fe702b8140",
                 "Хабаровский край": "5ac65755145", "Хакасия": "94fe3e9f136", "Челябинская обл.": "b5acf677145",
                 "Чечня": "b4532c5a134", "Ярославская обл.": "202dc939145"}
    link = link + city_data[city]
    return link


def get_data(link):
    try:
        driver = webdriver.Chrome()
        driver.get(link)
        time.sleep(2)
        html = driver.page_source
        return html
    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()


def clear_data(html):
    try:
        case = []
        date = []
        soup = BeautifulSoup(html, 'lxml')
        names_of_regions = soup.find_all('div', class_='chartkit-table__content chartkit-table__content_date')
        numbers_of_regions = soup.find_all('div', class_='chartkit-table__content chartkit-table__content_number')
        for i in range(len(names_of_regions)):
            clear = str(names_of_regions[i])
            clear = clear.replace('<div class="chartkit-table__content chartkit-table__content_date">',"")
            clear = clear.replace('</div>', "")
            date.append(clear)
            cases = str(numbers_of_regions[i])
            cases = cases.replace('<div class="chartkit-table__content chartkit-table__content_number">', "")
            cases = cases.replace('</div>', "")
            case.append(cases)
        data = dict(date=date, cases=case)
        print(data)
        return data, case
    except Exception as ex:
        print(ex)


def to_csv(data):
    df = pd.DataFrame(data)

    df.to_csv('data.csv', index=False)

