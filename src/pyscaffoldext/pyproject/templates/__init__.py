# -*- coding: utf-8 -*-
"""
Templates for all files this extension provides
"""
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
    data = resource_string("pyscaffoldext.pyproject.templates",
                           file_name)
    return string.Template(data.decode("UTF-8"))


def pyproject_toml(opts):
    """Template of pyproject.toml

    Args:
        opts: mapping parameters as dictionary

    Returns:
        str: file content as string
    """
    template = get_template("pyproject_toml")
    return template.substitute(opts)
