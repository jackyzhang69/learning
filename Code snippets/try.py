class Name(object):
    def __init__(self, name,group,tag):
        self.group=group
        self.tag=tag
        self.name=name

class Relative(object):
    def __init__(self,relation,province,group,tag):
        self.relation=relation
        self.province=province
        self.group=group
        self.tag=tag

class Applicant():
    pass


def main():
    app=Applicant()
    app.name=Name("Jacky Zhang",group=1,tag=['all'])
    # app.relative=Relative('sister','SK',group=2,tag=['SK','PEI'])

    print(dir(app))