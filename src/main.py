# -*- coding: utf-8 -*-
"""Web Crawling for collecting papers.

Author:
    - Name: Wooshik Myung
    - Email: wooshik.m@gamil.com
"""

import ssl
from urllib.request import Request, urlopen

from bs4 import BeautifulSoup

# https forbidden
context = ssl._create_unverified_context()  # pylint: disable=W0212

URL = "https://scholar.google.com/scholar?hl=ko&as_sdt=0%2C5&q=hih&btnG="
request_url = Request(URL, headers={"User-Agent": "Mozilla/5.0"})
html = urlopen(request_url, context=context).read()

soup = BeautifulSoup(html, "html.parser")

blocks = soup.find_all(class_="gs_rt")

for block in blocks:
    elements = block.find("a")

    title = elements.text
    href = elements.attrs["href"]

    print(title)
    print(href)
    print()
