import pymysql
# 链接数据库
db = pymysql.connect(host='localhost',
                     port=3306,user='root',
                     password="123456",
                     database='information_stu',
                     charset='utf8')
# 生成游标对象(操作数据库,执行SQL语句,获取结果)
cur = db.cursor()
# 执行各种SQL操作
while True:
    name=input("姓名:")
    sql="select name,age,score from cls where name='%s';"%name
    cur.execute(sql)
    all_row=cur.fetchall()
    print(all_row)
# 关闭游标和数据库链接
cur.close()
db.close()