import pytest
import sys
def add(arg1,arg2):
    return arg1+arg2
add(1,2)

def product(arg1,arg2):
    return arg1*arg2
product(1,2)

@pytest.mark.parametrize('arg1,arg2,result',[(3,5,8),('hello ','world','hello world'),(3.5,7.0,10.5)])
def test_add(arg1,arg2,result):
    assert add(arg1,arg2)==result

@pytest.mark.parametrize('arg1,arg2,result',[(5,5,25),('hello ',3,'hello hello hello ')])
def test_product(arg1,arg2,result):
    assert product(arg1,arg2)==result

@pytest.mark.skipif(sys.version_info>(3,3), reason='skip the test if python version greater than 3.3')
def test_add1():
    assert add(5,7)==12
    result=product('hello',3)
    assert 'hello' in result
    assert 'welcome' not in result

