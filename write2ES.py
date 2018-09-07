# coding=utf-8
import pycurl2
import StringIO

# 打开被写入的json 文件
lines = open('/Users/ouyang/PycharmProjects/ouyang/out2.json', "r").readlines()
line_num = 0
total_lines = len(lines)
print(total_lines)

response = StringIO.StringIO()
c = pycurl2.Curl()
# 目标ES地址和index name
c.setopt(c.URL, '192.168.21.33:9200/test0907new2/log')
c.setopt(c.WRITEFUNCTION, response.write)
c.setopt(c.HTTPHEADER, ['Content-Type: application/json','Accept-Charset: UTF-8'])
while line_num < total_lines:
    c.setopt(c.POSTFIELDS, lines[line_num])
    c.perform()
    print response.getvalue()
    line_num = line_num + 1

c.close()
response.close()