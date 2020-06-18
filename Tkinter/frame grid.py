from tkinter import *

root=Tk()
root.title("Frame test")

f1=Frame(root,relief=RAISED,borderwidth=5,padx=50,pady=30)
f1.grid(row=0,column=0,sticky='w')

f2=Frame(root,relief=RAISED,borderwidth=5,padx=80,pady=60)
f2.grid(row=0,column=1,sticky='w')

Label(f1,text="libpng warning: iCCP: cHRM chunk png warpng wpngpng warning: iCCP: cHRM chunk doe warning: iCCP: cHRM chunk doearning: iCCP: cHRM chunk doening: iCCP: cHRM chunk doedoes not match sRGB").pack()
Label(f2,text="所以 人员是：你女朋友父母png warning: iCCP: cHRM 是：你女朋友父是：你女朋友父是：你女朋友父是：你女朋友父chunk doe，你的妈妈和小弟弟。").pack()

f3=Frame(root,relief=RAISED,borderwidth=5)
f3.grid(row=1,column=0,columnspan=2,sticky='w')

Label(f3,text="阿斯蒂芬 爱是劳动女朋友父母png warning: iCCP: cHRM 是：你女朋友父是女朋友父母png warning: iCCP: cHRM 是：你女朋友父是女朋友父母png warning: iCCP: cHRM 是：你女朋友父是女朋友父母png warning: iCCP: cHRM 是：你女朋友父是女朋友父母png warning: iCCP: cHRM 是：你女朋友父是女朋友父母png warning: iCCP: cHRM 是：你女朋友父是女朋友父母png warning: iCCP: cHRM 是：你女朋友父是v女朋友父母png warning: iCCP: cHRM 是：你女朋友父是法 拉上代理费。").pack()

root.mainloop()

