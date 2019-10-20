# -*- coding: utf-8 -*-
"""
Templates for all files this extension provides
"""
from pyscaffold.templates import get_template


def pyproject_toml(opts):
    """Template of pyproject.toml

    Args:
        opts: mapping parameters as dictionary

    Returns:
        str: file content as string
    """
    template = get_template("pyproject_toml")
    return template.substitute(opts)
