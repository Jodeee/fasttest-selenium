#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from fasttest_selenium.driver import *

def keyDown(element, text):
    '''
    调用selenium api完成负责动作
    '''
    print(element.text)
    log_info(text)

def getText(text):
    '''
    调用普通脚本
    '''
    log_info(text)
    return text
