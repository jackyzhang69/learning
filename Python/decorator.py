import functools

def log(func):
    @functools.wraps(func)
    def wrapper(*args,**kw):
        print('call %s()'%func.__name__)
        return func(*args,**kw)
    return wrapper

@log
def now():
    print("hi")
    print(now.__name__)


now()

# Using @property decorator
# 用属性的方法调用函数

class Student():
    def __init__(self,name,score):
        self.score=score
        self.name=name

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self,value):
        self._score=value

    def __str__(self):
        return 'Student object (name:%s)' %self.name
    

s=Student('jacky',80)

print(s.score)
s.score=90
print(s.score)

print(s)

    