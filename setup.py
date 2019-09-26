# coding=utf-8
import os
from setuptools import find_packages
from setuptools import setup

import imagify

with open('README.rst') as readme:
    long_description = readme.read()


def load_requirements():
    folder = os.path.dirname(os.path.realpath(__file__))
    requirements_path = os.path.join(folder, 'requirements.txt')
    with open(requirements_path) as f:
        return f.read().splitlines()


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
    classifiers=[],
    packages=find_packages(),
    include_package_data=True,
    install_requires=load_requirements(),
    zip_safe=False
)
