import pytest 
from chooseplan.views import match_code1, ret_code1

def test_match_code1():
    a = match_code1('1OSIS')
    if 'Sharp_Silver_70_HMO' in a:
        assert True
    else:
        assert False

def test_ret_code1():
    a = ('32S', '10DT', '40OSIS', '28SNC')
    b = []
    assert ret_code1(a) == b
    
