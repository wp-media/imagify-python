imagify-python
============================

Official Imagify API Wrapper for Python

Installation
------------
To download the latest stable version do a

::

    pip install imagify-python


To install latest development version download the sources on this Github repository and do a

::

    python setup.py install

Usage
-----

.. code:: python

    >>> from imagify import Imagify
    >>> imagify = Imagify('api_key')
    >>> param = dict(ultra=True)
    >>> imagify.upload("/path/to/image.jpg", param)
