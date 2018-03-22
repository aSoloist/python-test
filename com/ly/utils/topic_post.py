#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/3/22 22:50
# @Author  : Soloist
# @File    : topic_post.py
# @Software: PyCharm

import xlrd
from com.ly.model.Topic import Topic
import requests
import json


# 打开excel文件
def open_excel(filename):
    try:
        open_file = xlrd.open_workbook(filename)
        print('读取到文件。。。')
        return open_file
    except Exception as e:
        print(e)


def read_excel(filename, index=0, sheet_name=u'Sheet1'):
    topic_list = []
    # 打开excel文件
    file = open_excel(filename)
    # 通过sheet名字获取sheet
    sheet = file.sheet_by_name(sheet_name)
    rows = sheet.nrows
    for i in range(index, rows):
        row_list = sheet.row_values(i)
        topic = Topic(i, row_list[0], row_list[1], row_list[2], row_list[3], row_list[4], row_list[5], row_list[6])
        topic_list.append(topic)
    print('完成')
    return topic_list


def get_post(topic):
    if topic.difficulty == '易':
        topic.difficulty = 'SIMPLE'
    elif topic.difficulty == '中':
        topic.difficulty = 'MEDIUM'
    elif topic.difficulty == '难':
        topic.difficulty = 'DIFFICULT'
    if topic.option_a == '':
        return {
            'topicNumber': str(topic.number),
            'title': topic.title,
            'answer': topic.answer,
            'difficulty': topic.difficulty
        }
    else:
        return {
            'topicNumber': str(topic.number),
            'title': topic.title,
            'optionA': topic.option_a,
            'optionB': topic.option_b,
            'optionC': topic.option_c,
            'optionD': topic.option_d,
            'answer': topic.answer,
            'difficulty': topic.difficulty
        }


def do_post(topic_list, url):
    session = requests.session()
    session.headers.update({'Content-Type': 'application/json; charset=utf-8'})
    for topic in topic_list:
        response = session.post(url, data=json.dumps(get_post(topic)))
        print(response.status_code)
        # print(get_post(topic))


if __name__ == '__main__':
    topics = read_excel('c语言题库.xls', 1)
    do_post(topics, 'http://localhost:8080/topic/save.do')
