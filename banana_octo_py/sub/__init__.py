from . import one
from . import two

# Define what gets imported when we run:
# from banana_octo_py.sub import *
__all__ = ['one','two']

def hello_from_submodule():
    return "Hello world! This is the submodule!"
