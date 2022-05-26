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
# 定义表对象
class Content(Base):
    # 表的名字
    __tablename__ = 'dz_portal_article_content'
    cid = Column('cid', Integer, primary_key=True, nullable=False)   # content的id
    aid = Column('aid', MEDIUMINT, nullable=False, autoincrement=True)  # aid为title的id
    id = Column('id', Integer, default=0, nullable=False)
    content = Column('content', Integer, default=0, nullable=False)
    pageorder = Column('pageorder', LONGTEXT, default=1, nullable=False)
    dateline = Column('dateline',Integer, nullable=False)  # 时间戳
    # 定义__repr__函数，返回一个可以用来表示对象的可打印字符串
    def __repr__(self):
        return self.title
def insert_content(cid,aid,content):
    try:
        course_obj = Content(cid=cid,aid=aid,content=content, dateline=timestamp())
        # 添加对象
        session.add(course_obj)
        # 事务提交,如果不提交事务，则处于待定状态，数据未写入数据库
        session.commit()
        print("插入数据成功")
    except:
        session.rollback()
        print("插入数据失败")
