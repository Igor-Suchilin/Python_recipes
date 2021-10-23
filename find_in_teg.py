""" Код для нахождения наиболее часто встречающегося слова в теге"""

from urllib.request import urlopen
from collections import Counter
import re

html = urlopen("file:///C:/Users/mrsuc/Downloads/2.html").read().decode('utf-8')
s = str(html)
result = re.findall(r'<code>(\w+)</code>', s)
counts = Counter(result)
most = counts.most_common(3)
for m in most:
    print(m[0], end=" ")