# 取得完数据后需要做的：
# 1. 扫描到的数据，跟excel里面最新的比较，如果是更新，把最新数据添加到现有excel中去
# 2. 统计当年ITA总数，打印： 总数，已经用完名额（regular的和Tech Pilot），剩余名额
# 3. 图形化表示数据走向
# 4. 计算出各项目、历史最高分，最低分，平均分
# 5. 计算出各项目、各个年份的最高分，最低分，和该年的平均分
# 6. 在客户算分的程序中，可以增加根据客户分数，估计可能性的内容： 1 该项目历史最高分 2. 当年最高分 3. 当年平均分 4. 当年最低分 5. 历史最低分 几个来估计ITA的可能性。

import pandas as pd 
from matplotlib import pyplot as plt
#from Datetime import Datetime
import re

# 画图
def plotTrends(xs,ys,titel,legend):
    for i in range(len(xs)):
        plt.plot(xs[i],ys[i])
    plt.title(titel)
    plt.xlabel("Date")
    plt.ylabel("Points")
    plt.legend(legend)
    plt.show()
# 历史分析：所有年份
def allYearAnalysis():
    for i, row in data.iterrows(): # 日期就去除月份即可
    data.loc[i,'Date']=re.match(r'^\d{2}(\d{2}-\d{2})-\d{2}$',data.loc[i,'Date']).group(1)
    x_sw=data.Date[data.TechPilot==False]
    y_sw=data.SkillWorker[data.TechPilot==False]
    x_ig=data.Date[data.TechPilot==False]
    y_ig=data.InternationalGraduate[data.TechPilot==False]
    x_elss=data.Date[data.TechPilot==False]
    y_elss=data.EntryLevel[data.TechPilot==False]
    x_eesw=data.Date[data.TechPilot==False]
    y_eesw=data.EESkillWorker[data.TechPilot==False]
    x_eeig=data.Date[data.TechPilot==False]
    y_eeig=data.EEInternationalGraduate[data.TechPilot==False]

    xs=[x_sw,x_ig,x_elss,x_eesw,x_eeig]
    ys=[y_sw,y_ig,y_elss,y_eesw,y_eeig]

    #plotTrends(xs,ys,"2017-2020 BCPNP ITA Points",["Skill Worker","International Graduate","Entre Level/Semi-Skill","EE-Skill Worker","EE-International Graduate"])

    count,mean,std,min,q,average,q3,max=y_sw.describe()
    all_time_sw_summary=[count,min,average,max]

    count,mean,std,min,q,average,q3,max=y_ig.describe()
    all_time_ig_summary=[count,min,average,max]

    count,mean,std,min,q,average,q3,max=y_elss.describe()
    all_time_elss_summary=[count,min,average,max]

    count,mean,std,min,q,average,q3,max=y_eesw.describe()
    all_time_eesw_summary=[count,min,average,max]

    count,mean,std,min,q,average,q3,max=y_eeig.describe()
    all_time_eeig_summary=[count,min,average,max]

    # print(all_time_sw_summary)
    # print(all_time_ig_summary)
    # print(all_time_elss_summary)
    # print(all_time_eesw_summary)
    # print(all_time_eeig_summary)

    # xs=[data['Date'],data1['Date'],data2['Date'],data3['Date']]
    # cat=['Skill Worker','International Graduate','Entry Level','EE-Skill Worker','EE-International Graduate']
    # for i in range(len(cat)):
    #     ys=[data[cat[i]],data1[cat[i]],data2[cat[i]],data3[cat[i]]]
    #     title="BCPNP "+cat[i]+" ITA Points Trend"
    #     plotTrends(xs,ys,title)
    #     # Number of invitation trends
        
    # ys=[data['Invitation number'],data1['Invitation number'],data2['Invitation number'],data3['Invitation number']]
    # plotTrends(xs,ys,"Invitation Number Distributions")



    # Tech Pilot
    x_sw=data.Date[data.TechPilot==True]
    y_sw=data.SkillWorker[data.TechPilot==True]
    x_ig=data.Date[data.TechPilot==True]
    y_ig=data.InternationalGraduate[data.TechPilot==True]
    x_elss=data.Date[data.TechPilot==True]
    y_elss=data.EntryLevel[data.TechPilot==True]
    x_eesw=data.Date[data.TechPilot==True]
    y_eesw=data.EESkillWorker[data.TechPilot==True]
    x_eeig=data.Date[data.TechPilot==True]
    y_eeig=data.EEInternationalGraduate[data.TechPilot==True]

    xs=[x_sw,x_ig,x_elss,x_eesw,x_eeig]
    ys=[y_sw,y_ig,y_elss,y_eesw,y_eeig]

    #plotTrends(xs,ys,"2017-2020 BCPNP ITA Points (Tech Pilot)",["Skill Worker","International Graduate","Entre Level/Semi-Skill","EE-Skill Worker","EE-International Graduate"])

    count,mean,std,min,q,average,q3,max=y_sw.describe()
    all_time_sw_summary=[count,min,average,max]

    count,mean,std,min,q,average,q3,max=y_ig.describe()
    all_time_ig_summary=[count,min,average,max]

    count,mean,std,min,q,average,q3,max=y_elss.describe()
    all_time_elss_summary=[count,min,average,max]

    count,mean,std,min,q,average,q3,max=y_eesw.describe()
    all_time_eesw_summary=[count,min,average,max]

    count,mean,std,min,q,average,q3,max=y_eeig.describe()
    all_time_eeig_summary=[count,min,average,max]

    # print(all_time_sw_summary)
    # print(all_time_ig_summary)
    # print(all_time_elss_summary)
    # print(all_time_eesw_summary)
    # print(all_time_eeig_summary)


