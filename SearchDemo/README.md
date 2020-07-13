## 说明

使用Django框架搭建一个自己的搜索页面，原型是cleverprogrammer的一个教学程序，
可以查看原[Youtube视频](https://www.youtube.com/watch?v=JT80XhYJdBw&list=LLgaMfukkcUgygAjChfzYpzQ&index=6&t=27931s)

在他的基础上做了一些修改，可以搜索当当网的书籍以及哔哩哔哩的视频

## 运行

可以直接运行

```
python manage.py runserver 0:9090
```

然后登录`localhost:9090`就可以访问页面

## 注意事项

本项目使用的是MySQL数据库，如果在自己的设备上运行需要修改`SearchDemo/settings.py`中的`DATABASE`字段，改成自己的配置

还有MySQL默认的数据库和表是不支持中文的，有两种方法解决：

- 1.在创建数据库时指定字符集

```
create database db_name default charset=utf8;
```

- 2.修改现有的表格为UTF-8编码

```
alter table table_name convert to character set utf8;
```
