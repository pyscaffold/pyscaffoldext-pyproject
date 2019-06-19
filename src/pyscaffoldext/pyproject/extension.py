# -*- coding: utf-8 -*-
"""
Implementation of a simple extension that additionally
adds the file pyproject.toml
"""
from pyscaffold.api import Extension, helpers

from .templates import pyproject_toml

__author__ = "Florian Wilhelm"
__copyright__ = "Florian Wilhelm"
__license__ = "mit"


class Pyproject(Extension):
    """Generate pyproject.toml"""
    def activate(self, actions):
        """Activate extension

        Args:
            actions (list): list of actions to perform

        Returns:
            list: updated list of actions
        """
        return self.register(
            actions,
            self.add_pyproject_toml,
            after='define_structure')

    def add_pyproject_toml(self, struct, opts):
        """Add the pyproject.toml file

        Args:
            struct (dict): project representation as (possibly) nested
                :obj:`dict`.
            opts (dict): given options, see :obj:`create_project` for
                an extensive list.

        Returns:
            struct, opts: updated project representation and options
        """
        if opts['update'] and not opts['force']:
            return struct, opts
        file = [opts['project'], 'pyproject.toml']
        content = pyproject_toml(opts)
        struct = helpers.ensure(struct, file, content)
        return struct, opts
