#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from os.path import exists as path_exists

from pyscaffold.api import create_project
from pyscaffold.cli import run

from pyscaffoldext.pyproject.extension import Pyproject


def test_create_project_with_pyproject(tmpfolder):
    # Given options with the pyproject extension,
    opts = dict(project="proj",
                extensions=[Pyproject('pyproject')])

    # when the project is created,
    create_project(opts)

    # then pyproject files should exist
    assert path_exists("proj/pyproject.toml")


def test_create_project_without_pyproject(tmpfolder):
    # Given options without the pyproject extension,
    opts = dict(project="proj")

    # when the project is created,
    create_project(opts)

    # then pyproject files should not exist
    assert not path_exists("proj/pyproject.toml")


def test_cli_with_pyproject(tmpfolder):
    # Given the command line with the pyproject option,
    sys.argv = ["pyscaffold", "--pyproject", "proj"]

    # when pyscaffold runs,
    run()

    # then pyproject files should exist
    assert path_exists("proj/pyproject.toml")


def test_cli_without_pyproject(tmpfolder):
    # Given the command line without the pyproject option,
    sys.argv = ["pyscaffold", "proj"]

    # when pyscaffold runs,
    run()

    # then pyproject files should not exist
    assert not path_exists("proj/pyproject.toml")
