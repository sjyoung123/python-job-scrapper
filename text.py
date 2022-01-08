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

BASE_URL = f"https://kr.indeed.com/취업?as_and=python&limit={LIMIT}"


indeed_result = requests.get(f"{BASE_URL}&start=9999")

indeed_soup = BeautifulSoup(indeed_result.text,"html.parser")

ul = indeed_soup.find("ul",{"class":"pagination-list"})

lis = ul.find_all("li")

print(lis[-1])