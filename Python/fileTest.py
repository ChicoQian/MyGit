# -*- coding: utf-8 -*-
#
#读取方式
#f.readline() //读取一行
#f.readlines() //读取8000多字节左右的大小。其值大概等于io缓冲区的大小。
#迭代器遍历 //占用内存小
#iter_f = iter(f)
#for i in iter_f:
#    count += 1

# f = open("file.py",'w')
#f = open("file.py",'w+')##打开清空
f = open("file.py",'r+')##打开可写
#list_c = f.readlines(1)
#print list_c
#print len(list_c)
count =0
iter_f = iter(f)
for i in iter_f:
    print(i)
    print
    count += 1
##print iter_f.next
##next(iter_f)
print type(i)
print type(f)

##################################文件写##################################
#向文件中写入内容会先把内容写入缓存，
#调用close函数关闭后才会写入文件，要主动调用close或flush
#如果写入量大于缓存，会同步到磁盘上

f = open("file.py",'a+')##打开可写
f.write('12345667')
f.close()

##################################Python 文件指针操作##################################
#Python文件指针：
#os.SEEK_SET:  0 相对文件起始位置
#os.SEEK_CUR:  1 相对文件的当前位置
#os.SEEK_END:  2 相对文件的结束位置
#seek(偏移量[,相对位置])
import os
f = open("file.py",'r+')##打开可写
f.read(3)
f.read(3)
f.tell()
f.seek(0,os.SEEK_SET)
f.tell()
##################################Python 文件属性##################################
#python文件属性
#file.fileno()文件描述符
#file.mode文件打开权限
#file.encoding文件编码
#file.closed文件是否关闭
#sys.argv属性，可以获得命令行参数
#sys.argv字符串组成的列表
import sys
if __name__=='__main__':
    print len(sys.argv)
    for arg in sys.argv:
        print arg
##################################Python OS模块操作文件##################################
#flag打开文件方式
#os.O_CREAT：创建文件
#os.O_RDONLY：只读方式打开
#os.O_WRONLY：只写方式打开
#os.O_RDWR：读写方式打开
#os.read(fd,buffersize) :读取文件
#os.write(fd,buffersize) :读取文件
#os.lseek(fd,pos,how) :文件指针操作
#os.close(fd) :关闭文件
import os
f = open("file.py",'r+')##打开可写
f.read(3)
f.read(3)
f.tell()
f.seek(0,os.SEEK_SET)
f.tell()