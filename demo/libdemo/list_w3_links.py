import requests
from bs4 import BeautifulSoup

WEBSITE = "https://www.w3schools.com"
resp = requests.get(WEBSITE)
bs = BeautifulSoup(resp.text, "html.parser")

links = bs.find_all("a")
print(len(links))

hrefs = set()
for link in links:
    href = link['href']
    if 'javascript:void' in href:
        continue

    if not href.startswith("http"):
        if href.startswith("/"):
            href = WEBSITE + href
        else:
            href = WEBSITE + "/" + href

    hrefs.add(href)

for href in sorted(hrefs):
    print(href)

print(len(hrefs))
