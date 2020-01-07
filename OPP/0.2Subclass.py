#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Student(object):
        a = 0  # 初始化计数器

        def __int__(self,name):   # 创建一个函数作为实例方法
                self.name = name  # 定义属性
                Student.a += 1    # 调用一次name，计数一次
