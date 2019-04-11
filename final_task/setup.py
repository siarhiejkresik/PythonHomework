from os import path
from setuptools import setup

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md')) as f:
    long_description = f.read()

setup(
    name='calc',
    version='0.1.0',
    description='A pure-python command-line calculator',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/siarhiejkresik/PythonHomework',
    author='Siarhiej Kresik',
    author_email='siarhiej.kresik@gmail.com',
    keywords='calculator calc cli',
    python_requires='>=3.6'
)
