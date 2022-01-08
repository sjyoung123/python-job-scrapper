# import requests
# from bs4 import BeautifulSoup

# LIMIT = 50

# BASE_URL = f"https://kr.indeed.com/취업?as_and=python&limit={LIMIT}"

# item_list = []


# def get_indeed_last_page():
#     index = 100
#     go = True

#     while go:
#         indeed_result = requests.get(f"{BASE_URL}&start={index*LIMIT}")
#         indeed_soup = BeautifulSoup(indeed_result.text,"html.parser")
        
#         ul = indeed_soup.find("ul",{"class":"pagination-list"})
       
#         lis = ul.find_all("li")
#         index +=1
        
#         for li in lis:
#             if(not ul.find("svg")):
#                 go = False
#                 item_list.append(li)
#                 return
#             item_list.append(li)
           

# get_indeed_last_page()
# print(item_list[-1])

import requests
from bs4 import BeautifulSoup

LIMIT = 50

BASE_INDEED_URL = f"https://kr.indeed.com/취업?as_and=python&limit={LIMIT}"


def extract_indeed_pages():
    result = requests.get(f"{BASE_INDEED_URL}&start=9999")

    soup = BeautifulSoup(result.text,"html.parser")

    ul = soup.find("ul",{"class":"pagination-list"})

    lis = ul.find_all("li")

    max_pages = int(lis[-1].string)

    return max_pages


def extract_indeed_jobs(last_page):
    jobs=[]
    # for page in range(last_page):
    result = requests.get(f"{BASE_INDEED_URL}&start={0*LIMIT}")
    soup = BeautifulSoup(result.text,"html.parser")
    results = soup.find_all("div",{"class":"job_seen_beacon"})
    for result in results:
        title = (
            result
            .find("table",{"class":"jobCard_mainContent"})
            .find("h2",{"class":"jobTitle"}).find(title=True).string
            )
        company = (result.find("span",{"class":"companyName"}).string)
        print(company)
    return jobs
