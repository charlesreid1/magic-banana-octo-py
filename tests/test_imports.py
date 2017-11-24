import banana_octo_py as bop

def test_core():
    assert bop.hello_core()=="Hello world! This is the core.py file"

def test_utils():
    assert bop.utils.hello_utils()=="Hello world! This is the utils.py file"

def test_sub():
    assert bop.sub.hello_submodule()=="Hello world! This is the submodule!"
    assert bop.sub.one.hello_submodule_one()=="Hello world! This is the submodule file, one.py!"
    assert bop.sub.two.hello_submodule_two()=="Hello world! This is the submodule file, two.py!"


