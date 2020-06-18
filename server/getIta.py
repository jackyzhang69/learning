from selenium import webdriver
import pandas as pd
import itchat
import time
from datetime import datetime
import re
import json
from apscheduler.schedulers.blocking  import BlockingScheduler

# BCPNP ITA data. Run on linux server
def bcPnpIta():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox') # required when running as root user. otherwise you would get no sandbox errors. 
    driver = webdriver.Chrome('/home/dev/chromedriver', chrome_options=chrome_options,service_args=['--verbose', '--log-path=/tmp/chromedriver.log'])

    # driver = webdriver.Chrome()

    url = "https://www.welcomebc.ca/Immigrate-to-B-C/B-C-Provincial-Nominee-Program/Invitations-to-Apply"
    driver.get(url)

    itas=driver.find_elements_by_css_selector("tbody tr td")
    
    ita_date=itas[0].text.strip()
    ita_number=itas[1].text.strip()
    ita_si_sw=itas[2].text.strip()
    ita_si_sw_score=itas[3].text.strip()
    ita_other_consideration=re.sub(r'\n',' ',itas[4].text.strip())
    ita_si_ig=itas[5].text.strip()
    ita_si_ig_score=itas[6].text.strip()
    ita_si_elss='SI – Entry Level and Semi-Skilled'
    ita_si_elss_score=''
    if 'Tech Pilot' not in ita_other_consideration:
        ita_si_elss=itas[7].text.strip()
        ita_si_elss_score=itas[8].text.strip()
        ita_si_eesw=itas[9].text.strip()
        ita_si_eesw_score=itas[10].text.strip()
        ita_si_ee_ig=itas[11].text.strip()
        ita_si_ee_ig_score=itas[12].text.strip()
        is_Tech_Pilot=False
    else:
        ita_si_eesw=itas[7].text.strip()
        ita_si_eesw_score=itas[8].text.strip()
        ita_si_ee_ig=itas[9].text.strip()
        ita_si_ee_ig_score=itas[10].text.strip()
        is_Tech_Pilot=True

    ita_dict={
        'ita_date':ita_date,
        'ita_number':ita_number,
        'ita_si_sw':ita_si_sw,
        'ita_si_sw_score':ita_si_sw_score,
        'ita_other_consideration':ita_other_consideration,
        'ita_si_ig':ita_si_ig,
        'ita_si_ig_score':ita_si_ig_score,
        'ita_si_elss':ita_si_elss,
        'ita_si_elss_score':ita_si_elss_score,
        'ita_si_eesw':ita_si_eesw,
        'ita_si_eesw_score':ita_si_eesw_score,
        'ita_si_ee_ig':ita_si_ee_ig,
        'ita_si_ee_ig_score':ita_si_ee_ig_score,
        'is_Tech_Pilot':is_Tech_Pilot
    }
    driver.quit()
    return ita_dict
    # 1. 获取最新的ITA信息，跟数据库里的最新的比对，如果更新，加入数据库，并通过微信、WhatsApp、email发通知，自动更新website
    # 2. 自动统计数据库中，各类分数的走向，图形化显示
    # 3. 客户在做规划时，算分后，可以用分数和BCPNP ita的历史比较，判断被邀请的机会
    
def brief_news(ita_dict):
    news=f"On {ita_dict['ita_date']}, BCPNP invited {ita_dict['ita_number']} candidates for applicaiton. The ITA poitns are as the followings:\n"
    news+=f'{ita_dict["ita_si_sw"]}: {ita_dict["ita_si_sw_score"]}\n'
    news+=f'{ita_dict["ita_si_ig"]}: {ita_dict["ita_si_ig_score"]}\n'
    news=(news+f'{ita_dict["ita_si_elss"]}: {ita_dict["ita_si_elss_score"]}\n') if ita_dict['ita_si_elss_score']!='' else news
    news+=f'{ita_dict["ita_si_eesw"]}: {ita_dict["ita_si_eesw_score"]}\n'
    news+=f'{ita_dict["ita_si_ee_ig"]}: {ita_dict["ita_si_ee_ig_score"]}\n'
    news+=f'Remarks: {ita_dict["ita_other_consideration"]}\n'

    return news

def isNewData(ita_dict):
    df=pd.read_csv('itas.txt',parse_dates=['Date'] )
    labels=df.columns
    date=datetime.strptime(ita_dict['ita_date'],'%B %d, %Y')
    cd=[[date,ita_dict['ita_si_sw_score'],ita_dict['ita_si_ig_score'],ita_dict['ita_si_elss_score'],ita_dict['ita_si_eesw_score'],ita_dict['ita_si_ee_ig_score'],ita_dict['ita_number'],ita_dict['is_Tech_Pilot']]]
    cdf=pd.DataFrame.from_records(cd, columns=labels)
    # 最新数据比对文件中最后的数据，如果日期为新，则添加数据
    if cdf.iloc[0,0] > df.iloc[-1,0]:
        df=df.append(cdf)
        df['Date']=df['Date'].dt.strftime('%Y%m%d') 
        df.to_csv('itas.txt', mode='w', header=True,index=False)
        return True
    else:
        return False

def send2herds(msg,herds):
    for herd in herds:
        itchat.send(message,herd)

def send_news(message,target):

    df=pd.read_csv('aiwechat\\send_list.txt')
    print(df)

    if target=='group':
        groups=df['UserName'][df['Group']==True]
        send2herds(message,groups)

    elif target=='individual': 
        individuals=df['UserName'][df['Group']==False]
        send2herds(message,individuals)
    elif target=='both':
        herds=df['UserName']
        send2herds(message,herds)
    else:
        return 1


def getdata():
    ita_dict=bcPnpIta()
    if isNewData(ita_dict):
        send_news(brief_news(ita_dict),'both')
    else:
        itchat.send('no update',toUserName='filehelper')        

itchat.auto_login(hotReload=True,enableCmdQR=2) # login in wechat, do it once 
# getdata()

scheduler = BlockingScheduler()
sched = BlockingScheduler()
# Every Monday, Tuesday, Wednsday, and Sunday from 08:00 to 20:00, get data every 15 minutes
sched.add_job(getdata, 'cron', day_of_week='0,1,2,6',hour='8-20',minute='*/1')
sched.start()

