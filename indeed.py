import requests
from bs4 import BeautifulSoup

LIMIT = 50


def get_last_page(URL):
    result = requests.get(
        URL)

    soup = BeautifulSoup(result.text, 'html.parser')

    pagination = soup.find("div", {"class", "pagination"})
    if pagination:
        links = pagination.find_all("a")
        pages = []
        for link in links[0:-1]:
            pages.append(int(link.string))

        max_page = pages[-1]
        return max_page


def extract_job(html):
    title = html.find("h2", {"class": "title"}).find("a")["title"]
    company = html.find("span", {"class": "company"})
    if company:
        company_anchor = company.find("a")
        if company_anchor is not None:
            company = company_anchor.string
        else:
            company = company.string
        if company:
            company = company.strip()
        location = html.find("div", {"class": "recJobLoc"})["data-rc-loc"]
        job_id = html["data-jk"]

        return {'title': title, 'company': company, "location": location, "link": f"https://kr.indeed.com/%EC%B7%A8%EC%97%85?q=python&l&radius=25&vjk={job_id}"}


def extract_jobs(last_page, URL):
    jobs = []
    if last_page:
        for page in range(last_page):
            print(f"인디드 스크래핑중... (page: {page})")
            result = requests.get(f"{URL}&start={page*LIMIT}")
            soup = BeautifulSoup(result.text, 'html.parser')
            results = soup.find_all("div", {"class": "jobsearch-SerpJobCard"})
            for result in results:
                job = extract_job(result)
                jobs.append(job)
        return jobs


def get_jobs(word):
    URL = f"https://kr.indeed.com/jobs?q={word}&l=&ts=1603147718590&rq=1&rsIdx=0&fromage=last&newcount=351"
    last_page = get_last_page(URL)
    jobs = extract_jobs(last_page, URL)
    return jobs
