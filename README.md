## 笔墨世间 后端服务

Based on Django, Python3.12.

## Ready to run

```shell
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver 
```

## Check Health

```shell
curl -X GET http://127.0.0.1:8000/tips/hello
```

## Questions

1. 每个Item叫什么
2. 有哪些属性
3. 有哪些功能（操作）