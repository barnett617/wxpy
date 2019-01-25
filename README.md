# wxpy

## Desc

my wxpy robot implements of wxpy

## Feature

- collect the wechat messages
- insert the messages collected into mysql database
- simply analysis messages and reply automatically

## How to use

1. git clone https://github.com/barnett617/wxpy
2. open the project with your IDE (like PyCharm or others)
3. have a your own mysql database
4. create a file named `conf.py`
5. input your infomation about your database as the following format
6. run the script `db.py` to build a table for message storage
7. run the script `main.py` to start your robot
8. use your wechat app to scan the qrcode on the computer's screen
9. done

```buildoutcfg
# db_host = 'xx.xx.xx.xx'
# db_user = 'xx'
# db_pass = 'xx'
# db_database = 'xx'
```

## Warning

1. if your computer sleep, the process of the robot will logout, you should manually restart the program by running `main.py`
2. the database io is not strong enough to work very well to store your messages, I'm working on it to get it better.

## Error Record

### [PYTHON 使用 MYSQL 存储 EMOJI 表情](https://kylingit.com/blog/python-%E4%BD%BF%E7%94%A8-mysql-%E5%AD%98%E5%82%A8-emoji-%E8%A1%A8%E6%83%85/)

#### 原因

在 mysql 中 utf8 的字段只能存储 1 至 3 字节的字符，而 emoji 表情是使用 4 字节字符来表示的，这就导致 Incorrect string value 错误

#### 解决方案

解决方案采取将数据库、数据表字符集设为utf8mb4，因为需要保存emoji表情，utf8mb4是utf8的超集

## TODO

- [ ] analysis more smartly
- [ ] deploy the project on the server with a daemon to hold it on
- [ ] receive file message like image, audio, video etc. and save