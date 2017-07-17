#!/usr/bin/env python
# coding=utf-8
import codecs  
   
def ReadFile(filePath,encoding):  
    with codecs.open(filePath,"r",encoding) as f:  
        return f.read()  
def WriteFile(filePath,u,encoding):  
    with codecs.open(filePath,"w",encoding) as f:  
        f.write(u)  
''''' 
定义GBK_2_UTF8方法，用于转换文件存储编码 
'''  
def GBK_2_UTF8(src,dst):  
    content = ReadFile(src,encoding='gbk')  
    WriteFile(dst,content,encoding='utf_8')              
''''' 
qyx.csv文件使用GBK编码存储，现在将其转为UTF_8存储 
'''  
src = '2015_1.csv'  
dst = '2015_1_utf8.csv'  
GBK_2_UTF8(src,dst) 
