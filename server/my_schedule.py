import schedule
import time

def job():
    schedule.every(1).seconds.do(doit)

def doit():
    print("I'm working... ")

def stopjob():
    schedule.cancel_job(doit)


# schedule.every(1).seconds.do(job)
# schedule.every().hour.do(job)
# schedule.every().day.at("10:30").do(job)
# schedule.every(5).to(10).minutes.do(job)
# schedule.every().monday.do(job)
# schedule.every().wednesday.at("13:15").do(job)
# schedule.every().minute.at(":17").do(job)



# schedule.every().sunday.at('08:46').do(stopjob)


while True:
    schedule.every().sunday.at('08:55').do(job)
