import pymysql
# 链接数据库
db = pymysql.connect(host='localhost',
                     port=3306,user='root',
                     password="123456",
                     database='information_stu',
                     charset='utf8')
# 生成游标对象(操作数据库,执行SQL语句,获取结果)
cur = db.cursor()
# 写操作
# sql="insert into cls (name,age,score)values('于大建',22,55);"
# cur.execute(sql)
# db.commit()
sql="update cls set sex='m' where name='于大建';"
cur.execute(sql)
db.commit()
# 关闭游标和数据库链接
cur.close()
db.close()