import os

from nose.plugins import Plugin


class DisableDocstring(Plugin):
    """Tells unittest not to use docstrings as test names."""

    name = 'enable-docstring'

    def options(self, parser, env=os.environ):
        super(DisableDocstring, self).options(parser, env=env)
        parser.add_option('--enable-docstring', action="store_false", default=True,
                          help=DisableDocstring.__doc__)

    def configure(self, options, conf):
        super(DisableDocstring, self).configure(options, conf)
        if options.enable_docstring:
            self.enabled = True
        if not self.enabled:
            return

    def describeTest(self, test):
        return str(test)
