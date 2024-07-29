import requests
from bs4 import BeautifulSoup

URL = "https://www.tiobe.com/tiobe-index"
resp = requests.get(URL)
bs = BeautifulSoup(resp.text, "html.parser")

table = bs.find(id="top20")
rows = table.tbody.find_all("tr")
for row in rows:
    cols = row.find_all("td")
    print(f"{cols[4].text:20}  {cols[5].text}")
