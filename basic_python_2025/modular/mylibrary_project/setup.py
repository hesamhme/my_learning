from setuptools import setup, find_packages

setup(
    name='mylibrary',
    version='1.0.0',
    description='A simple library management system',
    author='hxh',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'mylibrary = main:main'
        ],
    },
)
