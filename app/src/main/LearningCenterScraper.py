import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import sqlite3
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
#課程
class Course:
    # class ContactInformation :
    #     #聯絡資訊
    #     def __init__(self,ADDRESS = None,TELEPHONE_NUMBER = None,REMARKS = None):
    #         self.ADDRESS = ADDRESS #地址
    #         self.TELEPHONE_NUMBER = TELEPHONE_NUMBER #電話號碼
    #         self.REMARKS = REMARKS #備註
    #     def print(self):
    #         print(self.ADDRESS,self.TELEPHONE_NUMBER,self.REMARKS)
    def __init__(self,LEARNINGCENTER = None,COURSESACTIVITIES = None,DATE = None,LOCATION = None,LECTURER = None,REGISTRATIONSITUATION = None,COST = None):
        #課程活動資訊
        self.LEARNINGCENTER = LEARNINGCENTER #序號
        self.COURSESACTIVITIES = COURSESACTIVITIES #課程/活動名稱
        self.DATE = DATE #日期
        self.LOCATION = LOCATION #地點
        self.LECTURER = LECTURER #講師
        self.REGISTRATIONSITUATION = REGISTRATIONSITUATION #報名情形
        self.COST = COST #報名費用
    def print(self):
        print(self.LEARNINGCENTER,self.COURSESACTIVITIES,self.DATE,self.LOCATION,self.LECTURER,self.REGISTRATIONSITUATION,self.COST)
class database:
    #開啟資料庫
    def Connect(self):
        self.conn = sqlite3.connect('LiveAndLearn.db')
        print('Opened database successfully')
    def courseINSERT(self,course):
        self.Connect()
        sql = f"""INSERT INTO Learningcenter (LEARNINGCENTER,COURSESACTIVITIES,DATE,LOCATION,LECTURER,REGISTRATIONSITUATION,COST)
                VALUES('{course.LEARNINGCENTER}', '{course.COURSESACTIVITIES}', '{course.DATE}', '{course.LOCATION}', '{course.LECTURER}', '{course.REGISTRATIONSITUATION}', '{course.COST}')"""
        self.conn.execute(sql)
        self.conn.commit()
        print('Records created successfully') 

def content(s,center) :
    db = database()
    driverPath = 'C:\chromedriver\chromedriver.exe'
    browser = webdriver.Chrome(driverPath)
    # url = 'https://moe.senioredu.moe.gov.tw/HomeSon/Taipei/TaipeiIndex'
    url = 'https://moe.senioredu.moe.gov.tw/HomeSon/Taipei/TaipeiNewsCenter'
    browser.get(url)
    wait = WebDriverWait(browser, 10)
    wait.until(EC.presence_of_all_elements_located((By.TAG_NAME, 'style')))

    browser.find_element_by_link_text(s).click()
    wait = WebDriverWait(browser, 10)
    wait.until(EC.presence_of_all_elements_located((By.TAG_NAME, 'style')))
    # 切換到當前最新開啟的視窗
    windows = browser.window_handles
    browser.switch_to.window(windows[-1])
    # learningP = browser.find_elements_by_tag_name('p')
    # learningPlist = []
    # for i in learningP :
    #     learningPlist.append(i.text)
    # print(learningPlist)
    soup = BeautifulSoup(browser.page_source, 'lxml')
    tabList = soup.select('table .morenewstxt tbody tr')
    for i in range(len(tabList)):
        if center == '萬華區樂齡學習中心':
            LEARNINGCENTER = '萬華區樂齡學習中心無課程活動'
            COURSESACTIVITIES = ''
            DATE = ''
            LOCATION = ''
            LECTURER = ''
            REGISTRATIONSITUATION = ''
            COST = ''
        elif s == '臺北市中山區樂齡學習中心 110年 03 月課表' or s == '臺北市信義區樂齡學習中心110年三月份活動課表':
            if i == 21 :
                break
            td = tabList[i].select('td')
            LEARNINGCENTER = center
            COURSESACTIVITIES = td[1].text.strip().replace(u'\xa0', '')#.strip().replace(u'\xa0', '')去除爬蟲的&nbsp的html空格
            DATE = td[2].text.strip().replace(u'\xa0', '')
            LOCATION = td[3].text.strip().replace(u'\xa0', '')
            LECTURER = td[4].text.strip().replace(u'\xa0', '')
            REGISTRATIONSITUATION = ''
            COST = ''
        else :
            td = tabList[i].select('td')
            LEARNINGCENTER = center
            COURSESACTIVITIES = td[1].text.strip().replace(u'\xa0', '')
            DATE = td[2].text.strip().replace(u'\xa0', '')
            LOCATION = td[3].text.strip().replace(u'\xa0', '')
            LECTURER = td[4].text.strip().replace(u'\xa0', '')
            REGISTRATIONSITUATION = td[5].text.strip().replace(u'\xa0', '')
            COST = td[6].text.strip().replace(u'\xa0', '')      
        course = Course(LEARNINGCENTER, COURSESACTIVITIES, DATE, LOCATION, LECTURER, REGISTRATIONSITUATION, COST)
        course.print()
        db.courseINSERT(course)
    print()

