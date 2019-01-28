import pymysql
from secret import conf

db = None
cursor = None

def getDBConnection():
    global db  # 声明db是全局变量
    global cursor
    db = pymysql.connect(conf.db_host, conf.db_user, conf.db_pass, conf.db_database)
    cursor = db.cursor()
    cursor.execute("SELECT VERSION()")
    data = cursor.fetchone()
    print("Database version : %s " % data)

def releaseDBConnection():
    db.close()

def insert_msg(msg_content='', msg_type='', msg_sender='', msg_from='', create_time='', receive_time=''):
    sql = "INSERT INTO msg(content, type, sender, msg_from, create_time, receive_time) VALUES (%s, %s, %s, %s, '%s', '%s')" % (
        str(repr(msg_content)), repr(msg_type), repr(msg_sender), repr(msg_from), str(create_time), str(receive_time)
    )
    print(sql)
    try:
        # 执行sql语句
        cursor.execute(sql)
        # 执行sql语句
        db.commit()
    except Exception as e:
        getDBConnection()
        print('Reason:', e)
        db.rollback()
