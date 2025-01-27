import requests
from bs4 import BeautifulSoup as BS

URL = "https://litnet.com/ru"

HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
}


def get_html(url, params = ''):
    try:
        request = requests.get(url, headers=HEADERS, params=params)
        return request
    except:
        return f"Error: {url}"

def get_data(html):
    bs = BS(html, features="html.parser")
    items = bs.find_all("div", class_="col-xs-7")
    litres_list = []
    for item in items:
        title = item.find("a").get_text(strip=True)
        href = "https://litnet.com" + item.find("a").get("href")
        litres_list.append({
            'title': title,
            'href': href}
        )
    return litres_list


def parsing():
    response = get_html(URL)
    if response.status_code == 200:
        litres_list2 = []
        for page in range(1, 2):
            response = get_html(f"https://litnet.com/ru/top/all", params={'page':page})
            litres_list2.extend(get_data(response.text))
        return litres_list2[:3]

    else:
        raise Exception('Eror parsing')

# print(parsing())
