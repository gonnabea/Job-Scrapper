import requests
from bs4 import BeautifulSoup


URL = f"https://stackoverflow.com/jobs?q=python&sort"


def get_last_page():
    result = requests.get(URL)
    soup = BeautifulSoup(result.text, 'html.parser')

    page = soup.findAll("a", {"class", "s-pagination--item"})
    last_page = page[-2].get_text(strip=True)
    return int(last_page)


def extract_jobs(last_page):
    jobs = []
    for page in range(last_page):
        result = requests.get(f"{URL}={page+1}")
        soup = BeautifulSoup(result.text, "html.parser")
        results = soup.find_all("div", {"class": "-job"})
        for result in results:
            print(result["data-jobid"])


def get_jobs():
    last_page = get_last_page()
    jobs = extract_jobs(last_page)
    return jobs
