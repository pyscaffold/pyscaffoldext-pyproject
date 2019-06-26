# -*- coding: utf-8 -*-
from os.path import exists as path_exists

from pyscaffold.api import create_project
from pyscaffold.cli import parse_args, process_opts
from pyscaffold.utils import chdir

from pyscaffoldext.pyproject.extension import Pyproject

EXT_FLAG = "--pyproject"


def test_add_custom_extension(tmpfolder):
    opts = {"package": "my_extension", "project": "my_project",
            "extensions": [Pyproject("custom_ext")]}
    opts = process_opts(opts)
    create_project(opts)
    assert path_exists("my_project/src/my_extension/extension.py")


def test_add_custom_extension_with_namespace(tmpfolder):
    args = ["--namespace", "ns", EXT_FLAG, "my_project"]
    opts = parse_args(args)
    opts = process_opts(opts)
    create_project(opts)
    assert path_exists("my_project/src/ns/my_extension/extension.py")


def test_add_custom_extension_with_namespace_2(tmpfolder):
    args = ["--namespace", "ns1.ns2", EXT_FLAG, "my_project"]
    opts = parse_args(args)
    opts = process_opts(opts)
    create_project(opts)
    assert path_exists("my_project/src/ns1/ns2/my_project/extension.py")


def test_generated_extension_flake8(tmpfolder, venv_run):
    args = [EXT_FLAG, "my_project"]

    opts = parse_args(args)
    create_project(opts)

    with chdir("my_project"):
        assert '' == venv_run("flake8")
        venv_run("python setup.py install")

    venv_run("putup {ext_flag} the_actual_project".format(EXT_FLAG))
    assert path_exists("the_actual_project/setup.cfg")

    with chdir("the_actual_project"):
        assert '' == venv_run("flake8")
