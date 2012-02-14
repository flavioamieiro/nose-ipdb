from setuptools import setup

setup(
    name='ipdbplugin',
    version='1.2',
    url='http://github.com/flavioamieiro/nose-ipdb/tree/master',
    author='Flavio Amieiro',
    author_email = 'amieiro.flavio@gmail.com',
    description = 'Nose plugin to use iPdb instead of Pdb when tests fail',
    long_description = \
    """What about running nose with a smarter interactive debugger?

    Use this and *never* risk yourself forgetting `import pdb; pdb.set_trace()` in your code again!

    This plugin is 99.99% based on nose's builtin debug plugin.

    If you have any ideas about how to improve it, come and fork the code at http://github.com/flavioamieiro/nose-ipdb
    """,
    install_requires=['nose', 'ipython'],
    license = 'GNU LGPL',
    keywords = 'test unittest nose nosetests plugin debug ipdb ipython',
    py_modules = ['ipdbplugin'],
    entry_points = {
        'nose.plugins.0.10': [
            'ipdbplugin = ipdbplugin:iPdb'
            ]
        }
    )
