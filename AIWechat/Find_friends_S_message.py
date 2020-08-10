import itchat
import pandas as pd 
import time

def getUser(rmk_name):
    person=itchat.search_friends(remarkName=rmk_name )[0]
    return person['UserName']
        
def getGroup(nick_name):
    room=itchat.search_chatrooms(name=nick_name )[0]
    return room['UserName']

def send2Group(nick_name,message):
    itchat.send(message,toUserName=getGroup(nick_name))
    time.sleep(1)

def send2User(remark_name,message):
    itchat.send(message,toUserName=getUser(remark_name))
    time.sleep(1)

def send2AllinList(message):
    df=pd.read_csv('/home/jacky/aiadvisor/learning/AIWechat/test_list.txt')
    group_filt=(df['Group']==True)
    Individual_filt=(df['Group']==False)

    df.loc[group_filt,'NickName'].apply(send2Group,message=message) # 目前微信群 只能用NickName搜索
    df.loc[Individual_filt,'RemarkName'].apply(send2User,message=message)

for i in range(10):
    send2AllinList("hi")