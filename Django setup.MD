1. install Django
pip install django          # 安装
python -m django --version  # 查看版本 2.1 higher

2. Create new project
django-admin  # 显示Django的应用程序
django-admin startproject  django-project #启动一个项目django-project

3. Run server
python manage.py runserver  # 启动服务

4. Start an application
python manage.py startapp blog  # 创建一个blog的应用

5. urls  #路由设置
    在项目目录下的urls.py里面 设置

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('noc/', views.index,name='index'), # 可以直接设置一个路径指向
        path('case/', include('case.urls'))     # 也可以设置包含一个应用的子路进设置。case是一个应用，里面也带有一个urls.py的文件
    ]

    # 这是case里面的usrls.py文件
    urlpatterns = [
        path('', views.caseIndex,name='case_index') # views是一个应用，控制层，caseIndex是一个函数 name是这个路径的名字
    ]

6. 在项目目录的setting.py里面注册apps
    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        "noc.apps.NocConfig",   # 记得在这里注册apps
        "case.apps.CaseConfig",
    ]
    在每个app目录下，有一个apps.py， 在里面配置apps
    class CaseConfig(AppConfig):
        name = 'case'
7. 函数调用渲染template
    clients = [
    {
        'Name': 'Jacky Zhang',
        "Age": 51,
        "Sex": 'Male'
    },
    {
        'Name': 'May Li',
        "Age": 48,
        "Sex": 'Female'
    }
    ]
    context = {                 # 传字典到template里面去做渲染
        'clients': clients
    }
    def case_index(request):
        return render(request, 'case/index.html', context) # 第二个参数是模板网页，第三个是变量传递进去渲染网页


8. Template 语言                      # {% %} 表示是template language内容
  {% for client in clients %}       # for endfor 循环
        <h1>{{ client.Name }}</h1>  # 引用变量 {{ }}
        <p>{{ client.Age }}</p>
        <p>{{ client.Sex }}</p>
    {% endfor %}

9. Base template
    在base template里面处理好所有重复的东西，然后在<body></body>之间插入一段：
    <body>
    {% block content %} {% endblock %}
    </body>
    在子页面中，可以overwrite block content这部分
    {% extends "case/base.html" %}
    {% block content %}

        {% for i in ranges %}
            <p>I love Dan: {{ i }}</p>
        {% endfor %}

    {% endblock content %}

10. bootstrap 设计网站的免费资源
