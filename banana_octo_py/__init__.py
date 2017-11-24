import os.path as osp
from . import utils
from .core import hello_core
from . import sub

"""
Make functions in the file utils.py available as:

>>> banana_octo_py.utils.hello_utils()


Make functions in the file core.py available as:

>>> banana_octo_py.hello_core()


Build stuff in sub/
"""

__all__ = ['utils','sub','hello_core']

pkg_dir = osp.abspath(osp.dirname(__file__))
data_dir = osp.join(pkg_dir, 'data')

__version__ = '0.14dev'

print("ohai this is the banana_octo_pi package")


