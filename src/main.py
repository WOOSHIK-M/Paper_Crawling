# -*- coding: utf-8 -*-
"""Web Crawling for collecting papers.

Author:
    - Name: Wooshik Myung
    - Email: wooshik.m@gamil.com
"""

import ssl
from typing import Dict
from urllib.request import Request, urlopen

from bs4 import BeautifulSoup


def paper_summary(paper_info: Dict[str, str]) -> None:
    """Pretty print paper summary."""
    str_length = len(paper_info["title"]) + 10
    print("=" * str_length)
    print(f"{paper_info['title']}".center(str_length))
    print("=" * str_length)
    print(f"-> (ABSTRACT): {paper_info['abstract']}")
    print(f"-> (LINK): {paper_info['href']}")
    print()


def crawling_a_page(url: str) -> None:
    """Crawling paper description with a given URL."""
    context = ssl._create_unverified_context()  # pylint: disable=W0212
    request_url = Request(url, headers={"User-Agent": "Mozilla/5.0"})
    html = urlopen(request_url, context=context).read()
    soup = BeautifulSoup(html, "html.parser")

    blocks = soup.find_all(class_="gs_ri")
    assert blocks, "Something is wrong ..."
    for block in blocks:
        title_block = block.find(class_="gs_rt")

        paper_info: Dict[str, str] = {
            "title": title_block.text,
            "href": title_block.find("a").attrs["href"],
            "journal_name": block.find(class_="gs_a").text,
            "abstract": block.find(class_="gs_rs").text,
        }
        paper_summary(paper_info)


if __name__ == "__main__":
    # test_keywords: floorplan, automatic, physical design
    KEYWORDS = input("keywords: ").split(",")
    assert KEYWORDS, "Plaese give me more than a keyword(s)!!!"
    keywords = [keyword.strip().replace(" ", "+") for keyword in KEYWORDS]

    N_PAGES = int(input("pages: "))

    GOOGLE_SCHOLAR_PRE = "https://scholar.google.com/scholar?"
    GOOGLE_SCHOLAR_POST = "&hl=ko&as_sdt=0,5"
    GOOGLE_SCHOLAR_KEYS = "q=" + ",+".join(keywords)

    # make urls
    urls = [
        GOOGLE_SCHOLAR_PRE
        + f"start={page * 10}&"
        + GOOGLE_SCHOLAR_KEYS
        + GOOGLE_SCHOLAR_POST
        for page in range(N_PAGES)
    ]

    # do crawling
    for url in urls:
        crawling_a_page(url)
