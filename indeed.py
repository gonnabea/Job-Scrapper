import requests
from bs4 import BeautifulSoup

LIMIT = 50
URL = f"https://kr.indeed.com/%EC%B7%A8%EC%97%85?as_and=python&as_phr=&as_any=&as_not=&as_ttl=&as_cmp=&jt=all&st=&radius=25&l=&fromage=any&limit={LIMIT}"


def extract_indeed_pages():
    result = requests.get(
        URL)

    soup = BeautifulSoup(result.text, 'html.parser')

    pagination = soup.find("div", {"class", "pagination"})

    links = pagination.find_all("a")
    pages = []
    for link in links[0:-1]:
        pages.append(int(link.string))

    max_page = pages[-1]
    return max_page


def extract_indeed_jobs(last_page):
    for page in range(last_page):
        result = requests.get(f"{URL}&start={page*LIMIT}")
        print(result.status_code)