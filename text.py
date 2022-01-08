import requests
from bs4 import BeautifulSoup

indeed_result = requests.get("https://kr.indeed.com/취업?as_and=python&limit=50")

indeed_soup = BeautifulSoup(indeed_result.text,"html.parser")

pagination = indeed_soup.find("ul",{"class":"pagination-list"})

pages = pagination.find_all("li")

spans = []

for page in pages[:-1]:  #pages 에서 >버튼 제거
    if(page.find("b")):
        spans.append(page.find("b"))
    elif(page.find("span")):
        spans.append(page.find("span"))

print(spans)


