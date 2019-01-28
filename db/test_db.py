import pymysql
from secret import conf

# db_host = 'xx.xx.xx.xx'
# db_user = 'xx'
# db_pass = 'xx'
# db_database = 'xx'
db = pymysql.connect(conf.db_host, conf.db_user, conf.db_pass, conf.db_database)
cursor = db.cursor()
cursor.execute("SELECT VERSION()")
data = cursor.fetchone()
print ("Database version : %s " % data)

msg_content = "火箭"
msg_type = "Text"
msg_sender = '张三'

sql = "INSERT INTO msg(content, type, sender) VALUES (%s, %s, %s)" % (repr(msg_content), repr(msg_type), repr(msg_sender))
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
db.close()


