import unittest
import main
from configparser import *
config = ConfigParser()
config.read('config.ini', encoding='utf-8-sig')
print(r'' + config.get('client', 'profile') + '')


