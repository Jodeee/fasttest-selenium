#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import re
import sys
import time
from fasttest_selenium.common import Var, log_info, log_error
from fasttest_selenium.drivers.driver_base import DriverBase
from fasttest_selenium.utils.opcv_utils import OpencvUtils


class ActionExecutor(object):

    def __from_scripts_file(self):

        file_list = []
        try:
            for rt, dirs, files in os.walk(os.path.join(Var.ROOT, "Scripts")):
                for f in files:
                    if f == "__init__.py" or f.endswith("pyc") or f.startswith("."):
                        continue
                    file_list.append(f'from Scripts.{f[:-3]} import *')

        except Exception as e:
            log_error(e, False)

        return file_list

    def __get_element_info(self, action, is_return=False):
        '''
        :param action:
        :return:
        '''
        parms = action.parms
        if len(parms):
            element = None
            if not re.match(r'[id|name|class|tag_name|link_text|partial_link_text|xpath|css_selector]+=(.*)+', parms[0].strip(), re.I):
                raise TypeError('input parameter format error:{}'.format(parms[0]))
            key = parms[0].strip().split('=', 1)[0]
            text = parms[0].strip().split('=', 1)[-1]
            if len(parms) == 1:
                element = DriverBase.get_elements(key, text, 0)
            elif len(parms) == 2:
                element = DriverBase.get_elements(key, text, int(parms[1]))
            else:
                raise TypeError('takes 2 positional arguments but {} was given'.format(len(parms)))
            if not element and not is_return:
                raise Exception("Can't find element: {}={}".format(key, text))
        else:
            raise TypeError('missing 1 required positional argument: element')
        return element

    def __action_open_url(self, action):
        """
        openUrl
        :param action:
        :return:
        """
        parms = action.parms
        if len(parms) == 1:
            DriverBase.open_url(parms[0])
        else:
            raise TypeError('openUrl missing 1 required positional argument: url')

    def __action_close(self):
        """
        close
        :param action:
        :return:
        """
        DriverBase.close()

    def __action_quit(self):
        """
        行为执行：quit
        :param action:
        :return:
        """
        DriverBase.quit()

    def __action_back(self):
        '''
        back
        :param action:
        :return:
        '''
        DriverBase.back()

    def __action_implicitly_wait(self, action):
        """
        行为执行：implicitlyWait
        :param action:
        :return:
        """
        parms = action.parms
        if len(parms) == 1:
            DriverBase.implicitly_wait(parms[0])
        else:
            raise TypeError('implicitlyWait missing 1 required positional argument: time')

    def __action_maximize_window(self):
        '''
        maxWindow
        :return:
        '''
        DriverBase.maximize_window()

    def __action_minimize_window(self):
        '''
        minWindow
        :return:
        '''
        DriverBase.minimize_window()

    def __action_clear(self):
        '''
        clear
        :return:
        '''
        DriverBase.clear()

    def __action_delete_all_cookies(self):
        '''
        deleteAllCookies
        :return:
        '''
        DriverBase.delete_all_cookies()

    def __action_delete_cookie(self, action):
        '''
        deleteCookies
        :return:
        '''
        parms = action.parms
        if len(parms) == 1:
            DriverBase.delete_cookie(parms[0])
        else:
            raise TypeError('deleteCookies missing 1 required positional argument: key')

    def __action_submit(self, action):
        '''
        submit
        :param action:
        :return:
        '''
        element = self.__get_element_info(action)
        DriverBase.submit(element)

    def __action_click(self, action):
        '''
        click
        :param action:
        :return:
        '''
        element = self.__get_element_info(action)
        DriverBase.click(element)

    def __action_context_click(self, action):
        '''
        contextClick
        :param action:
        :return:
        '''
        element = self.__get_element_info(action)
        DriverBase.context_click(element)

    def __action_double_click(self, action):
        '''
        doubleClick
        :param action:
        :return:
        '''
        element = self.__get_element_info(action)
        DriverBase.double_click(element)

    def __action_click_and_hold(self, action):
        '''
        holdClick
        :param action:
        :return:
        '''
        element = self.__get_element_info(action)
        DriverBase.click_and_hold(element)

    def __action_drag_and_drop(self, action):
        '''
        dragAndDrop
        :param action:
        :return:
        '''
        # todo
        # element = self.__get_element_info(action)
        # DriverBase.drag_and_drop(element)

    def __action_move_to_element(self, action):
        '''
        moveToElement
        :param action:
        :return:
        '''
        element = self.__get_element_info(action)
        DriverBase.move_to_element(element)

    def __action_send_keys(self, action):
        '''
        sendKeys
        :param action:
        :return:
        '''
        # todo
        # element = self.__get_element_info(action)
        # DriverBase.send_keys(element)

    def __action_check(self, action):
        '''
        check
        :param action:
        :return:
        '''
        self.__get_element_info(action)

    def __action_is_selected(self, action):
        '''
        isSelected
        :param action:
        :return:
        '''
        element = self.__get_element_info(action)
        return DriverBase.is_selected(element)

    def __action_is_displayed(self, action):
        '''
        isDisplayed
        :param action:
        :return:
        '''
        element = self.__get_element_info(action)
        return DriverBase.is_displayed(element)

    def __action_is_enabled(self, action):
        '''
        isEnabled
        :param action:
        :return:
        '''
        element = self.__get_element_info(action)
        return DriverBase.is_enabled(element)

    def __action_get_size(self, action):
        '''
        getSize
        :param action:
        :return:
        '''
        element = self.__get_element_info(action)
        return DriverBase.get_size(element)

    def __action_get_attribute(self, action):
        '''
        getAttribute
        :param action:
        :return:
        '''
        # todo
        # element = self.__get_element_info(action)
        # return DriverBase.get_attribute(element)

    def __action_get_text(self, action):
        '''
        getText
        :param action:
        :return:
        '''
        element = self.__get_element_info(action)
        return DriverBase.get_text(element)

    def __action_get_tag_name(self, action):
        '''
        getTagName
        :param action:
        :return:
        '''
        element = self.__get_element_info(action)
        return DriverBase.get_tag_name(element)

    def __action_get_location(self, action):
        '''
        getLocation
        :param action:
        :return:
        '''
        element = self.__get_element_info(action)
        return DriverBase.get_location(element)

    def __action_get_name(self):
        '''
        getName
        :param :
        :return:
        '''
        return DriverBase.get_name()

    def __action_get_title(self):
        '''
        getTitle
        :param action:
        :return:
        '''
        return DriverBase.get_title()

    def __action_get_current_url(self):
        '''
        getTitle
        :param :
        :return:
        '''
        return DriverBase.get_current_url()

    def __action_get_cookies(self):
        '''
        getCookies
        :param :
        :return:
        '''
        return DriverBase.get_cookies()

    def __action_get_cookie(self, action):
        '''
        getCookie
        :param :
        :return:
        '''
        parms = action.parms
        if len(parms) == 1:
            return DriverBase.get_cookie(parms[0])
        else:
            raise TypeError('getCookie missing 1 required positional argument: name')

    def __action_get_window_position(self):
        '''
        getWindowPosition
        :param :
        :return:
        '''
        return DriverBase.get_window_position()

    def __action_get_window_size(self):
        '''
        getWindowSize
        :param :
        :return:
        '''
        return DriverBase.get_window_size()
    
    def __action_ifcheck(self, action):
        """
        行为执行：ifcheck
        :param action:
        :return:
        """
        element = self.__get_element_info(action, is_return=True)
        if not element:
            return False
        return True

    def __action_sleep(self, action):
        """
        行为执行
        :param action:
        :return:
        """
        parms = action.parms
        if parms is None:
            raise TypeError('sleep missing 1 required positional argument')
        elif len(parms) == 1:
            time.sleep(float(parms[0]))

    def __ocr_analysis(self, action, element, israise):
        """
        :param action:
        :param element:
        :return:
        """
        if element not in Var.extensions_var['images_file'].keys():
            return False
        time.sleep(5)
        img_file = Var.extensions_var['images_file'][element]
        orcimg = OpencvUtils(action, img_file)
        orcimg.save_screenshot()
        img_info = orcimg.extract_minutiae()
        if img_info:
            return img_info
        else:
            if israise:
                raise Exception("Can't find element {}".format(element))
            else:
                return None

    def __action_getVar(self, action):
        '''
        :return:
        '''
        if action.key == '$.isSelected':
            result = self.__action_is_selected(action)
        elif action.key == '$.isDisplayed':
            result = self.__action_is_displayed(action)
        elif action.key == '$.isEnabled':
            result = self.__action_is_enabled(action)
        elif action.key == '$.getText':
            result = self.__action_get_text(action)
        elif action.key == '$.getSize':
            result = self.__action_get_size(action)
        elif action.key == '$.getAttribute':
            result = self.__action_get_attribute(action)
        elif action.key == '$.getText':
            result = self.__action_get_text(action)
        elif action.key == '$.getTagName':
            result = self.__action_get_tag_name(action)
        elif action.key == '$.getLocation':
            result = self.__action_get_location(action)
        elif action.key == '$.getName':
            result = self.__action_get_name()
        elif action.key == '$.getTitle':
            result = self.__action_get_title()
        elif action.key == '$.getCookies':
            result = self.__action_get_cookies()
        elif action.key == '$.getCookie':
            result = self.__action_get_cookie(action)
        elif action.key == '$.getWindowPosition':
            result = self.__action_get_window_position()
        elif action.key == '$.getWindowSize':
            result = self.__action_get_window_size()
        elif action.key == '$.getElement':
            result = self.__get_element_info(action)
        elif action.key == '$.id':
            result = eval(action.parms)
        elif action.key == '$.getVar':
            if Var.global_var:
                if action.parms[0] in Var.global_var:
                    result = Var.global_var[action.parms[0]]
                else:
                    result = None
            else:
                result = None
        elif action.key:
            list = self.__from_scripts_file()
            for l in list:
                exec(l)
            func = f'{action.key}({action.parms})'
            result = eval(func)
        else:
           result = action.parms[0]

        log_info(f'{action.name}: {type(result)} {result}')
        return result

    def __action_setVar(self, action):
        '''
        :return:
        '''
        key = action.parms[0]
        values = action.parms[1]
        Var.global_var[key] = values
        return

    def __action_call(self, action):
        '''
        :param action:
        :return:
        '''
        key = action.key
        parms = action.parms
        if  not key in Var.common_func.keys():
            raise NameError('name "{}" is not defined'.format(key))
        if len(Var.common_func[key].input) != len(parms):
            raise TypeError('{}() takes {} positional arguments but {} was given'.format(key, len(
                Var.common_func[key].input), len(parms)))
        common_var = dict(zip(Var.common_func[key].input, parms))

        try:
            from fasttest_selenium.runner.case_analysis import CaseAnalysis
            case = CaseAnalysis()
            case.iteration(Var.common_func[key].steps, f'{action.style}  ', common_var)
        except Exception as e:
            # call action中如果某一句step异常，此处会往上抛异常，导致call action也是失败状态，需要标记
            Var.exception_flag = True
            raise e
        return

    def __action_other(self, action):
        '''
        :return:
        '''
        key = action.key
        parms = action.parms
        try:
            result = eval(parms)
            log_info('{}: {}'.format(action.parms, result))
            if key == 'assert':
                assert result
            return result
        except Exception as e:
            raise e

    def new_action_executor(self, action):

        if action.key:
            list = self.__from_scripts_file()
            for l in list:
                exec(l)
            func = f'{action.key}({action.parms})'
            result = eval(func)
            return result
        else:
            raise KeyError('The {} keyword is undefined!'.format(action.step))

    def action_executor(self, action):
        """
        行为执行
        :param action:
        :return:
        """
        if action.tag and action.tag == 'getVar':
            result = self.__action_getVar(action)

        elif action.tag and action.tag == 'setVar':
            result = self.__action_setVar(action)

        elif action.tag and action.tag == 'call':
            result = self.__action_call(action)

        elif action.tag and action.tag == 'other':
            result = self.__action_other(action)

        elif action.key == 'openUrl':
            result = self.__action_open_url(action)

        elif action.key == 'close':
            result = self.__action_close()

        elif action.key == 'quit':
            result = self.__action_quit()

        elif action.key == 'implicitlyWait':
            result = self.__action_implicitly_wait(action)

        elif action.key == 'back':
            result = self.__action_back()

        elif action.key == 'maxWindow':
            result = self.__action_maximize_window()

        elif action.key == 'minWindow':
            result = self.__action_minimize_window()

        elif action.key == 'deleteAllCookies':
            result = self.__action_delete_all_cookies()

        elif action.key == 'deleteCookies':
            result = self.__action_delete_cookie()

        elif action.key == 'clear':
            result = self.__action_clear()

        elif action.key == 'submit':
            result = self.__action_submit(action)

        elif action.key == 'click':
            result = self.__action_click(action)

        elif action.key == 'contextClick':
            result = self.__action_context_click(action)

        elif action.key == 'doubleClick':
            result = self.__action_double_click(action)

        elif action.key == 'holdClick':
            result = self.__action_click_and_hold(action)

        elif action.key == 'dragAndDrop':
            result = self.__action_drag_and_drop(action)

        elif action.key == 'moveToElement':
            result = self.__action_move_to_element(action)

        elif action.key == 'sendKeys':
            result = self.__action_send_keys(action)

        elif action.key == 'check':
            result = self.__action_check(action)

        elif action.key == 'sleep':
            result = self.__action_sleep(action)

        elif action.key == 'ifcheck':
            result = self.__action_ifcheck(action)

        elif action.key == 'elifcheck':
            result = self.__action_ifcheck(action)

        elif action.key == 'break':
            result = None

        elif action.key == 'else':
            result = None

        else:
            raise KeyError('The {} keyword is undefined!'.format(action.key))

        return result