def content2(s,center) :
    db = database()
    driverPath = 'C:\chromedriver\chromedriver.exe'
    browser = webdriver.Chrome(driverPath)
    # url = 'https://moe.senioredu.moe.gov.tw/HomeSon/Taipei/TaipeiIndex'
    url = 'https://moe.senioredu.moe.gov.tw/HomeSon/Taipei/TaipeiNewsCenter'
    browser.get(url)
    page_next = browser.find_element_by_partial_link_text('下一個')
    page_next.click()
    wait = WebDriverWait(browser, 10)
    wait.until(EC.presence_of_all_elements_located((By.TAG_NAME, 'style')))

    browser.find_element_by_link_text(s).click()
    wait = WebDriverWait(browser, 10)
    wait.until(EC.presence_of_all_elements_located((By.TAG_NAME, 'style')))
    # 切換到當前最新開啟的視窗
    windows = browser.window_handles
    browser.switch_to.window(windows[-1])
    # learningP = browser.find_elements_by_tag_name('p')
    # learningPlist = []
    # for i in learningP :
    #     learningPlist.append(i.text)
    # print(learningPlist)
    soup = BeautifulSoup(browser.page_source, 'lxml')
    tabList = soup.select('table .morenewstxt tbody tr')
    for i in range(len(tabList)):
        if s == '臺北市北投樂齡學習中心 110.03活動課程表':
            if i == 4 :
                break
        td = tabList[i].select('td')
        LEARNINGCENTER = center
        COURSESACTIVITIES = td[1].text.strip().replace(u'\xa0', '')
        DATE = td[2].text.strip().replace(u'\xa0', '')
        LOCATION = td[3].text.strip().replace(u'\xa0', '')
        LECTURER = td[4].text.strip().replace(u'\xa0', '')
        REGISTRATIONSITUATION = td[5].text.strip().replace(u'\xa0', '')
        COST = td[6].text.strip().replace(u'\xa0', '')      
        course = Course(LEARNINGCENTER, COURSESACTIVITIES, DATE, LOCATION, LECTURER, REGISTRATIONSITUATION, COST)
        course.print()
        db.courseINSERT(course)
    print()
#BeautifulSoup
html = requests.get('https://moe.senioredu.moe.gov.tw/HomeSon/Taipei/TaipeiIndex')
objSoup = BeautifulSoup(html.text, 'lxml')
learningSoup = objSoup.select('table .maintxt a')
learningCentreHref = []
learningCentreName = []
for i in learningSoup:
    learningCentreHref.append(i.get('href'))
    learningCentreName.append(i.text)
# print(learningCentreName)
# print(learningCentreHref)
#士林
center = '士林區樂齡學習中心'
s = '士林區樂齡中心：110年3月課程活動表'
content(s,center)
#中山
center = '中山區樂齡學習中心'
s = '臺北市中山區樂齡學習中心 110年 03 月課表'
content(s,center)
#文山
center = '文山區樂齡學習中心'
s = '110年3月臺北市文山區樂齡學習中心 課程活動表'
content(s,center)
#大同
center = '大同區樂齡學習中心'
s = '【大同樂齡學習中心】3月份課表'
content(s,center)
#南港
center = '南港區樂齡學習中心'
s = '臺北市南港區樂齡學習中心110年3月課程活動表'
content(s,center)
#信義
center = '信義區樂齡學習中心'
s = '臺北市信義區樂齡學習中心110年三月份活動課表'
content(s,center)
# 示範中心
center = '樂齡學習示範中心 '
s = '(示範中心)3月份課表'
content(s,center)
# 萬華
center = '萬華區樂齡學習中心'
s = '臺北市萬華區樂齡學習中心110年3月份無課程活動'
#內湖
center = '內湖區樂齡學習中心'
s = '內湖區樂齡學習中心110年3月份課程活動表'
content2(s,center)
# 北投
center = '北投區樂齡學習中心'
s = '臺北市北投樂齡學習中心 110.03活動課程表'
content2(s,center)
# 中正
center = '中正區樂齡學習中心'
s ='台北市中正區樂齡中心2021年3月份課表'
content2(s,center)