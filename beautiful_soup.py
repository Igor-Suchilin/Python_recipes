from urllib.request import urlopen, urlretrieve
from bs4 import BeautifulSoup

html = urlopen('file:///C:/Users/mrsuc/Downloads/5.html').read().decode('utf8') # считываем содержимое
soup = BeautifulSoup(html, 'html.parser') # делаем суп
print(sum(int(item.get_text()) for item in soup.findAll('td')))