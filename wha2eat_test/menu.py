#-*- coding: utf-8 -*-
#!/usr/bin/env python3
from bs4 import BeautifulSoup
import pandas as pd
import datetime
import requests
import time
import schedule
# import os
# os.environ['DISPLAY'] = ':0'
# os.environ['XAUTHORITY'] = '/run/user/1000/gdm/Xauthority'
# import pyautogui
# 스크린샷 라이브러리

#전역변수로 DISPLAY = 0하는 방법도 있다
#echo "DISPLAY=:0" >> ~/.bashrc
#source ~/.bashrc

# nohup python3 menu.py 1> /dev/null 2>&1 &을 사용하여 실행
# /dev/null 2>&1 & 뜻 == dev/null로 리다이렉션해서 표준출력을 버리라는 뜻

# nohup python3 server.py &를 사용하여 실행
#bs4는 데이터 크롤링을 위한 라이브러리 == pip install beautifulsoup4
#pandas는 csv 파일을 만들기 위해 필요한 것 같다
#request는 파이썬 HTTP 라이브러리 pip install requests

headers = {
	"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36"
}
#user-agent 요청 헤더는 서버와 네트워크 피어가 요청하는 사용자 에이전트의 정보를 식별할 수 있도록 하는 문자열이다.


def job():
	r = requests.get('https://www.kw.ac.kr/ko/life/facility11.jsp', headers=headers)
	soup = BeautifulSoup(r.text, 'html.parser')
	table = soup.find('table', {'class': 'tbl-list'})
	thead = table.find('thead')
	tbody = table.find('tbody')

	diet1 = map(lambda node: node.text.replace("\n",""), thead.findAll("th")[1:])
	diet2 = map(lambda node: node.text, tbody.findAll("td")[1:])
	data= [diet1,diet2]

	toSave = pd.DataFrame(data)
	toSave.to_csv("./table.csv", index=False, header=False, encoding="utf-8")

	now =datetime.datetime.now()
	now =str(now)
	with open("./log.txt",'a') as f:
		f.write("["+now+"] "+"update the diet!\n")
		f.close()

schedule.every(3).hours.do(job)

while True:
	schedule.run_pending()
	time.sleep(1)