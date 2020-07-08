# -*- coding: utf-8 -*-
"""
Templates for all files this extension provides
"""
import os
import string
from pkg_resources import resource_string


def get_template(name):
    """Retrieve the template by name

    Args:
        name: name of template

    Returns:
        :obj:`string.Template`: template
    """
    file_name = "{name}.template".format(name=name)
    data = resource_string(__name__, file_name)
    # we assure that line endings are converted to '\n' for all OS
    data = data.decode(encoding="utf-8").replace(os.linesep, "\n")
    return string.Template(data)


def pyproject_toml(opts):
    """Template of pyproject.toml

    Args:
        opts: mapping parameters as dictionary

    Returns:
        str: file content as string
    """
    template = get_template("pyproject_toml")
    return template.substitute(opts)
