from __future__ import print_function
import sphinx
import sphinx.apidoc
from setuptools import setup, find_packages, Command
import io
import os


class SphinxCommandProxy(Command):
    user_options = []
    description = 'sphinx'

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        # metadata contains information supplied in setup()
        metadata = self.distribution.metadata
        src_dir = (self.distribution.package_dir or {'': ''})['']
        src_dir = os.path.join(os.getcwd(),  src_dir)

        # Build docs from docstrings in *.py files
        sphinx.apidoc.main(
            ['', '-o', os.path.join('docs', 'source'), src_dir])

        # Build the doc sources
        sphinx.main(['', '-c', 'docs',
                     '-D', 'project=' + metadata.name,
                     '-D', 'version=' + metadata.version,
                     '-D', 'release=' + metadata.version,
                     os.path.join('docs', 'source'),
                     os.path.join('docs', 'build')])


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
    install_requires=[
        'SciPy>=0.9.0',
        'NumPy>=1.6.0',
        'matplotlib>=1.0.0',
        'pyaudio>=0.2.4',
        'spectrum>=0.5.6',
        'pymf>=0.1.9',
        'scikits.audiolab>=0.11.0',
    ],
    author_email='nils.werner@gmail.com',
    description='Digital Signal Processing tools for Python',
    long_description=long_description,
    packages=find_packages(),
    include_package_data=True,
    platforms='any',
    test_suite='nose.collector',
    classifiers=[
        'Programming Language :: Python',
        'Development Status :: 3 - Alpha',
        'Natural Language :: English',
        'Environment :: Web Environment',
        'Intended Audience :: Education',
        'Intended Audience :: Information Technology',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Topic :: Multimedia :: Sound/Audio :: Analysis',
        'Topic :: Multimedia :: Sound/Audio :: Sound Synthesis',
    ],
    extras_require={
        'testing': ['Nose'],
    },
    dependency_links=[
        "git+https://github.com/nils-werner/pymf.git#egg=pymf-0.1.9"
    ],
    # Register custom commands
    cmdclass={
        'build_sphinx': SphinxCommandProxy
    }
)
