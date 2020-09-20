## 说明

在Django网页应用中实现发送电子邮件的功能

关于代码的详细解析请看[这里](https://chunar5354.github.io/2020/09/20/django-email.html)

## 运行

首先需要将settings.py中的

```python
EMAIL_HOST_USER = '123456@qq.com'
EMAIL_HOST_PASSWORD = 'xxxxxxxxxxxxxxxx'
```

部分改成自己邮箱账号的授权码

并在views.py中指定发件邮箱和收件邮箱


运行

```
python manage.py runserver 0:9090
```

在浏览器中输入`localhost:9090`就可以访问页面，在主页中点击链接即可发送邮件
