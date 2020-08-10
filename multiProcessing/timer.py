#!/home/jacky/venv/bin/python3
from apscheduler.schedulers.blocking  import BlockingScheduler
import multiprocessing as mp
import time

def job1():
    time.sleep(3)
    print("job1 done")    

def job2():
    time.sleep(3)
    print("job2 done")    

def job3():
    time.sleep(6)
    print("job3 done")    

def job4():
    time.sleep(6)
    print("job4 done")  

def calculate():
    p1 = mp.Process(target=job1)
    p2 = mp.Process(target=job2)
    p3 = mp.Process(target=job1)
    p4 = mp.Process(target=job2)
    p5 = mp.Process(target=job1)
    p6 = mp.Process(target=job2)
    p7 = mp.Process(target=job1)
    p8 = mp.Process(target=job2)
    p9 = mp.Process(target=job1)
    p10 = mp.Process(target=job2)
    p1.start()
    p2.start()
    p3.start()
    p4.start()
    p5.start()
    p6.start()
    p7.start()
    p8.start()
    p9.start()
    p10.start()

    p1.join()
    p2.join()
    p3.join()
    p4.join()
    p5.join()
    p6.join()
    p7.join()
    p8.join()
    p9.join()
    p10.join()



def printHello():
    p1 = mp.Process(target=job3)
    p1.start()
    p2 = mp.Process(target=job4)
    p2.start()

def printWelcome():
    print('hello,welcome')

def stillOn():
    print('I am still on')

sched = BlockingScheduler()

with open('/home/jacky/aiadvisor/learning/multiProcessing/test.txt','r') as f:
    Lines = f.readlines() 

for line in Lines[1:]: 
    terms=line.split('|')
    print(terms)
    if terms[2]=='week':
        sched.add_job(eval(terms[0]),'cron',day_of_week=terms[1],hour=terms[3],minute=terms[4],second=terms[5])
    if terms[2]=='month':
        sched.add_job(eval(terms[0]),'cron',day=terms[1],hour=terms[3],minute=terms[4],second=terms[5])

sched.add_job(stillOn,'cron',day_of_week='0-6',hour='08-20',minute='*/1',second='00')

sched.start()