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

####8.确定当前有哪些用户
```
(venv)  ~/Python/Code/PythonCrashCourse/Web应用程序/ [master+*] python3 manage.py shell
Python 3.8.2 (default, Apr 27 2020, 15:53:34) 
[GCC 9.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> from django.contrib.auth.models import User
>>> User.objects.all()
<QuerySet [<User: ll_admin>, <User: jack>, <User: tom>, <User: jerry>]>
>>> for user in User.objects.all():
...     print(user.username, user.id)
... 
ll_admin 1
jack 2
tom 3
jerry 4
```

####9.迁移数据库
```
(venv)  ~/Python/Code/PythonCrashCourse/Web应用程序/ [master+*] python3 manage.py makemigrations learning_logs
You are trying to add a non-nullable field 'owner' to topic without a default; we can't do that (the database needs something to populate existing rows).
Please select a fix:
 1) Provide a one-off default now (will be set on all existing rows with a null value for this column)
 2) Quit, and let me add a default in models.py
Select an option: 1  # 选择迁移到的对象
Please enter the default value now, as valid Python
The datetime and django.utils.timezone modules are available, so you can do e.g. timezone.now
Type 'exit' to exit this prompt
>>> 1
Migrations for 'learning_logs':
  learning_logs/migrations/0003_topic_owner.py
    - Add field owner to topic

# 执行迁移
(venv)  ~/Python/Code/PythonCrashCourse/Web应用程序/ [master+*] python3 manage.py migrate                     
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, learning_logs, sessions
Running migrations:
  Applying learning_logs.0003_topic_owner... OK

# 验证迁移是否符合预期
(venv)  ~/Python/Code/PythonCrashCourse/Web应用程序/ [master+*] python3 manage.py shell  
Python 3.8.2 (default, Apr 27 2020, 15:53:34) 
[GCC 9.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> from learning_logs.models import Topic
>>> for topic in Topic.objects.all():
...     print(topic, topic.owner)
... 
Chess ll_admin
Rock Climbing ll_admin

```

###创建包含包列表的文件 requirements.txt
```
pip3 freeze > requirements.txt
```
