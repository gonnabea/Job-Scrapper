import requests
from bs4 import BeautifulSoup


def get_last_page(URL):
    result = requests.get(URL)
    soup = BeautifulSoup(result.text, 'html.parser')

    page = soup.findAll("a", {"class", "s-pagination--item"})
    last_page = 0
    if(len(page) > 2):
        last_page = page[-2].get_text(strip=True)
    elif len(page) == 1:
        last_page = 1
    else:
        pass
    return int(last_page)


def extract_job(html):
    title = html.find("h2").find("a")["title"]
    company, location = html.find("h3").find_all("span", recursive=False)
    company = company.get_text(strip=True)
    location = location.get_text(strip=True)
    job_id = html['data-jobid']
    return {
        'title': title,
        'company': company,
        'location': location,
        'apply_link': f"https://stackoverflow.com/jobs/{job_id}"
    }


def extract_jobs(last_page, URL):
    jobs = []
    if last_page > 50:  # 50페이지로 제한
        last_page = 50
    for page in range(last_page):
        print(f"스택오버플로우 스크래핑중... (page: {page})")
        result = requests.get(
            f"{URL}&so_source=JobSearch&so_medium=Internal&pg={page+1}")

        soup = BeautifulSoup(result.text, "html.parser")

        results = soup.find_all("div", {"class": "-job"})

        for result in results:
            job = extract_job(result)
            jobs.append(job)
    return jobs


def get_jobs(word):
    URL = f"https://stackoverflow.com/jobs?q={word}"

    last_page = get_last_page(URL)
    jobs = extract_jobs(last_page, URL)
    print(jobs)
    return jobs
