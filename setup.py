# coding=utf-8
from setuptools import find_packages
from setuptools import setup

import imagify

with open('README.rst') as readme:
    long_description = readme.read()

setup(
    name="imagify-python",
    version=imagify.__version__,
    description="Imagify API wrapper",
    long_description=long_description,
    author='Jean-Baptiste Marchand-Arvier',
    author_email='jeanbaptiste@wp-rocket.me',
    license="MIT License",
    url='',
    keywords='imagify, python',
    classifiers=[],
    packages=find_packages(),
    include_package_data=True,
    install_requires=['requests>=2.9.1'],
    zip_safe=False
)
