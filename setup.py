from __future__ import print_function
from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand
import io
import codecs
import os
import sys

here = os.path.abspath(os.path.dirname(__file__))

def read(*filenames, **kwargs):
    encoding = kwargs.get('encoding', 'utf-8')
    sep = kwargs.get('sep', '\n')
    buf = []
    for filename in filenames:
        with io.open(filename, encoding=encoding) as f:
            buf.append(f.read())
    return sep.join(buf)

long_description = read('README.md', 'CHANGES.md')

setup(
    name='dspy',
    version='0.1',
    url='http://github.com/nils-werner/dspy/',
    license='MIT',
    author='Nils Werner',
    tests_require=['Nose'],
    install_requires=['SciPy>=0.10.1',
                    'NumPy>=1.0',
                    ],
    author_email='nils.werner@gmail.com',
    description='Digital Signal Processing tools for Python',
    long_description=long_description,
    packages=['dspy'],
    include_package_data=True,
    platforms='any',
    test_suite='nose.collector',
    classifiers = [
        'Programming Language :: Python',
        'Development Status :: 4 - Beta',
        'Natural Language :: English',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        ],
    extras_require={
        'testing': ['Nose'],
    }
)