# news
Get data, news from website and push to social media, email, and websites.
## Install python3
~~~bash
$ sudo apt-get install python3.6
$ sudo apt update
~~~
## Install pip
~~~bash
$ sudo apt install python3-pip
~~~

## git clone
~~~bash
git clone https://github.com/jackyzhang69/news 
~~~

## Linux下搭建Python虚拟环境
~~~bash
$ sudo pip install virtualenv
$ virtualenv --python=/usr/bin/python3.8 news # 在news目录创建虚拟环境
$ source news/bin/activate
~~~


## install itchat 微信应用接口
~~~bash
pip3 install itchat
~~~

## install selenium 
~~~bash
pip3 install selenium
~~~

## 在服务器端运行程序，象service一样
nohup python3 news.py &  #只需要在send.py程序设定定时做什么动作，一直保持运行即可。 可以用ps查看进程，用kill 进程号终止. &的作用是让程序在后台运行。
实际最终并没有用nohup，因为用来apschedule的定时任务后，只要在后台运行，就一直不会挂。所以最终的命令是
~~~bash
python3 scheduler.py & 
~~~


## Linux 上安装Chromedriver
~~~bash
cd /home/dev
sudo wget ttps://chromedriver.storage.googleapis.com/2.35/chromedriver_linux64.zip
sudo apt install unzip   
sudo unzip chromedriver_linux64.zip
~~~
## 程序逻辑
1. scheduler.py 设定schedule，然后调用getNews
### 定期运行程序的
~~~Python
from apscheduler.schedulers.blocking  import BlockingScheduler

def bcpnp_ita_news():
    print('show some news')
    
scheduler = BlockingScheduler()
sched = BlockingScheduler()
sched.add_job(bcpnp_ita_news, 'cron', day_of_week='1',hour='8-20',minute='*/15')
sched.start()
~~~
### 用cron的方式，Every Tuesday from 08:00 to 20:00, get data every 15 minutes

2. getNews.py 网络抓取新闻和数据，返回数据字典，并提供news函数，返回组装好的news（中、英文两种）
3. sendNews.py 将getNews的返回值发送到不同的目的地
