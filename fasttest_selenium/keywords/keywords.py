#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def return_keywords():
    keywords = [
        "openUrl",  # 打开地址
        "close",  # 关闭浏览器
        "quit",  # 关闭浏览器并退出驱动
        "submit",  # 提交表单
        "back",  # 返回上一步
        "forward", # 前进
        "refresh", # 刷新
        "check",  # 检查元素
        "click",  # 单击
        "contextClick",  # 右击
        "doubleClick",  # 双击
        "holdClick",  # 按下鼠标左键
        "dragDrop",  # 鼠标拖放
        "dragDropByOffset", # 拖动元素到某个位置
        "moveByOffset", # 鼠标从当前位置移动到某个坐标
        "moveToElement",  # 鼠标移动
        "moveToElementWithOffset", #移动到距某个元素(左上角坐标)多少距离的位置
        "keyDown", # 按下某个键盘上的键
        "keyUp", # 松开某个键
        "sendKeys",  # 输入
        "clear",  # 清除
        "maxWindow",  # 窗口最大化
        "minWindow",  # 窗口最小化
        "implicitlyWait", # 设置等待时间
        "deleteAllCookies",  # 删除所有cookies
        "deleteCookies",  # 删除指定cookies
        "switchToFrame" # 切换到指定frame
        "switchToDefaultContent", # 切换到主文档
        "switchToParentFrame", # 切回到父frame
        "$.isSelected",  # 判断是否选中
        "$.isDisplayed",  # 判断元素是否显示
        "$.isEnabled",  # 判断元素是否被使用
        "$.getSize",  # 获取元素大小
        "$.getAttribute",  # 获取元素属性
        "$.getText",  # 获取元素文案
        "$.getTagName",  # 获取元素tag Name
        "$.getLocation",  # 获取元素坐标
        "$.getName",  # 获取浏览器名字
        "$.getTitle",  # 获取标题
        "$.getCurrentUrl", # 获取当前页面url
        "$.getCookies",  # 获取所有cookie
        "$.getCookie",  # 获取指定cookie
        "$.getWindowPosition",  # 获取窗口坐标
        "$.getWindowSize",  # 获取窗口大小
        "$.getElement",  # 获取元素
        "$.getElements",  # 获取元素
        "$.id",  # 科学运算
        "$.getVar",  # 获取全局变量
        "$.setVar",  # 设置全局变量
        "sleep",
        "break",
        "while",
        "if",
        "elif",
        "else",
        "ifcheck",
        "elifcheck",
        "assert"
    ]

    return keywords

