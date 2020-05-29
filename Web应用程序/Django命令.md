####1.创建Django项目，在虚拟环境中运行
```django-admin startproject learning_log .```

####2.创建数据库
```python3 manage.py migrate```

####3.查看项目
```python3 manage.py runserver```

####4.创建应用程序
```python3 manage.py startapp learning_logs```

####5.激活模型
***每当需要修改“学习笔记”管理的数据时，都采取如下三个步骤：修改models.py；
对learning_logs调用makemigrations；让Django迁移项目。***
```
# 命令makemigrations让Django确定该如何修改数据库
python3 manage.py makemigrations learning_logs

# 让Django替我们修改数据库库
python3 manage.py migrate
```

####6.Django管理网站
```
# 1.创建超级用户：
python3 manage.py createsuperuser

# 2.向管理网站注册模型
# admin.py：

from django.contrib import admin

# Register your models here.
from learning_logs.models import Topic

admin.site.register(Topic)

```

####7.Django shell
```
python3 manage.py shell
from learning_logs.models import Topic
Topic.objects.all()

(venv)  ~/Python/Code/PythonCrashCourse/Web应用程序/ [master+*] python3 manage.py shell                 
Python 3.8.2 (default, Apr 27 2020, 15:53:34) 
[GCC 9.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> from learning_logs.models import Topic
>>> Topic.objects.all()
<QuerySet [<Topic: Chess>, <Topic: Rock Climbing>]>
>>> topics = Topic.objects.all()
>>> for topic in topics:
...     print(topic.id, topic)
... 
1 Chess
2 Rock Climbing
>>> t = Topic.objects.get(id=1)
>>> t.text
'Chess'
>>> t.date_added
datetime.datetime(2020, 5, 29, 1, 53, 40, 954355, tzinfo=<UTC>)
>>> t.entry_set.all()
<QuerySet [<Entry: The opening is the first part of the game, roughly...>, <Entry: In the opening phase of the game, it's important t...>]>

```
