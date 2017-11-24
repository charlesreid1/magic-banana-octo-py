import os
import os.path as osp

pkg_dir = osp.abspath(osp.dirname(__file__))
data_dir = osp.join(pkg_dir, 'data')

__version__ = '0.14dev'

print("ohai this is the banana_octo_pi package")



"""
Make functions in the file utils.py available as:

>>> banana_octo_py.utils.hello_utils()
"""
from . import utils



"""
Make functions in the file core.py available as:

>>> banana_octo_py.hello_core()
"""
from .core import *



"""
Build stuff in sub/
"""
from . import sub
