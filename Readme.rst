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
The package also installs two command-line-interface (CLI) scripts,
``igorbinarywave`` and ``igorpackedexperiment`` which can be used to dump files
to stdout. You should install the ``[CLI]`` extra for them to fully work::

    pip install igor2[CLI]

For details on their usage, use the ``--help`` option.  For example::

    igorbinarywave --help


Testing
-------

Run internal unit tests by cloning the repository and installing the
``[dev]`` extra and then running the tests::

    git clone https://github.com/AFM-analysis/igor2.git
    cd igor2
    pip install -e .[dev]
    pytest


Licence
-------

This project is distributed under the `GNU Lesser General Public
License Version 3`_ or greater, see the ``LICENSE`` file distributed
with the project for details.


.. _GNU Lesser General Public License Version 3:
    http://www.gnu.org/licenses/lgpl.txt


.. |PyPI Version| image:: https://img.shields.io/pypi/v/igor2.svg
   :target: https://pypi.python.org/pypi/igor2
.. |Build Status| image:: https://img.shields.io/github/actions/workflow/status/AFM-analysis/igor2/check.yml?branch=master
   :target: https://github.com/AFM-analysis/igor2/actions?query=workflow%3AChecks
.. |Coverage Status| image:: https://img.shields.io/codecov/c/github/AFM-analysis/igor2/master.svg
   :target: https://codecov.io/gh/AFM-analysis/igor2
