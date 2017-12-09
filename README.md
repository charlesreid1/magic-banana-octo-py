# magic-octo-py: a simple Jupyter/IPython notebook extension 

<a href="https://travis-ci.org/charlesreid1/magic-octo-py">
<img src="https://travis-ci.org/charlesreid1/magic-octo-py.svg?branch=master" />
</a>

This simple project provides an example of how to create a package
following the [Python Packaging User Guide](https://packaging.python.org).

See the [Tutorial on Packaging and Distributing Projects](https://packaging.python.org/en/latest/distributing.html).

See the [Distributing Extensions](https://jupyter-notebook.readthedocs.io/en/stable/examples/Notebook/Distributing%20Jupyter%20Extensions%20as%20Python%20Packages.html)
page of the documentation.

This notebook extension adds a "Download as tarball" file option 
to the notebook.

## module contents

See [the documentation](https://jupyter-notebook.readthedocs.io/en/stable/examples/Notebook/Distributing%20Jupyter%20Extensions%20as%20Python%20Packages.html)
for source of example.

Import the module from Jupyter notebook:

```
import magic_octo_py as mop
```



## building

To build with Python 2:

```
python2 setup.py install
```

To build with Python 3:

```
python3 setup.py install
```

Optional: specify your python as needed - e.g., with conda in a Travis container, or on Homebrew, or etc.

## testing

To run the tests, you will need nose.
From the project directory, run:

```
nosetets
```

This will run all tests in the `tests/` directory.

## continuous integration (CI) with travis

The `.travis.yml` file runs the Travis tests by using the [tox test automation library](https://tox.readthedocs.io/en/latest/). tox sets up and configures tests for different python versions/compilations/system configurations on Travis.
