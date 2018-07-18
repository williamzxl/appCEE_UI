#! /usr/bin/python3
# coding=utf-8
import unittest
import os, time
from utils.config import REPORT_PATH, TEST_PATH
from BeautifulReport import BeautifulReport


def add_case(case_path=TEST_PATH, rule="test*.py"):
    '''加载所有的测试用例'''
    discover = unittest.defaultTestLoader.discover(case_path,
                                                  pattern=rule,
                                                  top_level_dir=None)
    return discover


def run(test_suit):
    result = BeautifulReport(test_suit)
    tm = time.strftime('%H%M%S', time.localtime(time.time()))
    result.report(filename='report_{}.html'.format(tm), description='测试deafult报告', log_path=REPORT_PATH)


if __name__ == "__main__":
    # 用例集合
    cases = add_case()
    run(cases)