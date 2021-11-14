'''
Descripttion: 
Author: lishaogang
version: 
Date: 2021-11-14 10:44:21
LastEditors: lishaogang
LastEditTime: 2021-11-14 10:46:16
'''
import pytest

def setup_module():
    print('test2 start')

def teardown_module():
    print('test2 end')

@pytest.mark.parametrize('a',[1,2,3,4,5,6])
def test_range(a):
    assert a>=3

