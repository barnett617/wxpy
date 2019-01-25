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

## TODO

- analysis more smartly