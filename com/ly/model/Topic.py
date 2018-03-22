#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/3/22 23:19
# @Author  : Soloist
# @File    : Topic.py
# @Software: PyCharm


class Topic(object):

    def __init__(self, number, title, option_a, option_b, option_c, option_d, answer, difficulty):
        self.number = number
        self.title = title
        self.option_a = option_a
        self.option_b = option_b
        self.option_c = option_c
        self.option_d = option_d
        self.answer = answer
        self.difficulty = difficulty
