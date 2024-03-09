import os
from dotenv import load_dotenv
load_dotenv()
from playwright.sync_api import sync_playwright
import time
from bs4 import BeautifulSoup
import csv

p = sync_playwright().start()

browser = p.chromium.launch(headless=False)

page = browser.new_page()

# 페이지 열기
page.goto("https://class.mju.ac.kr/login")

time.sleep(3)

# 팝업 닫기 클릭
page.click("a.languagehtml")

time.sleep(3)

# 학번 입력
page.get_by_placeholder("학번을 입력바랍니다.(Student ID)").fill(os.getenv("ID"))

time.sleep(1)

# 비밀번호 입력
page.get_by_placeholder("SSO 비밀번호를 입력바랍니다. (SSO Password)").fill(os.getenv("PASSWORD"))

time.sleep(1)

# 로그인
page.keyboard.down('Enter')

time.sleep(3)

# 
