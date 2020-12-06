#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
from selenium import webdriver
from fasttest_selenium.common import *


class ServerUtils(object):

    def __getattr__(self, item):
        try:
            return self.__getattribute__(item)
        except:
            return None

    def __init__(self, browser, browser_config):
        self.browser = browser
        self.instance = None
        self.browser_config = browser_config

    def start_server(self):

        try:
            path = None
            if self.browser_config:
                if 'path' in self.browser_config.keys():
                    path = self.browser_config['path']
                    if not os.path.isfile(path):
                        log_error(' No such file : {}'.format(path), False)
                        path = None
            if self.browser.lower() == 'chrome':
                if path:
                    self.instance = webdriver.Chrome(path)
                else:
                    self.instance = webdriver.Chrome()
            elif self.browser.lower == 'safari':
                pass
            return self.instance
        except Exception as e:
            raise e

    def stop_server(self, instance):

        try:
            instance.quit()
        except Exception as e:
            raise e

