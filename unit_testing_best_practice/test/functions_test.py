import os
import sys 
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'src'))
from functions import *

def test_name():
	assert validate_name('') == False
	assert validate_name('natha lie') == False

def test_pswd():
	assert not validate_pswd('asdfg2_') and not validate_pswd('asdfghj_') and not validate_pswd('1234567_') and not validate_pswd('asdfgh11')

def test_email():
	assert not validate_email('emailgmail.com') and not validate_email('email@gmailcom')

def test_pswd2():
	assert not validate_pswd('ashj1_')
