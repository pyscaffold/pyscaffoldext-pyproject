.. image:: https://api.cirrus-ci.com/github/pyscaffold/pyscaffoldext-pyproject.svg?branch=master
    :alt: Built Status
    :target: https://cirrus-ci.com/github/pyscaffold/pyscaffoldext-pyproject
.. image:: https://img.shields.io/coveralls/github/pyscaffold/pyscaffoldext-pyproject/master.svg
    :alt: Coveralls
    :target: https://coveralls.io/r/pyscaffold/pyscaffoldext-pyproject

=======================
pyscaffoldext-pyproject
=======================


This is a simple PyScaffold extension which serves as a blueprint.
It's sole purpose is to create a ``pyproject.toml`` file according to `[PEP 518]`_.
This extension was bootstrapped with PyScaffold::

    putup pyscaffoldext-pyproject -p pyproject --namespace pyscaffoldext --no-skeleton

Read more about creating an extension under http://pyscaffold.org/.

Usage
=====

Just install this package with ``pip install pyscaffoldext-pyproject``
and note that ``putup -h`` shows a new option ``--pyproject``.
Using this will create a default ``pyproject.toml``.

.. _[PEP 518]: https://www.python.org/dev/peps/pep-0518/
