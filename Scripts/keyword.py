#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from fasttest_selenium.driver import *

def keyDown(name):
    '''
    调用selenium api完成负责动作
    '''
    elements = driver.find_elements(By.CLASS_NAME, name)
    ActionChains(driver).key_down(Keys.COMMAND, elements[0]).send_keys('c').key_up(Keys.COMMAND).perform()

def getText():
    '''
    调用普通脚本
    '''
    return '这是一条测试数据!'
