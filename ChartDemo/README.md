## 说明

使用Django结合pyecharts做一个物联网的设备监测页面，可以实时的将各种参数以图像的形式显示

关于在Django中嵌入图表的方法，请参考[在Django中嵌入图表](https://chunar5354.github.io/2020/07/02/django-pyecharts.html)

## 运行

可以直接运行

```
python manage.py runserver 0:9090
```

然后登录`localhost:9090`就可以访问页面

## 测试数据

因为要从MySQL数据库中取出数据来显示，可以通过`into_db_test.py`向数据库中添加测试数据
