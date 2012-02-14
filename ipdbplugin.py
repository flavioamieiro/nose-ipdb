"""
This plugin provides ``--ipdb`` and ``--ipdb-failures`` options. The ``--ipdb``
option will drop the test runner into pdb when it encounters an error. To
drop into pdb on failure, use ``--ipdb-failures``.
"""

import sys
import inspect
import traceback
from nose.plugins.base import Plugin

class iPdb(Plugin):
    """
    Provides --ipdb and --ipdb-failures options that cause the test runner to
    drop into ipdb if it encounters an error or failure, respectively.
    """
    enabled_for_errors = False
    enabled_for_failures = False
    score = 5 # run last, among builtins

    def options(self, parser, env):
        """Register commandline options.
        """
        parser.add_option(
            "--ipdb", action="store_true", dest="ipdbErrors",
            default=env.get('NOSE_IPDB', False),
            help="Drop into ipdb on errors")
        parser.add_option(
            "--ipdb-failures", action="store_true",
            dest="ipdbFailures",
            default=env.get('NOSE_IPDB_FAILURES', False),
            help="Drop into ipdb on failures")

    def configure(self, options, conf):
        """Configure which kinds of exceptions trigger plugin.
        """
        self.conf = conf
        self.enabled = options.ipdbErrors or options.ipdbFailures
        self.enabled_for_errors = options.ipdbErrors
        self.enabled_for_failures = options.ipdbFailures

    def addError(self, test, err):
        """Enter ipdb if configured to debug errors.
        """
        if not self.enabled_for_errors:
            return
        self.debug(err)

    def addFailure(self, test, err):
        """Enter ipdb if configured to debug failures.
        """
        if not self.enabled_for_failures:
            return
        self.debug(err)

    def debug(self, err):
        import IPython
        ec, ev, tb = err
        stdout = sys.stdout
        sys.stdout = sys.__stdout__
        sys.stderr.write('\n- TRACEBACK --------------------------------------------------------------------\n')
        traceback.print_exception(*err)
        sys.stderr.write('--------------------------------------------------------------------------------\n')
        try:
            # The IPython API changed a bit so we should
            # support the new version
            if hasattr(IPython, 'InteractiveShell'):
                shell = IPython.InteractiveShell()
                ip = IPython.core.ipapi.get()
                p = IPython.core.debugger.Pdb(ip.colors)
            # and keep support for older versions
            else:
                shell = IPython.Shell.IPShell(argv=[''])
                ip = IPython.ipapi.get()
                p = IPython.Debugger.Pdb(ip.options.colors)

            p.reset()
            # inspect.trace() returns a list of frame information from this
            # frame to the one that raised the exception being treated
            frame, filename, line, func_name, ctx, idx = inspect.trace()[-1]
            p.interaction(frame, tb)
        finally:
            sys.stdout = stdout
