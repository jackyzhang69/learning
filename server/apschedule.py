import time
from apscheduler.schedulers.blocking  import BlockingScheduler

scheduler = BlockingScheduler()

def doit():
    print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
    # subprocess.call("python Crawler.py")

sched = BlockingScheduler()
# Every Monday, Tuesday, Wednsday, and Sunday from 08:00 to 20:00, get data every 15 minutes

sched.add_job(doit, 'cron', day_of_week='0,1,2,6',hour='8-20',minute='*/1')
sched.start()

