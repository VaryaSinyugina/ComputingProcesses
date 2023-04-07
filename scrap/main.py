import requests
from lxml import html
import pandas as pd

__author__ = 'Варвара Синюгина'

def get_page_text(url):
    """Получение html-разметки страницы"""

    res = requests.get(f"{url}")
    text = res.text  # текст страницы
    return text


def get_news_list(text):
    """Получение списка новостей с одной страницы в HTML-формате"""

    page_text = html.fromstring(text) #html - модуль из библеотеки lxml (принцип работы)
    div_news = page_text.xpath('//div[@id = "news"]')[0]
    news_list = div_news.xpath('//div[@class = "preview_new" or @class = "preview_new_end"]')

    return news_list


def set_new_info(news_list, df):
    """Добавление деталей о новостях из news_list в DataFrame
    news_list - список дивов новостей,
    df - таблица с данными"""

    for new in news_list:
        header = new.xpath('.//div[@class = "headline"]/text()')
        tags_list = new.xpath('.//a[@class = "marker_news"]/text()')
        tags = ' '.join(tags_list)
        date_list = new.xpath('.//p[@class = "day"]/text()') + new.xpath(
            './/p[@class = "yearInTileNewsOnPageWithAllNews"]/text()')
        date = ' '.join(date_list)
        images = new.xpath('.//img[@class = "img_news"]')

        row = {'Header': header, 'Tags': tags, 'Date': date, 'Image': images}
        row = pd.DataFrame(row)
        df = pd.concat([df, row], ignore_index=True)

    return df


# создание DataFrame
dict = {'Header': [],
        'Tags': [],
        'Date': [],
        'Image': []}
df = pd.DataFrame(dict)


n = 10   # кол-во страниц сайта

# прохождение по n страницам сайта новостей ЗабГУ
for i in range(1, n + 1):
    # получение разметки сайта в HTML-формате
    url = 'https://zabgu.ru/php/news.php?category=1&page=' + str(i)
    text = get_page_text(url)

    # получение списка новостей в HTML-формате
    news_list = get_news_list(text)

    # добавление новостей в таблицу DataFrame
    df = set_new_info(news_list, df)


# вывод данных
#print(df.to_markdown())
df.to_excel('result.xlsx')