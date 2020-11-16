#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from fasttest_selenium.driver import *

def openUrl(url):

    driver.get(url)
    return

def find_elements_by_id(name):
    '''
    直接调用appium、macaca底层api
    :param name:
    :return:
    '''
    raise Exception("Can't find element {}".format(id))
    return name

def getText(id, index=1):
    '''
    调用已封装api
    :param id:
    :return:
    '''
    text = None

    elements = driver.wait_for_elements_by_name(id)
    if elements:
        text = elements[index].text
    else:
        raise Exception("Can't find element {}".format(id))
    return text

if __name__ == '__main__':
    import time
    start = time.time()
    s = 5
    while s >= 1:
        print(s)
        if s >= 4:
            s = s - 1
        elif 1 < s < 3:
            s = s - 1
        else:
            time.sleep(5)
            s = s - 1

    end = time.time()
    print(end-start)
