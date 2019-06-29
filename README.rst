.. image:: https://travis-ci.org/pyscaffold/pyscaffoldext-pyproject.svg?branch=master
    :target: https://travis-ci.org/pyscaffold/pyscaffoldext-pyproject
.. image:: https://img.shields.io/coveralls/github/pyscaffold/pyscaffoldext-pyproject/master.svg
    :alt: Coveralls
    :target: https://coveralls.io/r/pyscaffold/pyscaffoldext-pyproject
.. image:: https://img.shields.io/pypi/v/pyscaffoldext-pyproject.svg
    :alt: PyPI-Server
    :target: https://pypi.org/project/pyscaffoldext-pyproject

=======================
pyscaffoldext-pyproject
=======================


This is a simple PyScaffold extension which serves as a blueprint.
It's sole purpose is to create a ``pyproject.toml`` file according to `[PEP 518]`_.
This extension was bootstrapped with PyScaffold's `custom-extension`_::

    putup pyscaffoldext-pyproject --custom-extension

Read more about creating an extension under http://pyscaffold.org/.

Usage
=====

Just install this package with ``pip install pyscaffoldext-pyproject``
and note that ``putup -h`` shows a new option ``--pyproject``.
Using this will create a default ``pyproject.toml``.

.. _custom-extension: https://github.com/pyscaffold/pyscaffoldext-custom-extension
.. _[PEP 518]: https://www.python.org/dev/peps/pep-0518/
