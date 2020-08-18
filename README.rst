.. image:: https://api.cirrus-ci.com/github/pyscaffold/pyscaffoldext-pyproject.svg?branch=master
    :alt: Built Status
    :target: https://cirrus-ci.com/github/pyscaffold/pyscaffoldext-pyproject
.. image:: https://img.shields.io/coveralls/github/pyscaffold/pyscaffoldext-pyproject/master.svg
    :alt: Coveralls
    :target: https://coveralls.io/r/pyscaffold/pyscaffoldext-pyproject
.. image:: https://img.shields.io/pypi/v/pyscaffoldext-pyproject.svg
    :alt: PyPI-Server
    :target: https://pypi.org/project/pyscaffoldext-pyproject

=======================
pyscaffoldext-pyproject
=======================

.. warning::
   **DEPRECATED**: PyScaffold v4 supports ``pyproject.toml``
   out-of-the-box, without the help of extensions.
   Migration to the newest version in recommended, since it offers better
   support for `PEP 517`_ and `PEP 518`_.


This is a simple PyScaffold extension which serves as a blueprint.
It's sole purpose is to create a ``pyproject.toml`` file according to `PEP 518`_.
This extension was bootstrapped with PyScaffold's `custom-extension`_::

    putup pyscaffoldext-pyproject --custom-extension

Read more about creating an extension under http://pyscaffold.org/.

Usage
=====

Just install this package with ``pip install pyscaffoldext-pyproject``
and note that ``putup -h`` shows a new option ``--pyproject``.
Using this will create a default ``pyproject.toml``.

.. _custom-extension: https://github.com/pyscaffold/pyscaffoldext-custom-extension
.. _PEP 517: https://www.python.org/dev/peps/pep-0517/
.. _PEP 518: https://www.python.org/dev/peps/pep-0518/
