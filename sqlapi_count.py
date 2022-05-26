from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.dialects.mysql import \
    BIGINT, BINARY, BIT, BLOB, BOOLEAN, CHAR, DATE, \
    DATETIME, DECIMAL, DECIMAL, DOUBLE, ENUM, FLOAT, INTEGER, \
    LONGBLOB, LONGTEXT, MEDIUMBLOB, MEDIUMINT, MEDIUMTEXT, NCHAR, \
    NUMERIC, NVARCHAR, REAL, SET, SMALLINT, TEXT, TIME, TIMESTAMP, \
    TINYBLOB, TINYINT, TINYTEXT, VARBINARY, VARCHAR, YEAR

# 声明映射
from timestamp import timestamp

Base = declarative_base()
# 创建Session
Session = sessionmaker()
# 创建连接引擎
engine = create_engine('mysql+pymysql://root:202899318@localhost:3306/hocasion?charset=utf8', echo=True)
Session.configure(bind=engine)
# 构造新的Session
session = Session()
# 定义表对象
class Count(Base):
    # 表的名字
    __tablename__ = 'dz_portal_article_count'
    aid = Column('aid', MEDIUMINT, primary_key=True, nullable=False,autoincrement=True)
    catid = Column('catid', MEDIUMINT, nullable=False)  # 博文类型的id
    # 定义__repr__函数，返回一个可以用来表示对象的可打印字符串
    def __repr__(self):
        return self.title


def insert_count(aid,catid):
    try:
        course_obj2 = Count(aid=aid,catid=catid)
        # 添加对象
        session.add(course_obj2)
        # 事务提交,如果不提交事务，则处于待定状态，数据未写入数据库
        session.commit()
        print("插入数据成功")
    except:
        session.rollback()
        print("插入数据失败")
