'''使用py下载的11种方法'''
# 1.使用requests
'''使用requests的get访问URL, 将结果存储到'myfile'的变量中，将变量内容写入文件'''
# import requests
# url = 'https://www.python.org/static/img/python-logo@2x.png'
# myfile = requests.get(url)
# open('G:\工作导图\py脚本\pyimage.png', 'wb').write(myfile.content)

# 2.使用wget
'''
使用wget模块从一个URL下载文件，需使用pip安装wget模块，
URL和路径(图像存储在其中)被传递给wget模块的download方法
'''
# import wget
# url = 'https://www.python.org/static/img/python-logo@2x.png'
# wget.download(url, 'G:\工作导图\py脚本\pyimage.png')

# 3.下载重定向文件
'''
使用requests从URL下载文件，
该URL会被重定向到另一个带有一个.pdf的URL
* 在get方法中，将allow_redirects设置为True，允许URL中的重定向，
且将重定向后的内容分配给变量myfile
'''
# import requests
# url = 'https://readhedocs.org/projects/python-guide/downloads/pdf/latest/'
# myfile = requests.get(url, allow_redirects=True)
# open('G:\工作导图\py脚本\pypdf.pdf', 'wb').write(myfile.content)

## 4.分块下载大文件
'''
1) 使用requests的get访问URL，把stream属性设置为True;
2) 当前目录创建一个PythonBook.pdf文件，打开并写入
3) 指定每次要下载的块大小，设置为1024字节，
4) 遍历每个块，在文件中写入这些块，直到块结束
'''
# import requests
#
# url = 'https://www.python.org/static/img/python-logo@2x.png'
# myfile = requests.get(url, stream=True)
# open('G:\工作导图\py脚本\pyimage.png', 'wb').write(myfile.content)

# 5.下载多个文件(并行/批量下载)
'''
1) 导入os和time：检查下载文件需要多少时间;ThreadPool：允许使用池运行多个线程/进程
2) 创建一个简单函数，将响应分块发送到一个文件
3) 将URL传递给requests.get
4) 打开文件(URL中指定的路径)并写入页面内容
'''
import os
import requests
from time import time
from multiprocessing.pool import ThreadPool


def url_response(url):
    path, url = url
    r = requests.get(url, stream=True)
    with open(path, 'wb') as f:
        for ch in r:
            f.write(ch)

# URL二维数组,指定要下载的页面路径和URL
urls = [
    ("Event1", "https://www.python.org/events/python-events/805/"),
    ("Event2", "https://www.python.org/events/python-events/801/"),
    ("Event3", "https://www.python.org/events/python-events/798/"),
    ("Event4", "https://www.python.org/events/python-events/807/"),
    ("Event5", "https://www.python.org/events/python-events/806/"),
    ("Event6", "https://www.python.org/events/python-events/804/"),
    ("Event7", "https://www.python.org/events/python-events/757/"),
    ("Event8", "https://www.python.org/events/python-events/816/")
]
















