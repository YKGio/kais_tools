import requests
from bs4 import BeautifulSoup

def call(url):
    response = requests.get(url)
    html = response.text
    # Parse the HTML using BeautifulSoup
    soup = BeautifulSoup(html, "html.parser")

    # Find all the torrent download rows
    rows = soup.find_all("tr")

    result = []
    for row in rows:
        columns = row.find_all("td")
        entry = {}
        for column in columns:
            links = column.find_all("a")
            for link in links:
                if "magnet" in link["href"]:
                    entry['magnet'] = link["href"]
                if "view" in link["href"]:
                    entry['title'] = link.text
        if entry:
            result.append(entry)

    return result

call("https://sukebei.nyaa.si/?f=0&c=0_0&q=%E5%8C%97%E5%B7%9D%E7%9E%B3&s=seeders&o=desc")
