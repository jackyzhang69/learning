import itchat
import time
from datetime import datetime
import pandas as pd 

# find all my friends
def allFriends():
    friends=itchat.get_friends(update=True)  

    print(f"There are {str(len(friends))} friends")
    i=0
    for friend in friends:
        #print(f"{i} {friend['NickName']} {friend['UserName']}")
        print(friend)
        i+=1
    return friends



def allGroups():
    rooms = itchat.get_chatrooms(update=True)
    print(f'There are {len(rooms)} wechat groups')
    i=0
    for room in rooms:
        print(room['NickName'],room['UserName'])
    
    return rooms
def send2groups(msg,remarkNames):
    for remarkName in remarkNames:
        group=itchat.search_chatrooms(name=remarkName)[0]
        userName=group['UserName']
        itchat.send(message,toUserName=userName)

def send2indiduals(msg, individuals):
    for individual in individuals:
        person=itchat.search_friends(remarkName=individual )[0]
        userName=person['UserName']
        itchat.send(msg,toUserName=userName)

def toTargets(message,target):

    df=pd.read_csv('aiwechat\\send_list.txt')
    print(df)

    if target=='group':
        groups=df['RemarkName'][df['Group']==True].to_list()
        send2groups(message,groups)

    elif target=='individual': 
        individuals=df['RemarkName'][df['Group']==False].to_list()
        send2indiduals(message,individuals)
    elif target=='both':
        groups=df['RemarkName'][df['Group']==True].to_list()
        send2groups(message,groups)
        individuals=df['RemarkName'][df['Group']==False].to_list()
        send2indiduals(message,individuals)
    else:
        return 1

print("scan the 2d code")
#scan wechat 2d code and login
itchat.auto_login(hotReload=True)

# friend_remarkName=input("enter the name: ")
message="Hi " +str(datetime.now())
toTargets(message,'group')

# Identify the friend with name: remarkName, return a list of friends
# friends=friend_UserName=itchat.search_friends(remarkName=friend_remarkName)
# i=input("Pick which friend by number: ")
# Pick the matching friend
# friend_UserName=friends[int(i)]['UserName']
# send out the message
# itchat.send_msg(msg=message,toUserName=friend_UserName)










