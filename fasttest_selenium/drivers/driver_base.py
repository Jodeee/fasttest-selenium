#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re
from concurrent import futures
from fasttest_selenium.common import *
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

class DriverBase(object):


    @staticmethod
    def init():
        try:
            global driver
            driver = Var.instance
        except Exception as e:
            raise e

    @staticmethod
    def open_url(url):
        '''
        open url
        :param url:
        :return:
        '''
        driver.get(url)

    @staticmethod
    def close():
        '''
        close
        :param:
        :return:
        '''
        driver.close()

    @staticmethod
    def quit():
        '''
        quit
        :param:
        :return:
        '''
        driver.quit()

    @staticmethod
    def back():
        '''
        back
        close app
        :param
        :return:
        '''
        driver.back()


    @staticmethod
    def implicitly_wait(time):
        '''
        implicitlyWait
        :param: time
        :return:
        '''
        driver.implicitly_wait(float(time))

    @staticmethod
    def maximize_window():
        '''
        maxWindow
        :param:
        :return:
        '''
        driver.maximize_window()

    @staticmethod
    def minimize_window():
        '''
        minWindow
        :param:
        :return:
        '''
        driver.minimize_window()

    @staticmethod
    def delete_all_cookies():
        '''
        deleteAllCookies
        :param:
        :return:
        '''
        driver.delete_all_cookies()

    @staticmethod
    def delete_cookie(name):
        '''
        deleteCookies
        :param name
        :return:
        '''
        driver.delete_cookie(name)

    @staticmethod
    def submit(element):
        '''
        submit
        :param: element
        :return:
        '''
        element.submit()

    @staticmethod
    def clear(element):
        '''
        element
        :param:
        :return:
        '''
        element.clear()

    @staticmethod
    def click(element):
        '''
        click
        :param: element
        :return:
        '''
        element.click()


    @staticmethod
    def context_click(element):
        '''
        contextClick
        :param: element
        :return:
        '''
        ActionChains(driver).context_click(element).perform()

    @staticmethod
    def double_click(element):
        '''
        doubleClick
        :param: element
        :return:
        '''
        ActionChains(driver).double_click(element).perform()

    @staticmethod
    def click_and_hold(element):
        '''
        holdClick
        :param: element
        :return:
        '''
        ActionChains(driver).click_and_hold(element).perform()

    @staticmethod
    def drag_and_drop(element, target ):
        '''
        dragAndDrop
        :param element:鼠标按下的源元素
        :param target:鼠标释放的目标元素
        :return:
        '''
        ActionChains(driver).drag_and_drop(element, target).perform()

    @staticmethod
    def move_to_element(element):
        '''
        moveToElement
        :param element
        :return:
        '''
        ActionChains(driver).move_to_element(element).perform()

    @staticmethod
    def send_keys(element, text):
        '''
        sendKeys
        :param element:
        :param text:
        :return:
        '''
        element.send_keys(text)

    @staticmethod
    def is_selected(element):
        '''
        isSelected
        :param element:
        :return:
        '''
        return element.is_selected()

    @staticmethod
    def is_displayed(element):
        '''
        isDisplayed
        :param element:
        :return:
        '''
        return element.is_displayed()

    @staticmethod
    def is_enabled(element):
        '''
        isEnabled
        :param element:
        :return:
        '''
        return element.is_enabled()

    @staticmethod
    def get_size(element):
        '''
        getSize
        :param element:
        :return:
        '''
        return element.size

    @staticmethod
    def get_attribute(element, attribute):
        '''
        getAttribute
        :param element
        :param attribute
        :return:
        '''
        return element.get_attribute(attribute)

    @staticmethod
    def get_text(element):
        '''
        getText
        :param element:
        :return:
        '''
        return element.text

    @staticmethod
    def get_tag_name(element):
        '''
        getTagName
        :param element:
        :return:
        '''
        return element.tag_name

    @staticmethod
    def get_location(element):
        '''
        getLocation
        :param element:
        :return:
        '''
        return element.location

    @staticmethod
    def get_name():
        '''
        getName
        :return:
        '''
        return driver.name

    @staticmethod
    def get_title():
        '''
        getTitle
        :return:
        '''
        return driver.title

    @staticmethod
    def get_current_url():
        '''
        getCurrentUrl
        :return:
        '''
        return driver.current_url

    @staticmethod
    def get_cookies():
        '''
        getCookies
        :return:
        '''
        return driver.get_cookies()

    @staticmethod
    def get_cookie(name):
        '''
        getCookie
        :param name
        :return:
        '''
        return driver.get_cookie(name)

    @staticmethod
    def get_window_position():
        '''
        getWindowPosition
        :return:
        '''
        return driver.get_window_position()

    @staticmethod
    def get_window_size():
        '''
        getWindowSize
        :return:
        '''
        return driver.get_window_size()

    # @staticmethod
    # def get_element(type, text):
    #     '''
    #     getElement
    #     :param type:
    #     :param text:
    #     :return:
    #     '''
    #     element = driver.find_element(type, text)
    #     return element

    @staticmethod
    def get_elements(type, text, index=0):
        '''
        getElements
        :param type:
        :param text:
        :return:
        '''
        type = type.lower()
        by = Dict({
            'id': By.ID,
            'name': By.NAME,
            'xpath': By.XPATH,
            'class': By.CLASS_NAME,
            'tag_name': By.TAG_NAME,
            'link_text': By.LINK_TEXT,
            'css_selector': By.CSS_SELECTOR,
            'partial_link_text': By.PARTIAL_LINK_TEXT,
        })
        elements = driver.find_elements(by[type], text)
        if elements:
            if len(elements) <= int(index):
                log_error('elements exists, but cannot find index({}) position'.format(index), False)
                raise Exception('list index out of range, index:{}'.format(index))
            return elements[index]
        return None