from setuptools import setup
import os
import sys

_here = os.path.abspath(os.path.dirname(__file__))

if sys.version_info[0] < 3:
    with open(os.path.join(_here, 'README.rst')) as f:
        long_description = f.read()
else:
    with open(os.path.join(_here, 'README.rst'), encoding='utf-8') as f:
        long_description = f.read()

version = {}
with open(os.path.join(_here, 'UrlSnippet', 'version.py')) as f:
    exec(f.read(), version)

setup(
    name='urlsnippet',
    version=version['__version__'],
    description=('Python rest app for requesting text snippet from a url.'),
    long_description=long_description,
    author='Zack Greenberg',
    author_email='icompute@protonmail.com',
    url='https://github.com/ZacharyIG/UrlSnippet',
    license='Apache-2.0',
    packages=['urlsnippet'],
    include_package_data=True,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Science/Research',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.6'],
)
