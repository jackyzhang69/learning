import itchat
from tuling import get_response

def greeting():
    return '您好，需要我为你做点什么?'


def visa():
    return "你要visa，是吧"

reply={
    "greetings":greeting,
    "visa":visa

}


def get_catogry(msg):
    categories=[
        ['greetings','hi hello 你好 您好 好久不见 在吗'],
        ['visa','签证 探亲 旅游 留学 工作']
    ]
    catogry=''
    for cg in categories:
        print(cg)
        if msg['Text'] in cg[1]:
            catogry= cg[0]
            break
        else:
            catogry= 'Other'
    print(catogry)
    return catogry


@itchat.msg_register('Text')
def text_reply(msg):
    if get_catogry(msg)=='Other':
        other_msg=" 主人现在不在，我只是个机器人，不太明白你要做什么。我会提醒主人，回来时候看您的留言。"
        return get_response(msg['Text']) or u'收到：' + msg['Text']+other_msg
    else:
        return reply.get(get_catogry(msg))()

itchat.auto_login(True, enableCmdQR=True)
itchat.run()

