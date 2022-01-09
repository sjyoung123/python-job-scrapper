import requests
from bs4 import BeautifulSoup

LIMIT = 50

BASE_INDEED_URL = f"https://kr.indeed.com/취업?as_and=python&limit={LIMIT}"


def extract_indeed_pages():
    result = requests.get(f"{BASE_INDEED_URL}&start=9999")
    soup = BeautifulSoup(result.text, "html.parser")
    ul = soup.find("ul", {"class": "pagination-list"})
    lis = ul.find_all("li")
    max_pages = int(lis[-1].string)
    return max_pages


def extract_jobs(html):
    title = html.find("h2", {
        "class": "jobTitle"
    }).find("span", title=True).text
    company = (html.find("span", {"class": "companyName"}))
    if company is not None:
        company_anchor = company.find("a")
        if company_anchor is not None:
            company = company_anchor.string
        else:
            company = company.string
    location = html.find("div", {"class": "companyLocation"}).text
    job_id = (html["data-jk"])
    return {"title": title, "company": company, "location": location,
            "link": f"https://kr.indeed.com/채용보기?jk={job_id}"}


def extract_indeed_jobs(last_page):
    jobs = []
    for page in range(last_page):
        print(f"Page: {page}")
        result = requests.get(f"{BASE_INDEED_URL}&start={page*LIMIT}")
        soup = BeautifulSoup(result.text, "html.parser")
        results = soup.find_all("a", {"class": "fs-unmask"})
        for result in results:
            job = extract_jobs(result)
            jobs.append(job)
    return jobs
