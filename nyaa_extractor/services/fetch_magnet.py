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

call(" ")
