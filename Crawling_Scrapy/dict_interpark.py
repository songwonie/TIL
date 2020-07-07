"""
 크롤링의 처리속도를 최대화 하기 위해, dict 형태로 필요정보를 받아온다.

 받아오는 페이지를 모두 dict에 입력한 후,

 BeautifulSoup 상에서 데이터를 가공한다.
"""

from selenium import webdriver as wd 
import time

driver = wd.Chrome('chromedriver.exe')
driver.get("https://tour.interpark.com/")
time.sleep(2)

# 최대 대기시간 설정
driver.implicitly_wait(10)

# 검색 키워드 입력
keyword = input("\n 여행지 검색: ")
Items = driver.find_element_by_id("SearchGNBText")
Items.send_keys(keyword)

# 검색 클릭
driver.find_element_by_class_name('search-btn').click()
# 해외여행지 더보기 클릭!
driver.find_element_by_css_selector('.oTravelBox > ul.boxList > li.moreBtnWrap .moreBtn').click()


# 총 페이지 받아오기
Pages = driver.find_elements_by_css_selector('.panelZone > div.pageNumBox > ul > li')
if Pages:
    print(" {} 여행지 페이지 받아옴!\n".format(keyword))


'''
여러 페이지의 html 소스를 dict로 받는다
'''
HTML_dict = {} # 여러 페이지를 받을 dict 선언.

# 자바스크립트 실행, 페이지 넘기기
for page in range(1, len(Pages)+1):
    driver.execute_script("searchModule.SetCategoryList({}, '')".format(page))
    time.sleep(2)
    print("{} 페이지 이동".format(page))

    # 각 페이지마다 소스 dict에 담기
    HTML_dict[page] = driver.page_source 

print("{} 여행지 {} 페이지 불러옴\n".format(keyword, len(HTML_dict)))
# print(HTML_dict[1])

# 셀레니움 닫기
driver.quit()


'''
BeautifulSoup 처리
'''
from bs4 import BeautifulSoup

# 여행지명과 가격을 담을 리스트 생성
tour_List = []

for n in range(1, len(HTML_dict)+1):
    # 각 페이지 마다 담은 dict, soup로 담기
    soup = BeautifulSoup(HTML_dict[n], "html.parser")
    tour_names = soup.select('.proTit') # class명='proTit', 여행지명
    tour_prices = soup.select('.proPrice') # 가격
    # print("Page = ", n)
    # print(tour_names)
    # print(tour_prices)
    # print("="*100)

    # 리스트에 여행지명, 가격 담기
    for i in range(len(tour_names)):
        name = tour_names[i].get_text().strip()
        price = tour_prices[i].get_text().replace('~', '').replace('원', '').replace(',', '').strip()
        print("투어명:", name)
        print("가격:", price)
        print('='*80)
        tour_List.append([name,price])

# print(len(tour_List))

for tour in tour_List:
    print(tour)

# csv 파일 저장
with open("tour_info.csv", "w") as file:
    file.write("여행상품,가격\n")
    for tour in tour_List:
        file.write("{},{}\n".format(tour[0],tour[1]))
    print("저장 완료!")


'''
# 표로 그리기
import pandas as pd 
import matplotlib as mpl 
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm # matplotlib로 그릴 폰트 설정
    
font_name = fm.FontProperties(fname='C:/Windows/Fonts/malgun.ttf').get_name()
mpl.rc('font', family=font_name)

df = pd.read_csv("tour_info.csv", index_col='여행상품', encoding='cp949')

ax = df.plot(kind='bar', title='여행정보', figsize=(12,4), legend=True, fontsize=12)
ax.set_xlabel("제품명", fontsize=8)
ax.set_ylabel("가격", fontsize=8)
ax.legend(['여행상품','가격'], fontsize=8)
plt.show()
'''
