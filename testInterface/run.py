'''
Descripttion: 接口测试主入口
Author: lishaogang
version: 
Date: 2021-11-19 15:57:28
LastEditors: lishaogang
LastEditTime: 2021-11-19 16:28:02
'''

from common.utils import case_path, report_path, getTime
import pytest
import os

now = getTime()
file = os.path.join(report_path, now+'.html').replace('\\', '/')
pytest.main(['-v', r'--html={}'.format(file), case_path])
