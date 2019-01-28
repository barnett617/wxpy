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

## deploy

0. install required package `yum install bzip2`
1. download python on the server `wget https://repo.continuum.io/archive/Anaconda3-4.3.1-Linux-x86_64.sh`
2. install python `sh Anaconda3-4.3.1-Linux-x86_64.sh`
3. press `enter` to read the licence
4. input `q` to quit the licence
5. input `yes` to go on
6. input `/usr/local/anaconda3` to specific install path
7. done
8. relogin your server and type `python` to start to use

## Warning

1. if your computer sleep, the process of the robot will logout, you should manually restart the program by running `main.py`
2. the database io is not strong enough to work very well to store your messages, I'm working on it to get it better.

## Error Record

### [PYTHON 使用 MYSQL 存储 EMOJI 表情](https://kylingit.com/blog/python-%E4%BD%BF%E7%94%A8-mysql-%E5%AD%98%E5%82%A8-emoji-%E8%A1%A8%E6%83%85/)

#### 原因

在 mysql 中 utf8 的字段只能存储 1 至 3 字节的字符，而 emoji 表情是使用 4 字节字符来表示的，这就导致 Incorrect string value 错误

#### 解决方案

解决方案采取将`数据库`、`数据表`、`数据表字段`字符集均设为utf8mb4，因为需要保存emoji表情，utf8mb4是utf8的超集

若数据库、数据表已建为utf8，需要修改数据库字符集、数据表字符集和需要存储emoji表情的字段的字符集为utf8mb4

以下为修改指定字段的sql语句

```SQL
alter table msg change column `content` `content`  varchar(255) CHARACTER set 'utf8mb4'
```

## TODO

- [ ] analysis more smartly
- [ ] deploy the project on the server with a daemon to hold it on
- [x] receive and save picture message
- [ ] receive and save audio message 
- [ ] receive and save video message
- [ ] 标准emoji表情无法保存，提示`1366, "Incorrect string value: '\\xF0\\x9F\\x98\\x82\\xE5\\x95...' for column 'content' at row 1"``