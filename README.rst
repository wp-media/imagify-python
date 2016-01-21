imagify-python
============================

Official Imagify API Wrapper for Python

Installation
------------
Download the sources on this Github reposityro and do a

::

    python setup.py install

Usage
-----

.. code:: python

    >>> from imagify import Imagify
    >>> imagify = Imagify('api_key')
    >>> param = dict(ultra=True)
    >>> imagify.upload("/path/to/image.jpg", param)
