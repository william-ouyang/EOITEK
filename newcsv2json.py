# coding=utf-8

import sys, getopt
import csv
import json
import re
#import pycurl2
#import StringIO

input_file = sys.argv[1]
output_file = sys.argv[2]
#input_file = '/Users/ouyang/Desktop/increment.csv'
#output_file = '/Users/ouyang/PycharmProjects/ouyang/out.json'
lines = open(input_file, "r").readlines()
lines = [line.strip() for line in lines]
# 获取键值
keys = lines[0].split(',')
line_num = 1
total_lines = len(lines)
parsed_datas = []
while line_num < total_lines:
    values = lines[line_num].split(",")
    parsed_datas.append(dict(zip(keys, values)))
    out_string = str(dict(zip(keys, values)))
    #将time字段去空格并加上T
    out_string = re.sub(r'\d{4}-\d{2}-\d{2} ', lambda m: (m.group(0)).rstrip() + 'T', out_string)
    # 将time字段加上08：00
    out_string = re.sub(r'T\d{2}:\d{2}:\d{2}', lambda m: m.group(0) + '+08:00', out_string)
    # 将time改为timestamp
    out_string = re.sub(r'time', '@timestamp', out_string)
    # 将hit 去掉' 达到转成interger类型目的
    out_string = re.sub(r'hit\': \'', lambda m: (m.group(0)).rstrip('\''), out_string)
    out_string = re.sub(r'hit\': \d+\'', lambda m: (m.group(0)).rstrip('\''), out_string)
    # 将' 去掉以达到变成json格式
    out_string = re.sub(r'\'', '\"', out_string)
    #print(out_string)
    line_num = line_num + 1
    #print('\nparsed_datas is'.join(parsed_datas))

    #json_str = json.dumps(parsed_datas, ensure_ascii=False, indent=4)
    #output_file = input_file.replace("csv", "json")

# write to the file
    f = open(output_file, "a+")

    f.writelines(out_string+'\n')
    f.close()
print("解析结束！")

# print('****************(1)')
# response = StringIO.StringIO()
# c = pycurl2.Curl()
# c.setopt(c.URL, '192.168.21.33:9200/increment0907/log')
# c.setopt(c.WRITEFUNCTION, response.write)
# c.setopt(c.HTTPHEADER, ['Content-Type: application/json','Accept-Charset: UTF-8'])
# print(line_num)
# print(total_lines)
# line_num = 1
#
# while line_num < total_lines:
#
#     c.setopt(c.POSTFIELDS, lines[line_num])
#     c.perform()
#     print(response.getvalue())
#     line_num = line_num + 1
#
# c.perform()
# c.close()
# response.close()