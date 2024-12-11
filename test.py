from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# ChromeDriver 경로
driver_path = r"C:\Users\user\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe"

# ChromeOptions 설정
options = webdriver.ChromeOptions()

# Service 객체 생성
service = Service(driver_path)

# 기존 디버그 모드 Chrome 제어
driver = webdriver.Chrome(service=service, options=options)

loginUrl = "https://accounts.kakao.com/login/?continue=https%3A%2F%2Fkauth.kakao.com%2Foauth%2Fauthorize%3Fis_popup%3Dfalse%26ka%3Dsdk%252F2.7.3%2520os%252Fjavascript%2520sdk_type%252Fjavascript%2520lang%252Fko-KR%2520device%252FWin32%2520origin%252Fhttps%25253A%25252F%25252Fwww.tistory.com%26auth_tran_id%3DxzpC5eoC79hMp.B32nM0YDsf60TSojqgRCyiXJryNg7sy3.MC9EucI3LkN50%26response_type%3Dcode%26state%3DaHR0cHM6Ly93d3cudGlzdG9yeS5jb20v%26redirect_uri%3Dhttps%253A%252F%252Fwww.tistory.com%252Fauth%252Fkakao%252Fredirect%26client_id%3D3e6ddd834b023f24221217e370daed18%26through_account%3Dtrue&talk_login=hidden#login"

# 블로그 로그인
driver.get(loginUrl)
time.sleep(2)

# 로그인 정보 입력
driver.find_element(By.ID, 'loginId--1').send_keys('your_username')
driver.find_element(By.ID, 'password--2').send_keys('your_password')
#driver.find_element(By.ID, 'login-button').click()

driver.quit()