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

    def __init__(self, browser, browser_options, implicitly_wait, max_window):
        self.browser = browser
        self.instance = None
        self.browser_options = browser_options
        if implicitly_wait is None :
            implicitly_wait = 5
        self.implicitly_wait = implicitly_wait
        if max_window is None:
            max_window = False
        self.max_window = max_window

    def start_server(self):

        try:
            path = None
            if self.browser_options:
                if 'path' in self.browser_options.keys():
                    path = self.browser_options['path']
                    if not os.path.isfile(path):
                        log_error(' No such file : {}'.format(path), False)
                        path = None
            if self.browser.lower() == 'chrome':
                options = webdriver.ChromeOptions()
                if self.browser_options:
                    if 'options' in self.browser_options.keys():
                        for opt in self.browser_options['options']:
                            options.add_argument(opt)
                if path:
                    self.instance = webdriver.Chrome(executable_path=path,
                                                     chrome_options=options)
                else:
                    self.instance = webdriver.Chrome(chrome_options=options)
            elif self.browser.lower() == 'firefox':
                options = webdriver.FirefoxOptions()
                if self.browser_options:
                    if 'options' in self.browser_options.keys():
                        for opt in self.browser_options['options']:
                            options.add_argument(opt)
                if path:
                    self.instance = webdriver.Firefox(executable_path=path,
                                                      firefox_options=options)
                else:
                    self.instance = webdriver.Firefox(firefox_options=options)
            elif self.browser.lower() == 'edge':
                if path:
                    self.instance = webdriver.Edge(executable_path=path)
                else:
                    self.instance = webdriver.Edge()
            elif self.browser.lower() == 'safari':
                self.instance = webdriver.Safari()
            elif self.browser.lower() == 'ie':
                if path:
                    self.instance = webdriver.Ie(executable_path=path)
                else:
                    self.instance = webdriver.Ie()
            elif self.browser.lower() == 'opera':
                if path:
                    self.instance = webdriver.Opera(executable_path=path)
                else:
                    self.instance = webdriver.Opera()
            elif self.browser.lower() == 'phantomjs':
                if path:
                    self.instance = webdriver.PhantomJS(executable_path=path)
                else:
                    self.instance = webdriver.PhantomJS()

            self.instance.implicitly_wait(self.implicitly_wait)
            if self.max_window:
                self.instance.maximize_window()
            return self.instance
        except Exception as e:
            raise e

    def stop_server(self, instance):

        try:
            instance.quit()
        except Exception as e:
            raise e

