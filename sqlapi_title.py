
import pymysql
# 创建数据库连接
from timestamp import timestamp

conn = pymysql.connect(host="localhost",port=3306,user="root",passwd="202899318",db="hocasion" )
#获取一个游标对象
cursor=conn.cursor()
def insert_title(aid,catid,title,author,summary):
    try:
        sql="insert into dz_portal_article_title(aid,catid,uid,username,title,author,summary,contents,allowcomment,tag,dateline) " \
            "values(%s,%s,1,'Hocassian',%s,%s,%s,1,1,1,%s)"
        param=(aid,catid,title,author,summary,timestamp())
        cursor.execute(sql,param)
        conn.commit()
        print("插入数据成功")
    except:
        conn.rollback()
        print("插入数据失败")
def selectmax():
    sql = "select max(aid) from dz_portal_article_count"
    cursor.execute(sql)
    rest = cursor.fetchone()
    return  rest[0]
