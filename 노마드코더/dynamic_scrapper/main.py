from playwright.sync_api import sync_playwright
import time
from bs4 import BeautifulSoup
import csv

p = sync_playwright().start()

browser = p.chromium.launch(headless=False)

page = browser.new_page()

# headless mode로 작동하므로 브라우저를 실행시키지만 보이지 않는다.
page.goto("https://www.wanted.co.kr/")

time.sleep(3)

# page.screenshot(path="screenshot.png")

# css selector을 넣어야한다.
page.click("button.Aside_searchButton__Xhqq3")

time.sleep(3)

# placeholder를 찾아 flutter 입력
page.get_by_placeholder("검색어를 입력해 주세요.").fill("flutter")

# Enther키 적용
page.keyboard.down('Enter')

time.sleep(3)

# search_tab_position 를 가진 anchor
page.click("a#search_tab_position")

for x in range(5):
    time.sleep(3)
    page.keyboard.down("End")
    
content = page.content()

p.stop()

soup = BeautifulSoup(content, "html.parser")

jobs = soup.find_all("div", class_="JobCard_container__FqChn")

jobs_db = []

num = 0

for job in jobs:
    # num = num + 1을 의미
   num += 1
   
   title = job.find("strong", class_="JobCard_title__ddkwM").text
   
   company_name = job.find("span", class_="JobCard_companyName__vZMqJ").text
   
   reward = job.find("span", class_="JobCard_reward__sdyHn").text
   
    # anchor의 href 선택해 link 획득
   link = f"https://www.wnted.co.kr{job.find('a')['href']}"
   
   job = {
       "num" : num,
        "title" : title,
        "company_name" : company_name,
        "reward" : reward,
        "link" : link,
   }
   jobs_db.append(job)

# jobs.csv "쓰기" 모드로 실행
file = open("jobs.csv", "w")
writer = csv.writer(file)
writer.writerow(["Num", "Title", "Company", "Reward", "Link"])

# writerrow()는 리스트만 받는다.
# dictionaly에 values()를 사용하면 값들이 리스트로 반환된다.
for job in jobs_db:
    writer.writerow(job.values())
