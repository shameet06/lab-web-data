from bs4 import BeautifulSoup

with open('sample_listings.html', encoding='utf-8') as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')
for tag in soup.select(".price"):
    print(tag)
