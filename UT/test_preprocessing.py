import sys, os

sys.path.append(os.path.abspath('.'))
print(os.path.abspath('.'))

from utils import line_preprocessor, parser
from UT.data import tests

def test_preprocessing():
    for test, res in tests:
        line_preprocessor(test)
        assert test == res