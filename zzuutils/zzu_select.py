# !/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    选课脚本
"""
__author__ = 'python-test'

import requests
import sys
from bs4 import BeautifulSoup
from apscheduler.schedulers.blocking import BlockingScheduler

session = requests.session()
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/64.0.3282.140 Safari/537.36'}
session.headers.update(headers)

scheduler = BlockingScheduler()

name = ''
value = ''
sub_url = ''


def get_login_data(grade, user_id, password):
    return {
        'nianji': grade,
        'xuehao': user_id,
        'mima': password,
        'xkstep': '1'
    }


def get_post(response_text):
    global name
    global value
    global sub_url
    one_name = ''
    one_value = ''
    sub_url = get_url(response_text)
    soup = BeautifulSoup(response_text, 'html.parser')
    div_tag = soup.find('table', {'height': '18'})
    tr_tags = div_tag.find_all('tr')
    count = 0
    for tr in tr_tags[2:]:
        credit = tr.find('td', {'width': '34'})
        if credit.string == '2':
            course_input = tr.find('input')
            if course_input['type'] == 'checkbox':
                name = course_input['name']
                value = course_input['value']
                count = count + 1
        elif credit.string == '1':
            course_input = tr.find('input')
            if course_input['type'] == 'checkbox':
                one_name = course_input['name']
                one_value = course_input['value']
    if count == 0:
        name = one_name
        value = one_value


def do_select():
    print('选课中……')
    if not (name and value):
        response = session.post(sub_url, {name: value})
        status = response.status_code
        if status == 200:
            print('选课成功')
            scheduler.shutdown(0)
        else:
            print('选课失败，尝试重新选课')
            do_select()
    else:
        print('课程已满')


def login(grade, user_id, password):
    print('登陆中……')
    response = session.post('http://202.196.64.154/scripts/newxkxt.dll/newlogin',
                            get_login_data(grade, user_id, password))
    response.encoding = 'gbk'
    if response.status_code == 200:
        print('登陆成功')
        get_post(response.text)
    else:
        print('登陆失败，尝试重新登陆……')
        login(grade, user_id, password)


# 获取提交url
def get_url(response_text):
    soup = BeautifulSoup(response_text, 'html.parser')
    url = soup.form['action']
    return url


if __name__ == '__main__':
    args = sys.argv
    if len(args) == 1:
        login('2016', '', '')
        scheduler.add_job(login, 'interval', args=('2016', '', ''), minutes=10)
        scheduler.add_job(do_select, 'cron', hour=0, minute=0)
        scheduler.start()
    elif len(args) == 4:
        scheduler.add_job(login, 'interval', args=(args[1], args[2], args[3]), seconds='10')
    else:
        raise ValueError('传入参数个数错误')
