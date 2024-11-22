import sys 
sys.path += ['../src'] 

from prime import *

def test_is_prime():
    assert is_prime(2) == True
    assert is_prime(3) == True
    assert is_prime(4) == False
    assert is_prime(1) == False
    assert is_prime(0) == False
    assert is_prime(-7) == False
    assert is_prime(29) == True
