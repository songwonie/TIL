import datetime

now = datetime.datetime.now()
'''
print("{}년 {}월 {}일 {}시 {}분 {}초".format(\
                                      now.year,
                                      now.month,
                                      now.day,
                                      now.hour,
                                      now.minute,
                                      now.second))
'''

first_user = ()  # 최초 사용자 성함 tuple
birth_day = ()
sch_list = [] # 스케줄 list (변동 가능성)

print("\n"*3)
print("  Alarm Program 사용 시작")
print("\n"*3)

# 알림 mod.
def Alarm_mod(user_name, month, day): 
    if day == (now.day-1): # 하루전날 발송
        print("\n")
        print("{}님! 내일이 생일이시네요! 내일 쿠폰발송 예정입니다.\n".format(user_name))
    elif day == (now.day):
        print("\n")
        print("{}월 {}일 자로, 쿠폰 발송!".format(month, day))


if not first_user:  # 빈 튜플이나 리스트 확인방법!
    first_user = input("  이름을 알려주세요:")
    print("\n")
    birth_day = input("  생년월일을 알려주세요 (ex: 1997-07-29 or" + "'오늘'을 입력하면 현재날짜 적용!)" + "):")
    print("\n")

    if birth_day[0] == '오' and birth_day[1] == '늘':
        # birth_day.clear() 튜플은 삭제 변경 안됨!!
        birth_day = (now.year, now.month, now.day) # tuple 입력방법
        
        # tuple을 split!
        birth_year = int(birth_day[0]) 
        birth_month = int(birth_day[1]) 
        birth_date = int(birth_day[2])
        print(birth_day)
        print("  {}님은 {}년 {}월 {}일 생일로 등록되었습니다.".format(first_user, now.year, now.month, now.day))
    # print("birth_day tuple:", tuple(birth_day))
    
    else:
        birth_year = int(birth_day.split('-')[0]) 
        birth_month = int(birth_day.split('-')[1]) # int형 변환
        birth_date = int(birth_day.split('-')[2])
        print("  {}님은 {}년 {}월 {}일 생일로 등록되었습니다.".format(first_user, birth_year, birth_month, birth_date))
        # print(type(birth_month))


# 사용자 명이 등록되었다면,
if first_user:
    print("\n")
    # 생일 하루전 또는 당일날 문자 발송!
    if now.day == (birth_date-1) or now.day == birth_date:
        Alarm_mod(first_user, birth_month, birth_date)

'''
프로그램 작동중인 while문을 추가해서 routine을 개발해보자.
'''

    # 스케줄 입력
    sch_name = input("  {}님! 스케줄 명을 입력해주세요:".format(first_user))
    print("\n")
    sch_year, sch_month, sch_date = input("  {} 스케줄의 날짜를 입력해주세요:".format(sch_name)).split('-')
    
    # (스케줄명,스케줄 날짜) 튜플 형태로 리스트에 append!
    sch_list.append((sch_name, sch_year, sch_month, sch_date))
    print(sch_list)



    

    
       
        
