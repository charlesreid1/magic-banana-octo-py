# banana-octo-py: a simple Python project

This simple project provides an example of how to create a package
following the [Python Packaging User Guide](https://packaging.python.org).

Also see the [Tutorial on Packaging and Distributing Projects](https://packaging.python.org/en/latest/distributing.html).

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
