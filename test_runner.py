# coding=utf-8
import HtmlTestRunner
import os
import unittest
import time


# 设置报告文件保存路径
report_path = os.path.join(os.path.abspath('.'),'reports/')

# 构建suite
suite = unittest.TestLoader().discover("tests")

if __name__ =='__main__':

    # 初始化一个HTMLTestRunner实例对象，用来生成报告
    runner = HtmlTestRunner.HTMLTestRunner(output=report_path,report_title='My Report')
    # HtmlTestRunner(output=report_path, report_title='My Report')
    # 开始执行测试套件
    runner.run(suite)
