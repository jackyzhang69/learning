目录结构
immlib
notes: 项目说明文件
models: 模型层。 applicant 等类定义、数据转换、模型函数定义等
bcPoints: BCPNP 算分
... 其他各省的算分
ee: ee 算分，包含 fsw 的 67 分算分
utils: 基础模块

软件工程分层
Web 界面层： template
逻辑调度层： views。 接收界面层数据，分发到数据转换，并从数据转换层得到返回数据，发送到界面层。
模型和数据转换层： models 转换 views 传过来的数据，调用基础库中的 API，得到分数，以及逻辑（这个目前尚未完成）
基础层：immlib. 可以考虑做成外部包 package. 主要，数据转换层，从某种意义就是数据层了。

Applicant 类是核心数据，所有的后续应用都是根据这个数据来的。 在实际应用中，通过 Web 页面接受数据，保存到数据库

# 具体做各种计算时，用 Applicant 里的方法，具体提供该计算所需要的变量（传入一个具体项目的 applicant 对象），然后返回计算数据。 可能是分数，也有可能是方案集合

# 各种项目的分数计算，方案规划由最底层的数据和逻辑计算包完成

# 在 FSW 67 分的算法中，education 有这些表述和分数

# edu_level_points_table = {

# 'Doctor': 25,

# 'Master': 23,

# 'Professional': 23,

# # professional degree needed to practice in a licensed profession. https://www.canada.ca/en/immigration-refugees-citizenship/corporate/publications-manuals/operational-bulletins-manuals/permanent-residence/economic-classes/federal-skilled-workers/selection-criteria-education.html#after

# 'Two more post-secondary': 22, # Two or more post-secondary, at least one is 3 years more

# '3-year post-secondary': 21,

# '2-year post-secondary': 19,

# '1-year post-secondary': 15,

# 'Secondary': 5

# 在 BCPNP 中，education 有这些表述和分数

<!-- # education_points = {

# 'doctor': 17,

# 'master': 17,

# 'postgraduate': 11,

# 'bachelor': 11,

# 'trade diploma': 11,

# 'associate degree': 4,

# 'non-trade diploma': 2,

# 'secondary': 0

# } -->

# # 创建教育经历类,对象是一个 list

# class Education(Model):

# start_date = models.DateTimeField('Start date')

# end_date = models.DateTimeField('End date')

# name_of_institution = models.CharField(max_length=120)

#

# class Language(Model):

# reading=models.FloatField()

# writing = models.FloatField()

# speaking = models.FloatField()

# listening = models.FloatField()

# format=models.Choices() # IELTS, CELPIP,TEF, TCF

# test_date=models.DateTimeField('Test date') #考试日期

# admin_date = models.DateTimeField('Admin date') #发证日期

# test_number=models.CharField(max_length=40) #号码

#

# # 创建工作经历类

# # 创建居住地址类 （这个如果后续做自动处理 PR 申请填表时需要用）

# # 创建一个 Person 基类，定义基本属性

```Python
class Person():
     name = models.CharField(max_length=12)
     sex = (
         (0, 'Male'),
         (1, 'Female'),
     )
     DOB=models.DateTimeField('Date of Birth')
#  工作经历中，要能算出来NOC类别的工作年限，NOC Level
```

<!-- 1 操作对象的属性： hasattr(obj,'attr'), setattr(obj,'attr'),getattr(obj,'attr') -->

使用判断一个对象是否有某种属性，可以作为控制的一个方式 比如：hasattr(obj,'pnp'))
scenario1: 界面层获取一个人考虑申请的不同项目，放到一个 post 传输给 view 层，要判断一个人是否考虑 pnp，可以通过这个来判断，如果有，再取出 pnp 的值，
比如，['BC', 'SK'], 然后再分别去计算分数和做逻辑判断。

2. 模型考虑 （表结构）
   Person： name,dob,sex。 可以直接获取年龄 obj.age
   Application: category, stream # 这个是否需要单列，有待考虑
   Solution: person_id (外键）,application (外键），factors (language,education,work_experience,age,job offer,relative,spouse,adaptability)

3. Education
   定义实例（start_date, end_date, program_years, level, study_field, name_of_institution, city, province,
   country）
   self.is_Canadian：bool
   def in_province(self, province):
   return True if self.province == province else False
   def **str**(self): 返回一个名称
   def **call**(self, \*args, \*\*kwargs): 返回一个介绍

2020-04-21
后续考虑问题：

1. 可以考虑系统能够自动判断哪个作为第一语言比较合理，分数会更高，考虑到法语有特别优惠方面，需要研究政策
2. 需要考虑语言 工作经验 数组的问题，如何自动计算，而不仅仅是在类里面的那几个。 自动计算多个学历，工作经验，归类，算时间等
3. 教育在不同的地方，有不同的定义，需要增加变量 判断

2020-04-24:
目前当午之急，是做两个东西：

1. 算分和报告 (这个就是移民顾问用，可以是速算，输入最简单的几个变量，得出结论。 跟后续要做的客户综合评价是 2 套东西。）
2. 客户案子跟踪

后续可以做：

1. LMIA： assessment, 文案处理,final review
2. BCPNP: assessment, 文案处理,final review

