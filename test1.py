import os
import re

file_path = "F:\download\爬虫文章合集(2019.10.23)\情感博文归档\浪迹情感微信公众号元数据\浪迹情感微信公众号元数据\浪迹情感\\1"
file_names = os.listdir(file_path)
os.chdir(file_path)
# dirname = os.path.dirname(file_path) #上一级目录
basename = os.path.basename(file_path)  # 当前所打开文件夹的名
files = os.listdir(file_path)   # 读入文件夹

for i in range(0,len(files)):
    with open(os.path.join(file_path, file_names[i]), 'r', encoding='utf-8') as f:

        txt = f.read()
    match = re.findall(r'<meta content="(.*?)" property="og:title"/>',txt)
    try:
        os.rename(file_names[i],match[0].replace("|",'')+r'.html')
    except:
        print('第{0}条数据处理失败'.format(i))
