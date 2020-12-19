#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import re
import sys
import time
import shutil

class Template_mixin(object):
    """
     Define a HTML template for report customerization and generation.

     Overall structure of an HTML report

     HTML
     +------------------------+
     |<html>                  |
     |  <head>                |
     |                        |
     |   STYLESHEET           |
     |   +----------------+   |
     |   |                |   |
     |   +----------------+   |
     |                        |
     |  </head>               |
     |                        |
     |  <body>                |
     |                        |
     |   HEADING              |
     |   +----------------+   |
     |   |                |   |
     |   +----------------+   |
     |                        |
     |   REPORT               |
     |   +----------------+   |
     |   |                |   |
     |   +----------------+   |
     |                        |
     |   ENDING               |
     |   +----------------+   |
     |   |                |   |
     |   +----------------+   |
     |                        |
     |  </body>               |
     |</html>                 |
     +------------------------+
     """
    HTML_TMPL = r'''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>测试报告</title>
    <link rel="stylesheet" type="text/css" href="resource/css.css">
    <script type="text/javascript" src="http://libs.baidu.com/jquery/2.1.1/jquery.min.js"></script>
    <script src="resource/js.js"></script>
</head>
<body>
<div class="root">
    {heading}
    {tabdiv}
</div>
</body>
</html>
    '''

    # 测试汇总
    HEADING_TMPL = r'''
        <div class="result_css_title">
            <h2 style="color: white;text-align: center;line-height: 65px">{title}</h2>
        </div>
        <div class="result_css_head" style="height: 240px">
            <div class="result_css_head_title">Summarization</div>
            <div style="height: 210px;border: 1px solid rgb(220,220,220); background-color: white">
                <p class="result_css_text">Total：{total}</p>
                <p class="result_css_text">Success：{success}</p>
                <p class="result_css_text">Failure：{failure}</p>
                <p class="result_css_text">Error：{error}</p>
                <p class="result_css_text">Skipped：{skipped}</p>
                <p class="result_css_text">StartTime：{startTime}</p>
                <p class="result_css_text">Duration：{duration}</p>
            </div>
        </div>
        '''

    # 详细数据
    TABDIV_TMPL = r'''
        <div class="result_css_tabdiv" style="height: auto">
        <div class="result_css_head_title">Details</div>
        <div style="height:auto;border: 1px solid rgb(220,220,220); background-color: white">
            <table class="result_css_table" cellspacing="0">
                <tr>
                    <th class="result_css_th" width="20%%">CaseName</th>
                    <th class="result_css_th" width="30%%">Description</th>
                    <th class="result_css_th" width="20%%">StartTime</th>
                    <th class="result_css_th" width="10%%">Duration</th>
                    <th class="result_css_th" width="10%%">Status</th>
                    <th class="result_css_th" width="10%%">Open/Close</th>
                </tr>
                {trlist}
            </table>
        </div>
        </div>
    '''

    # module_name
    MODULE_NAME = r'''
                <tr>
                    <td class="result_css_module_td" colspan="2" style=" text-align:left; text-indent: 20px;">{module_name}</td>
                    <td class="result_css_module_td" colspan="3"><span class="result_css_success result_css_status">&nbsp;success:{success}&nbsp;</span> | <span class="result_css_failure result_css_status">&nbsp;failure:{failure}&nbsp;</span> | <span class="result_css_error result_css_status">&nbsp;error:{error}&nbsp;</span> | <span class="result_css_skipped result_css_status">&nbsp;skipped:{skipped}&nbsp;</span></td>
                    <td class="result_css_module_name" data-tag='module_name_{tag_module_name}'>Open</td>
                </tr>
    '''

    # case
    CASE_TMPL = r'''
                <tr class='module_name_{module_name}' style="display: none">
                    <td class="result_css_module_td result_css_{b_color}" style=" text-align:left; text-indent: 40px;">{casename}</td>
                    <td class="result_css_module_td result_css_{b_color}">{description}</td>
                    <td class="result_css_module_td result_css_{b_color}">{startTime}</td>
                    <td class="result_css_module_td result_css_{b_color}">{duration}</td>
                    <td class="result_css_module_td result_css_{b_color}">{status}</td>
                    <td class="result_css_module_td_view result_css_{b_color}" data-tag='module_td_view_{module}_{dataId}'>Open</td>
                </tr>
    '''

    # case details
    CASE_DETA_NOT_SNAPSHOT = r'''
                <tr class="module_td_view_{module_name}_{dataId}" style="display: none">
                    <td class="result_css_module_deta" colspan="2" style="border-right: 0">
                        <div class="result_css_errordiv">
                            <h3 style="margin-bottom: 10px">Steps</h3>
                            <pre class="result_css_errorp" style="white-space: pre-wrap;overflow-wrap: break-word;margin-top: 0">{steplist}</pre>
                        </div>
                    </td>
                    <td class="result_css_module_deta" colspan="4">
                        <div class="result_css_errordiv">
                            <h3 style="margin-bottom: 10px">Logs</h3>
                            <pre class="result_css_errorp" style="white-space: pre-wrap;overflow-wrap: break-word;margin-top: 0">{errlist}</pre>
                        </div>
                    </td>
                </tr>
    '''

    CASE_DETA_SNAPSHOT = r'''
                <tr class="module_td_view_{module_name}_{dataId}" style="display: none">
                    <td class="result_css_module_deta" colspan="6" style="border-right: 0">
                        <div class="result_css_errordiv">
                            <h3 style="margin-bottom: 10px">Steps</h3>
                            {steplist}
                        </div>
                    </td>
                </tr>
    '''
    CASE_SNAPSHOT_DIV = r'''
                            <div class="result_css_Stepsdetails">
                                <div class="result_css_steps" style="display: inline-block">
                                        <pre class="result_css_StepsdetailsPre_duration">{runtime} | </pre>
                                        <pre class="result_css_StepsdetailsPre {status}">{steps}</pre>
                                </div>
                                <div class="img_errorp" style="display: none;">
                                    <img class="result_css_img" src="{image}">
                                </div>
                            </div>
    '''
    CASE_NOT_SNAPSHOT_DIV = r'''
                            <div class="result_css_Stepsdetails">
                                <div class="result_css_steps" style="display: inline-block">
                                        <pre class="result_css_StepsdetailsPre_duration">{runtime} | </pre>
                                        <pre class="result_css_StepsdetailsPre {status}">{steps}</pre>
                                </div>
                            </div>
    '''
    CASE_ERROR_DIV = r'''
                            <div class="result_css_Stepsdetails">
                                <div class="result_css_steps" style="display: inline-block">
                                        <pre class="result_css_StepsdetailsPre_duration">{runtime} | </pre>
                                        <pre class="result_css_StepsdetailsPre {status}">{steps}</pre>
                                </div>
                                <div class="img_errorp" style="display: none;">
                                    <img class="result_css_img" src="{image}">
                                    <pre class="result_css_errorp" style="white-space: pre-wrap;overflow-wrap: break-word;">{errlist}</pre>
                                </div>
                            </div>
    '''
    CASE_NOT_ERROR_DIV = r'''
                            <div class="result_css_Stepsdetails">
                                <div class="result_css_steps" style="display: inline-block">
                                        <pre class="result_css_StepsdetailsPre_duration">{runtime} | </pre>
                                        <pre class="result_css_StepsdetailsPre {status}">{steps}</pre>
                                </div>
                                <div class="img_errorp" style="display: none;">
                                    <pre class="result_css_errorp" style="white-space: pre-wrap;overflow-wrap: break-word;">{errlist}</pre>
                                </div>
                            </div>
    '''

    DEFAULT_TITLE = 'Unit Test Report'
    DEFAULT_DESCRIPTION = ''

