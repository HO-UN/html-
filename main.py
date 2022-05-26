from sqlapi_content import insert_content
from sqlapi_count import insert_count
from sqlapi_title import insert_title, selectmax
import os

file_path = "F:\download\爬虫文章合集(2019.10.23)\杂谈博文归档\团子ACGN集散地\团子ACGN集散地"
file_names = os.listdir(file_path)
# dirname = os.path.dirname(file_path) #上一级目录
basename = os.path.basename(file_path)  # 当前所打开文件夹的名字
indexid = selectmax()+1  # 数据库最后一个id
for i in range(0,len(file_names)):
    with open(os.path.join(file_path, file_names[i]), 'r', encoding='utf-8') as f:
        txt = f.read()
    index = i + indexid
    try:
        insert_content(index, index, txt)
        insert_count(index, 6)
        insert_title(index, 6, file_names[i].strip('.html'), basename, " ")  # catid,title,author,summary
        f.close()
    except:
        print("有问题")
