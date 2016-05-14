fluentcms-jumbotron
===================

.. image:: https://img.shields.io/travis/edoburu/fluentcms-jumbotron/master.svg?branch=master
    :target: http://travis-ci.org/edoburu/fluentcms-jumbotron
.. image:: https://img.shields.io/pypi/v/fluentcms-jumbotron.svg
    :target: https://pypi.python.org/pypi/fluentcms-jumbotron/
.. image:: https://img.shields.io/pypi/dm/fluentcms-jumbotron.svg
    :target: https://pypi.python.org/pypi/fluentcms-jumbotron/
.. image:: https://img.shields.io/badge/wheel-yes-green.svg
    :target: https://pypi.python.org/pypi/fluentcms-jumbotron/
.. image:: https://img.shields.io/pypi/l/fluentcms-jumbotron.svg
    :target: https://pypi.python.org/pypi/fluentcms-jumbotron/
.. image:: https://img.shields.io/codecov/c/github/edoburu/fluentcms-jumbotron/master.svg
    :target: https://codecov.io/github/edoburu/fluentcms-jumbotron?branch=master

Displaying a Bootstrap 3 Jumbotron_ in a page


Installation
============

First install the module, preferably in a virtual environment. It can be installed from PyPI:

.. code-block:: bash

    pip install fluentcms-jumbotron

First make sure the project is configured for django-fluent-contents_.

Then add the following settings:

.. code-block:: python

    INSTALLED_APPS += (
        'fluentcms_jumbotron',
    )

    FLUENT_CONTENTS_PLACEHOLDER_CONFIG = {
        'slot name': {
            'plugins': ('JumbotronPlugin', ...),
        },
    }

The database tables can be created afterwards:

.. code-block:: bash

    ./manage.py migrate


Frontend styling
================

The jumbotron is renderd with the HTML that Bootstrap prescribes:

.. code-block:: html+django

    <div class="jumbotron">
      <h1>Hello, world!</h1>
      <p>...</p>
      <p><a class="btn btn-primary btn-lg" href="#" role="button">Learn more</a></p>
    </div>

The standard Bootstrap 3 CSS will provide a reasonable styling for this,
which can either be overwritten, or replaced in your own CSS files.


Contributing
------------

If you like this module, forked it, or would like to improve it, please let us know!
Pull requests are welcome too. :-)

.. _django-fluent-contents: https://github.com/edoburu/django-fluent-contents
.. _jumbotron: http://getbootstrap.com/components/#jumbotron
