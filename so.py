import requests
from bs4 import BeautifulSoup


URL = f"https://stackoverflow.com/jobs?q=python"


def get_last_page():
    result = requests.get(URL)
    soup = BeautifulSoup(result.text, 'html.parser')

    page = soup.findAll("a", {"class", "s-pagination--item"})
    last_page = page[-2].get_text(strip=True)
    return int(last_page)


def extract_job(html):
    title = html.find("h2", {"class": "fs-body3"}).find("a")["title"]
    company_name = html.find("h3", {"class": "fs-body1"}
                             ).find("span").get_text(strip=True)
    company_location = html.find("span", {"class": "fc-black-500"})
    print(title)


def extract_jobs(last_page):
    jobs = []

    for page in range(last_page):
        result = requests.get(f"{URL}$pg={page+1}")

        soup = BeautifulSoup(result.text, "html.parser")

        results = soup.find_all("div", {"class": "-job"})
        print(results)

        for result in results:
            job = extract_job(result)
            jobs.append(job)
    return jobs


def get_jobs():
    last_page = get_last_page()
    jobs = extract_jobs(last_page)
    return jobs
