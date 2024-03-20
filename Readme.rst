Igor2
=====

|PyPI Version| |Build Status| |Coverage Status|


Python parser for Igor Binary Waves (``.ibw``) and Packed Experiment
(``.pxp``) files written by WaveMetrics' IGOR Pro software.

Igor2 is the continuation of the inactive
`igor <https://github.com/wking/igor>`_ project.


Installation
------------
You can install igor2 via pip::

    pip install igor2


Usage
-----
This package is a direct replacement of `igor`. Your scripts should work
without any issues if you replace::


    import igor

with::

    import igor2 as igor


See the docstrings and unit tests for examples using the Python API.

CLI
---
The package also installs two scripts, ``igorbinarywave`` and
``igorpackedexperiment`` which can be used to dump files to stdout.
For details on their usage, use the ``--help`` option.  For example::

    igorbinarywave --help


Testing
-------

Run internal unit tests by cloning the repository and installing the
test requirements ``pytest`` and then running the tests::

    git clone https://github.com/AFM-analysis/igor2.git
    cd igor2
    pip install -e .[dev]
    pytest


Licence
-------

This project is distributed under the `GNU Lesser General Public
License Version 3`_ or greater, see the ``LICENSE`` file distributed
with the project for details.


.. _layman: http://layman.sourceforge.net/
.. _wtk overlay: http://blog.tremily.us/posts/Gentoo_overlay/
.. _Debian: http://www.debian.org/
.. _Gentoo: http://www.gentoo.org/
.. _NumPy: http://numpy.scipy.org/
.. _Matplotlib: http://matplotlib.sourceforge.net/
.. _Nose: http://somethingaboutorange.com/mrl/projects/nose/
.. _Git: http://git-scm.com/
.. _homepage: http://blog.tremily.us/posts/igor/
.. _pip: http://pypi.python.org/pypi/pip
.. _igor.py: http://pypi.python.org/pypi/igor.py
.. _GNU Lesser General Public License Version 3:
    http://www.gnu.org/licenses/lgpl.txt
.. _update-copyright: http://blog.tremily.us/posts/update-copyright/


.. |PyPI Version| image:: https://img.shields.io/pypi/v/igor2.svg
   :target: https://pypi.python.org/pypi/igor2
.. |Build Status| image:: https://img.shields.io/github/actions/workflow/status/AFM-analysis/igor2/check.yml?branch=master
   :target: https://github.com/AFM-analysis/igor2/actions?query=workflow%3AChecks
.. |Coverage Status| image:: https://img.shields.io/codecov/c/github/AFM-analysis/igor2/master.svg
   :target: https://codecov.io/gh/AFM-analysis/igor2
