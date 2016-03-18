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
        # This is to work around issue #16, that occured when the exception
        # value was being passed as a string.
        if isinstance(ev, str):
            ev = ec(ev)
        stdout = sys.stdout
        sys.stdout = sys.__stdout__
        sys.stderr.write('\n- TRACEBACK --------------------------------------------------------------------\n')
        traceback.print_exception(ec, ev, tb)
        sys.stderr.write('--------------------------------------------------------------------------------\n')
        try:
            try:
                # ipython >= 1.0
                from IPython.terminal.ipapp import TerminalIPythonApp
                app = TerminalIPythonApp.instance()
                app.initialize(argv=['--no-banner'])
                p = IPython.core.debugger.Pdb(app.shell.colors)
            except ImportError:
                try:
                    # 0.11 <= ipython <= 0.13
                    ip = IPython.core.ipapi.get()
                    p = IPython.core.debugger.Pdb(ip.colors)
                except AttributeError:
                    # ipython <= 0.10
                    shell = IPython.Shell.IPShell(argv=[''])
                    ip = IPython.ipapi.get()
                    p = IPython.Debugger.Pdb(ip.options.colors)

            p.reset()
            # inspect.getinnerframes() returns a list of frames information
            # from this frame to the one that raised the exception being
            # treated
            frame, filename, line, func_name, ctx, idx = inspect.getinnerframes(tb)[-1]
            p.interaction(frame, tb)
        finally:
            sys.stdout = stdout
