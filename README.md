# 油田仪表智能识别系统

#### 介绍
本系统使用python开发，是一个django项目，主要功能包括多类型指针式仪表识别、文字识别、仪表模板管理等。仪表识别的过程为：使用OCR文字识别检测待测仪表图像的模板类型，读取模板图像和其对应的参数信息；然后进行模板匹配定位仪表位置，再获取指针角度以及计算仪表数值。

#### 软件架构
本系统使用python开发，是一个django项目，需要先搭建django环境，数据库中的表可以使用相应命令自动生成。本系统涉及到目标检测，所以需要有yolov5环境（自行安装）


#### 安装教程

（1）安装django

```
pip install django
```

（2）配置数据库相关操作，安装第三方模块

```
pip install mysqlclient
```

（3）自己先去MySQL创建一个数据库，配置数据库连接settings.py

```python
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }
 
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django_pj',  # 数据库名字
        'USER': 'root',
        'PASSWORD': '123456',
        'HOST': '127.0.0.1',  # 那台机器安装了MySQL
        'PORT': 3306,
    }
}
```

（4）数据库表信息在models.py文件中，执行命令自动创建数据库中的表

```
>>>python manage.py makemigrations
>>>python manage.py migrate
```

（5）启动，直接运行project_start.py即可



#### 使用说明

用户角色：用户和管理员，管理员和用户登录的界面不一样，管理员的权限更多，在注册时默认为用户

![1663558139937](/README.assets/1663558139937.png)



**用户一开始可以在数据库admin表中自己添加一个管理员账号**

**用户名：root，密码：123456（加密之后b2cb09feda40ad159c1a6c864363ae1f），role为2**

![1663558202737](/README.assets/1663558202737.png)

#### 系统页面

![1663558246853](/README.assets/1663558246853.png)

![1663558289000](/README.assets/1663558289000.png)



![1663558329101](/README.assets/1663558329101.png)

![1663558359363](/README.assets/1663558359363.png)



用户在添加模板信息时先上传模板，再点击生成模板库信息
