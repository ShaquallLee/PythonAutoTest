'''
Descripttion: 
Author: lishaogang
version: 
Date: 2021-11-13 16:16:38
LastEditors: lishaogang
LastEditTime: 2021-11-13 16:42:27
'''

import pytest

class TestA():
    def test_a1(self):
        assert 1==1
    
    def test_a2(self):
        assert 2==2

def test_1():
    assert 12==12

def test_2():
    print(555)
    assert(12 == int('12'))


if __name__ == "__main__":
    # pytest.main(['-s', __file__])  # -s:将函数中的print的结果打印出来
    pytest.main(['-v', r'test_1.py']) # -v:將測試結果詳細列出
    # pytest.main(['-q', r'F:/githubfiles/PythonAutoTest/testPytest']) #-q:简略输出测试结果
