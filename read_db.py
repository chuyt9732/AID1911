import pymysql
# 链接数据库
db = pymysql.connect(host='localhost',
                     port=3306,user='root',
                     password="123456",
                     database='information_stu',
                     charset='utf8')
# 生成游标对象(操作数据库,执行SQL语句,获取结果)
cur = db.cursor()
# 读操作
sql='select name,age,score from cls;'
cur.execute(sql)
# 获取结果方法1
# for i in cur:
#     print(i)
# 获取结果方法2
# one_row=cur.fetchone()
# print(one_row)
# 获取结果方法3
# many_row=cur.fetchmany(3)
# print(many_row)
all_row=cur.fetchall()
print(all_row)
# 关闭游标和数据库链接
cur.close()
db.close()