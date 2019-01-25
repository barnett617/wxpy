import pymysql
import conf

db = pymysql.connect(conf.db_host, conf.db_user, conf.db_pass, conf.db_database)
cursor = db.cursor()
cursor.execute("SELECT VERSION()")
data = cursor.fetchone()
print("Database version : %s " % data)


def insert_msg(msg_content='', msg_type='', msg_sender='', msg_from=''):
    sql = "INSERT INTO msg(content, type, sender, msg_from) VALUES (%s, %s, %s, %s)" % (
        repr(msg_content), repr(msg_type), repr(msg_sender), repr(msg_from))
    print(sql)
    try:
        # 执行sql语句
        cursor.execute(sql)
        # 执行sql语句
        db.commit()
    except Exception as e:
        print('Reason:', e)
        db.rollback()

    # 关闭数据库连接
    # db.close()