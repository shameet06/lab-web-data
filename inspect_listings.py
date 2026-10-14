from bs4 import BeautifulSoup

with open('sample_merchandise.html', encoding='utf-8') as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')
for tag in soup.select(".price"):
    print(tag)
    
from lab_selectors import extract_listings

print(extract_listings(html = html))

with open('sample_merchandise.html', encoding='utf-8') as f:
    html = f.read()

catalog = extract_listings(html)

for item in catalog:
    print(item['name'])
    
phrases = ['obama', 'trump', 'mexico', 'russia', 'fake news', 'wall', 'freedom', 'jobs']