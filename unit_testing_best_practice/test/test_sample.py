import sys 
import os
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'src'))

from sample import *

def test_answer():
    assert func(3) == 4
