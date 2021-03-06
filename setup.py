"""
MAGIC OCTO PY
A simple Jupyter/IPython magic package

See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
https://github.com/ipython-contrib/jupyter_contrib_nbextensions
https://jupyter-notebook.readthedocs.io/en/stable/examples/Notebook/Distributing%20Jupyter%20Extensions%20as%20Python%20Packages.html
"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages

# To use a consistent encoding
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
#import pypandoc
#long_description = pypandoc.convert('README.md', 'rst')
#long_description = open('README.md').read()
long_description = 'this is a simple Python project, and this is a long description'

setup(
    name='magic_octo_py',

    # Versions should comply with PEP440.  For a discussion on single-sourcing
    # the version across setup.py and the project code, see
    # https://packaging.python.org/en/latest/single_source_version.html
    version='1.0',

    description='a simple Jupyter/IPython notebook extension',
    long_description=long_description,

    # The project's main homepage.
    url='https://github.com/charlesreid1/magic-octo-py',

    # Author details
    author='charles reid',
    author_email='not_one_email@notevenonce.com',

    # Choose your license
    license='MIT',

    ## You can just specify the packages manually here if your project is
    ## simple. Or you can use find_packages().
    #packages=(['magic_octo_py']),
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),

    # Alternatively, if you want to distribute just a my_module.py, uncomment
    # this:
    #   py_modules=["my_module"],

    # List run-time dependencies here.  These will be installed by pip when
    # your project is installed. For an analysis of "install_requires" vs pip's
    # requirements files see:
    # https://packaging.python.org/en/latest/requirements.html
    install_requires=['numpy'],

    ## List additional groups of dependencies here (e.g. development
    ## dependencies). You can install these using the following syntax,
    ## for example:
    ## $ pip install -e .[dev,test]
    #extras_require={
    #    'dev': ['check-manifest'],
    #    'test': ['coverage'],
    #},

    # If there are data files included in your packages that need to be
    # installed, specify them here.  If using Python 2.6 or less, then these
    # have to be included in MANIFEST.in as well.
    package_data={
        'magic_octo_py': ['static/smoke.css',
                          'static/index.js']
    },

    ### # Although 'package_data' is the preferred approach, in some case you may
    ### # need to place data files outside of your packages. See:
    ### # http://docs.python.org/3.4/distutils/setupscript.html#installing-additional-files # noqa
    ### # In this case, 'data_file' will be installed into '<sys.prefix>/my_data'
    ### data_files=[('my_data', ['data/data_file'])],

    ### # To provide executable scripts, use entry points in preference to the
    ### # "scripts" keyword. Entry points provide cross-platform support and allow
    ### # pip to create the appropriate form of executable for the target platform.
    ### entry_points={
    ###     'console_scripts': [
    ###         'sample=sample:main',
    ###     ],
    ### },
)
