'''
Descripttion: 
Author: lishaogang
version: 
Date: 2021-11-13 16:16:38
LastEditors: lishaogang
LastEditTime: 2021-11-14 10:44:05
'''

import pytest

def setup_module():
    print('test1 start')

def teardown_module():
    print('test1 end')

class TestA():
    def test_a1(self):
        assert 1 == 1

    def test_a2(self):
        assert 2 == 2


@pytest.mark.a
def test1():
    assert 12 == 12


@pytest.mark.b
def test2():
    print(555)
    assert(12 == int('12'))


if __name__ == "__main__":
    # pytest.main(['-s', __file__])  # -s:将函数中的print的结果打印出来
    # pytest.main(['-v', r'test_1.py']) # -v:將測試結果詳細列出
    # -q:简略输出测试结果
    pytest.main(['-q', r'F:/githubfiles/PythonAutoTest/testPytest'])
