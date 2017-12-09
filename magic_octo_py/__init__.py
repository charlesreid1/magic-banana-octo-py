import os.path as osp

pkg_dir = osp.abspath(osp.dirname(__file__))
data_dir = osp.join(pkg_dir, 'data')

__version__ = '0.14dev'

print("ohai this is the banana_octo_pi package")


# Jupyter Extension points
def _jupyter_nbextension_paths():
    return [dict(
        section="notebook",
        # the path is relative to the `my_fancy_module` directory
        src="static",
        # directory in the `nbextension/` namespace
        dest="magic_octo_py",
        # _also_ in the `nbextension/` namespace
        require="magic_octo_py/index")]

