# !/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    查询成绩脚本
"""
__author__ = 'python-test'

import sys
import re
import requests
from bs4 import BeautifulSoup

session = requests.session()
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/64.0.3282.140 Safari/537.36'}
session.headers.update(headers)


def get_search_data(grade, user_id, password):
    return {
        'nianji': grade,
        'xuehao': user_id,
        'mima': password,
        'selec': 'http://jw.zzu.edu.cn/scripts/qscore.dll/search'
    }


def search(grade, user_id, password):
    response = session.post('http://jw.zzu.edu.cn/scripts/qscore.dll/search',
                            data=get_search_data(grade, user_id, password))
    response.encoding = 'gbk'

    # print(response.text)
    soup = BeautifulSoup(response.text, 'html.parser')

    # 学生信息
    p_tags = soup.find_all('p')
    # print(p_tags[1].string)
    # print(re.split(r'\s+', p_tags[1].string))
    lists = re.split('\s+', p_tags[1].string)
    student_message = ''
    for l in lists:
        student_message += l + '  '
    print(student_message)

    # 成绩
    tr_tags = soup.find_all('tr')
    for tr in tr_tags[1:]:
        td_tags = tr.contents
        row_str = ''
        for td in td_tags:
            row_str += td.string + '  '
        print(row_str)

    # 绩点
    lists = re.split('\s+', p_tags[2].string)
    student_message = ''
    for l in lists:
        student_message += l + '  '
    print(student_message)


if __name__ == '__main__':
    args = sys.argv
    if len(args) == 1:
        search('2016', '', '')
    elif len(args) == 4:
        search(args[1], args[2], args[3])
    else:
        raise ValueError('传入参数个数错误')
