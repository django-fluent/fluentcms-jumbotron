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

The jumbotron is rendered with the HTML that Bootstrap prescribes:

.. code-block:: html+django

    <div class="jumbotron">
      <h1>Hello, world!</h1>
      <p>...</p>
      <p><a class="btn btn-primary btn-lg" href="#" role="button">Learn more</a></p>
    </div>

The standard Bootstrap 3 CSS will provide a reasonable styling for this,
which can either be overwritten, or replaced in your own CSS files.
The defaults provided by Bootstap 3 is: https://github.com/twbs/bootstrap-sass/blob/master/assets/stylesheets/bootstrap/_jumbotron.scss

Customizing
-----------

Centering, adding backgrounds, etc.. all happen by adding CSS styling. For example:

.. code-block:: css

    .jumbotron {
      background: url('/static/frontend/images/background.jpg') no-repeat fixed 0 0;
      background-size: cover;
      color: #fff;
      text-align: center;
    }

    .jumbotron .btn {
      margin-top: 12px;  /* For Sass: $padding-base-vertical * 2; */
    }

When you use Sass, you can also override the Sass variables.

Full page width
---------------

To display the Bootstrap Jumbotron full page, you likely need to break out of the container
the ``JumbotronPlugin`` is rendered in. For example, when your page looks like:

.. code-block:: html+django

    <div class="container">
        {% page_placeholder "homepage" title="Homepage" role="m" %}
    </div>

You can change that into:

.. code-block:: html+django

    <div class="container">
        {% page_placeholder "homepage" title="Homepage" role="m" template="pages/placeholders/homepage.html" cachable=1 %}
    </div>

The ``pages/placeholders/homepage.html`` template looks like:

.. code-block:: html+django

    {% for contentitem, html in contentitems %}
      {% if contentitem.plugin.name == 'JumbotronPlugin' %}
        </div>
        {{ html }}
        <div class="container">
      {% else %}
        {{ html }}
      {% endif %}
    {% endfor %}

Note the exact HTML tags depend on your frontend HTML layout.

The ``cachable=1`` flag is a promise that the template always returns the same result for every request.
Otherwise, remove it.

Contributing
------------

If you like this module, forked it, or would like to improve it, please let us know!
Pull requests are welcome too. :-)

.. _django-fluent-contents: https://github.com/edoburu/django-fluent-contents
.. _jumbotron: http://getbootstrap.com/components/#jumbotron
