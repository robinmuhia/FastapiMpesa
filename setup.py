#!/usr/bin/env python
from setuptools import find_packages, setup

with open('README.md') as f:
    readme = f.read()

setup(
    name='fastapiMpesa',
    version='0.0.1',
    url='https://github.com/robinmuhia/fastapiMpesa',
    license='BSD',
    author='Robin Mike Muhia',
    author_email='muhiarobinonyancha@gmail.com',
    description='A Safaricom\'s DarajaAPI2.0 Package for FastAPI Applications.',
    long_description=readme,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    zip_safe=False,
    platforms='any',
    install_requires=[
        'FastAPI',
        'requests'
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: FastAPI',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
