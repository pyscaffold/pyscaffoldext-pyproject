#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Setup file for PyScaffold's pyproject extension.

    This file was generated with PyScaffold 3.0.3.
    PyScaffold helps you to put up the scaffold of your new Python project.
    Learn more under: http://pyscaffold.org/
"""

import sys
from setuptools import setup

# Register the entry_point so that PyScaffold finds this extension
entry_points = """
[pyscaffold.cli]
pyproject = pyscaffoldext.pyproject.extension:PyProject
"""


def setup_package():
    needs_sphinx = {'build_sphinx', 'upload_docs'}.intersection(sys.argv)
    sphinx = ['sphinx'] if needs_sphinx else []
    setup(setup_requires=['pyscaffold>=3.0a0,<3.1a0'] + sphinx,
          entry_points=entry_points,
          use_pyscaffold=True)


if __name__ == "__main__":
    setup_package()