# 逐年分析
def yearlyInvitationSum(df,year):
    start=year+"-01-01"
    end=year+"-12-31"
    return df[(data.Date>=start)&(df.Date<=end)].loc[:,'InvitationNumber'].sum()

def yearlyAnalysis(data,year):

    data=data[(data.Date>year) & (data.Date<str(int(year)+1))]
    for i, row in data.iterrows(): # 日期就去除月份即可
        data.loc[i,'Date']=re.match(r'^\d{2}(\d{2}-\d{2})-\d{2}$',data.loc[i,'Date']).group(1)
    getPicData(False,data,year) # get Tech Pilot data OR NOT

def getPicData(is_tech_pilot,data,year):
    x_sw=data.Date[data.TechPilot==is_tech_pilot]
    y_sw=data.SkillWorker[data.TechPilot==is_tech_pilot]
    x_ig=data.Date[data.TechPilot==is_tech_pilot]
    y_ig=data.InternationalGraduate[data.TechPilot==is_tech_pilot]
    x_elss=data.Date[data.TechPilot==is_tech_pilot]
    y_elss=data.EntryLevel[data.TechPilot==is_tech_pilot]
    x_eesw=data.Date[data.TechPilot==is_tech_pilot]
    y_eesw=data.EESkillWorker[data.TechPilot==is_tech_pilot]
    x_eeig=data.Date[data.TechPilot==is_tech_pilot]
    y_eeig=data.EEInternationalGraduate[data.TechPilot==is_tech_pilot]

    xs=[x_sw,x_ig,x_elss,x_eesw,x_eeig]
    ys=[y_sw,y_ig,y_elss,y_eesw,y_eeig]

    title=year+" BCPNP ITA Points (Tech Pilot)" if is_tech_pilot else year+" BCPNP ITA Points (Non Tech Pilot)"
    plotTrends(xs,ys,title,["Skill Worker","International Graduate","Entre Level/Semi-Skill","EE-Skill Worker","EE-International Graduate"])

    count,mean,std,min,q,average,q3,max=y_sw.describe()
    all_time_sw_summary=[count,min,average,max]

    count,mean,std,min,q,average,q3,max=y_ig.describe()
    all_time_ig_summary=[count,min,average,max]

    count,mean,std,min,q,average,q3,max=y_elss.describe()
    all_time_elss_summary=[count,min,average,max]

    count,mean,std,min,q,average,q3,max=y_eesw.describe()
    all_time_eesw_summary=[count,min,average,max]

    count,mean,std,min,q,average,q3,max=y_eeig.describe()
    all_time_eeig_summary=[count,min,average,max]

    # print_it(all_time_sw_summary)
    # print_it(all_time_ig_summary)
    # print_it(all_time_elss_summary)
    # print_it(all_time_eesw_summary)
    # print_it(all_time_eeig_summary)

    count=yearlyInvitationSum(data,year)
    print(count)

def print_it(l):
    line=str(l[0])+' & '+str(l[1])+' & '+str(l[2])+' & '+str(l[3])+' \\'
    print(line)


# 总表：2017年到2020年
# 1. 所有数据走向
# 2. 各项目最高分，最低分，平均分列表


data=pd.read_excel('itas.xlsx')
for year in ['2020','2019','2018']:
    yearlyAnalysis(data,year)








