import requests
from bs4 import BeautifulSoup

import json
import urllib # URL 디코딩에 필요


requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)

header = {
      'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 Edg/96.0.1054.62'
      }
      
#포스웰 메인 -개발자모드 - 인재창조원 메뉴(새창) - Name(todaymenu.php?...)
url = "https://www.poswel.co.kr/fmenu/todaymenu.php"

year = '2022'
month = '02'
day = '18'

param = {
      'area_code': 'A4',
      'nyear': year,
      'nmonth': month,
      'reqday': day,
}

res = requests.get(url, params=param, headers=header, verify=False)
res.raise_for_status()

soup = BeautifulSoup(res.text, "html.parser")
menu = soup.select("#today_menu_list01 > .today_menu_list01_box02 > div")


# print(menu) #리스트로 되어 있음
print(menu[0].text.strip()) #.strip() : 문자열 양 끝에 있는 공백을 제거