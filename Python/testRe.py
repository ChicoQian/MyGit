# -*- coding: utf-8 -*-
##################################python正则表达式之re模块使用.##################################
# 调入正则表达式包re
import re
# 创建字符串
str1 = 'imooc lib'
# 生成规则
change = re.compile(r'imooc')
# 查看规则类型
print(type(change))
# 匹配目标
str1_match = change.match(str1)
# 保存目标
receive_str1_match = str1_match.group()
# 打印目标
print (receive_str1_match)
##################################python正则表达式语法.（单个字符）##################################
#1、ma=re.match(r".","除了\n的任意字符")#两个.可以匹配两个字符
#   [...]代表匹配所有字符集
#2、a-z:代表从字母a一直到z
#   ma=re.match(r"{[a-z]}","{d}")  \d/\D 匹配数字，非数字     sS空白非空白
#   ma=re.match(r"{[a-zA-Z0-9]}","{d}")#其中，\w或者是\W(非单词)可以代替a-zA-Z0-9
#   ma=re.match(r"\[[\w]\]","[a]")#注意，加入转义字符
ma = re.match(r'{[a-z]}','{A}')
##################################python正则表达式语法.（多个字符）##################################
#[A-Z][a-z]* Adasdas * = 0到无穷大
ma = re.match(r'[A-Z][a-z]*','Afsdsdf')
# [_a-zA-z]+[_\w]* + = 1到无穷大
ma = re.match(r'[_a-zA-z]+[_\w]*','_ht11')
# [1-9]?[0-9] ? = 0到1
ma = re.match(r'[1-9]?[0-9]','87')
# {m}/{m,n} = m次或者m到n次
ma = re.match(r'[a-zA-Z0-9]{6,10}@[/w]*.com','760799578@QQ.COM')
# *?或者+？或者？？非贪婪，见好就收（上面的加？）
ma = re.match(r'[0-9][a-z]*?','lbc')
##################################python正则表达式语法.（边界匹配（开头结尾））##################################
#^ 匹配字符串的开头
#$ 匹配字符串的结尾
ma = re.match(r'^[a-zA-Z0-9]{6,10}@[/w]*.COM$','760799578@QQ.COM')
#\A必须以我为字符串的开头
ma = re.match(r'\Aimmoc[\w]*','immocpython')
#| 匹配左右任意一个表达式
ma = re.match(r'abc|d','abc')
#(ab) 括号中表达式作为一个分组
ma = re.match(r'^[\w]{4,6}@(163|126).(COM|com)$','760799578@QQ.COM')
#\<number> 引用编号为number的分组匹配到的字符串
ma = re.match(r'<([\w]+)[\w]+</\1','<book>python</book>')
#(?P<name>) 分组起别名
ma = re.match(r'<(?P<mark>[\w]+)[\w]+</(?P=mark)','<book>python</book>')
#(?P=name) 引用别名为name的分组匹配字符串
##################################python正则表达式 re模块其他方法##################################
#search(pattern, string, flags=0)
#在一个字符串中查找匹配
str1 = 'imooc video num = 10000'
info = re.search(r'/d+',str1)
#findall(pattern, string, flags=0)
#返回所有匹配的列表集合
str2= 'c++=100,java=90,python=80'
info = re.findall(r'/d+',str2)
#sub(pattern, repl, string, count=0, flags=0)
#匹配部分替换为其他值
str3 = 'imooc videonum = 1000'
info = re.sub(r'/d+','10001',str3)
#split(pattern, string, maxsplit=0, flags=0)
#根据匹配分割字符串，返回分割字符串组成的列表