class HTMLTestRunner(Template_mixin):

    def __init__(self, stream=sys.stdout, verbosity=1, title=None, description=None):
        self.stream = stream
        self.verbosity = verbosity
        self.title = title if title else self.DEFAULT_TITLE
        self.description = description if description else self.DEFAULT_DESCRIPTION

    def generateReport(self,result,starttime,stoptime):
        # 获取头部数据
        report_attrs = self._getReportAttributes(result, starttime, stoptime)
        report = self._generate_report(result)
        heading = self._generate_heading(report_attrs)
        tabdiv = self.TABDIV_TMPL.format(
            trlist = report
        )
        output = self.HTML_TMPL.format(
            heading = heading,
            tabdiv = tabdiv
        )
        resource = os.path.join(os.path.split(os.path.abspath(__file__))[0], "resource")
        shutil.copy(os.path.join(resource,"css.css"), os.path.join(result.report,'resource'))
        shutil.copy(os.path.join(resource,"js.js"), os.path.join(result.report,'resource'))
        self.stream.write(output.encode('utf-8'))

    def _getReportAttributes(self,result,starttime,stoptime):

        startTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(starttime))
        duration = str(int(stoptime - starttime)) + 's'
        Total = result.testsRun
        Success = len(result.successes)
        Failure = len(result.failures)
        Error = len(result.errors)
        skipped = len(result.skipped)
        return (Total,Success,Failure,Error,skipped,startTime,duration)

    def _generate_report(self, result):
        '''
        解析结果
        :param result:
        :return:
        '''
        table_lsit = []
        for module_name, module_list in result.result.items():
            success = 0
            failure = 0
            error = 0
            skipped = 0
            cls_list = []
            for test_info in module_list:
                # case模块
                case_module = self._generate_case(test_info)
                cls_list.append(case_module)

                # 具体case
                status = test_info.status
                if status != 3: # skip
                    case_deta = self._generate_case_deta(test_info)
                    cls_list.append(case_deta)

                # 统计结果
                if status == 0:
                    success += 1
                elif status == 1:
                    failure += 1
                elif status == 2:
                    error += 1
                elif status == 3:
                    skipped += 1

            module_name = self.MODULE_NAME.format(
                module_name = module_name,
                success = success,
                failure = failure,
                error = error,
                skipped = skipped,
                tag_module_name = module_name
            )

            table_lsit.append(module_name)
            for tr in cls_list:
                table_lsit.append(tr)

        tr_ = ''
        for tr in table_lsit:
            tr_ = tr_ + tr
        return tr_

    def _generate_heading(self,report_attrs):

        if report_attrs:
            heading = self.HEADING_TMPL.format(
                title = self.title,
                total = report_attrs[0],
                success = report_attrs[1],
                failure = report_attrs[2],
                error = report_attrs[3],
                skipped = report_attrs[4],
                startTime = report_attrs[5],
                duration = report_attrs[6]
            )
            return heading

    def _generate_case(self,testinfo):
        '''
        module 样式
        :param testinfo:
        :return:
        '''
        status_list = ['success', 'failure', 'error', 'skipped']
        casename = testinfo.casename
        status = status_list[testinfo.status]
        description = testinfo.description
        startTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(testinfo.start_time))
        duration = str(int(testinfo.stop_time - testinfo.start_time)) + 's'
        dataId = testinfo.dataId
        module_name = testinfo.module_name

        caseinfo = self.CASE_TMPL.format(
            module_name=module_name,
            casename=casename,
            description=description,
            startTime=startTime,
            duration=duration,
            status=status,
            module=module_name,
            dataId=dataId,
            b_color=status
        )
        return caseinfo

    def _generate_case_deta(self,test_info):
        '''
        具体case
        :param testinfo:
        :return:
        '''
        dataId = test_info.dataId
        module_name = test_info.module_name
        err = '\n' + test_info.err if test_info.err else 'Nothing'
        steps = ""
        if os.path.exists(test_info.snapshot_dir):
            for key in sorted(test_info.test_case_steps):
                value = test_info.test_case_steps[key]
                run_time = value['duration']
                step = value['step'].replace('\n', '')
                if value['result']:
                    step = '{} --> {}'.format(value['step'], value['result']).replace('\n', '')
                image_path = value['snapshot'].split(test_info.report)[-1]
                image_path = image_path.lstrip(os.sep)
                if value['status']:
                    if os.path.isfile(value['snapshot']):
                        case_snapshot = self.CASE_SNAPSHOT_DIV.format(
                            status='result_css_successfont',
                            runtime=run_time,
                            steps=step,
                            image=image_path
                        )
                    else:
                        case_snapshot = self.CASE_NOT_SNAPSHOT_DIV.format(
                            status='result_css_successfont',
                            runtime=run_time,
                            steps=step
                        )
                else:
                    if os.path.isfile(value['snapshot']):
                        case_snapshot = self.CASE_ERROR_DIV.format(
                            status='result_css_errorfont',
                            runtime=run_time,
                            steps=step,
                            image=image_path,
                            errlist=err
                        )
                    else:
                        case_snapshot = self.CASE_NOT_ERROR_DIV.format(
                            status='result_css_errorfont',
                            runtime=run_time,
                            steps=step,
                            errlist=err
                        )

                steps = steps + case_snapshot

            casedeta = self.CASE_DETA_SNAPSHOT.format(
                module_name=module_name,
                dataId=dataId,
                steplist=steps,
            )
        else:
            casedeta = self.CASE_DETA_NOT_SNAPSHOT.format(
                module_name=module_name,
                dataId=dataId,
                steplist=steps,
                errlist=err
            )

        return casedeta


def embedded_numbers(s):
    '''
    :param s:
    :return:
    '''
    re_digits = re.compile(r'(\d+)')
    pieces = re_digits.split(s)
    pieces[1::2] = map(int,pieces[1::2])
    return pieces

def sort_string(lst):

    return sorted(lst,key=embedded_numbers)
