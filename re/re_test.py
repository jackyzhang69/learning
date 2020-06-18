import re

# https://www.liaoxuefeng.com/wiki/1016959663602400/1017639890281664

def is_valid_email(str):
    return True if re.match(r'^[a-zA-Z0-9\-]+\@[a-zA-Z]+\.[a-zA-Z]+',str) else False



print(is_valid_email('someone@gmail.com'))
print(is_valid_email('111@gmail.com'))
print(is_valid_email('mr-bob@example.com'))


def name_of_email(str):
    return re.match(r'\<([a-zA-Z\s]+)\>',str).groups()

print(name_of_email('<Tom Paris>'))

def name_of_email1(str):
    return re.match(r'([a-zA-Z]+\@[A-Za-z]+\.[A-Za-z]+)',str).groups()

print(name_of_email1('tom@voyager.org'))

def name_of_email2(str):
    return re.match(r'\<([a-zA-Z\s]+)\>\s+([a-zA-Z]+\@[A-Za-z]+\.[A-Za-z]+)',str).groups()[0]

print(name_of_email2('<Tom Paris> tom@voyager.org'))