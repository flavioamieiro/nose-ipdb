# -*- coding: utf-8 -*-

from setuptools import setup


setup(
    name='ipdbplugin',
    version='1.4.4',
    url='http://github.com/flavioamieiro/nose-ipdb/tree/master',
    maintainer='Flavio Amieiro',
    maintainer_email='amieiro.flavio@gmail.com',
    description='Nose plugin to use iPdb instead of Pdb when tests fail',
    long_description=(
        """What about running nose with a smarter interactive debugger?

        Use this and *never* risk yourself forgetting `import ipdb; ipdb.set_trace()` in your code again!

        This plugin is 99.99% based on nose's builtin debug plugin.

        If you have any ideas about how to improve it, come and fork the code at http://github.com/flavioamieiro/nose-ipdb
        """
    ),
    install_requires=['nose', 'ipython'],
    license='GNU LGPL',
    keywords='test unittest nose nosetests plugin debug ipdb ipython',
    py_modules=['ipdbplugin'],
    entry_points={
        'nose.plugins.0.10': [
            'ipdbplugin = ipdbplugin:iPdb'
        ]
    },
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
