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
    url='https://github.com/wp-media/imagify-python',
    keywords='imagify, python',
    packages=find_packages(),
    include_package_data=True,
    install_requires=['requests>=2.9.1'],
    zip_safe=False,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 2",
    ],
)
