# 1. 安装虚拟环境的第三方包 virtualenv
~~~bash 
pip install virtualenv
~~~
# 2. 创建虚拟环境
cd 到存放虚拟环境光的地址
~~~bash
virtualenv ENV 
~~~
在当前目录下创建名为ENV的虚拟环境（如果第三方包virtualenv安装在python3下面，此时创建的虚拟环境就是基于python3的）

# 3. 激活/退出虚拟环境
~~~bash cd ~/ENV ~~~ 跳转到虚拟环境的文件夹

~~~ source bin/activate ~~~ 激活虚拟环境

~~~bash pip list ~~~ 查看当前虚拟环境下所安装的第三方库

~~~bash deactivate ~~~ 退出虚拟环境