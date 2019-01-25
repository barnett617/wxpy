import pymysql
import conf

db = pymysql.connect(conf.db_host, conf.db_user, conf.db_pass, conf.db_database)
cursor = db.cursor()
cursor.execute("SELECT VERSION()")
data = cursor.fetchone()
print ("Database version : %s " % data)

cursor.execute("DROP TABLE IF EXISTS msg")
sql = """CREATE TABLE msg (
         id int(11) not null AUTO_INCREMENT,
         content  CHAR(255),
         type  CHAR(255),
         sender CHAR(255),
         msg_from CHAR(255),
         PRIMARY KEY (`id`)
         ) ENGINE=InnoDB DEFAULT CHARSET=utf8"""

cursor.execute(sql)
db.close()