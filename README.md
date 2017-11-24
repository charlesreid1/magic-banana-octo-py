# banana-octo-py: a simple Python project

This simple project provides an example of how to create a package
following the [Python Packaging User Guide](https://packaging.python.org).

Also see the [Tutorial on Packaging and Distributing Projects](https://packaging.python.org/en/latest/distributing.html).

## module contents

Module was assembled following the [modules](https://docs.python.org/3/tutorial/modules.html#packages) documentation.

Import the module:

```
import banana_octo_py as bop
```

The `core.py` file defines a `hello_core()` that is imported 
at the module level:

```
bop.hello_core()
```

The `utils.py` file defines a `hello_utils()` that is imported
as a `utils` submodule:

```
bop.hello_utils()
```

The `sub` submodule defines a `hello_submodule()` function 
when it is imported:

```
bop.sub.hello_submodule()
```

There are further subcomponents of `sub`, specifically `one` and `two`:

```
bop.sub.hello_submodule_one()
bop.sub.hello_submodule_two()
```

## building

To build with Python 2:

```
python2 setup.py install --user
```

To build with Python 3:

```
python3 setup.py install --user --prefix=
```

## testing

To run the tests, you will need nose.
From the project directory, run:

```
nosetets
```

This will run all tests in the `tests/` directory.

The `.travis.yml` file runs the Travis tests by using tox to set up/configure Travis.

