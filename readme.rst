Template Inheritance Helper
===========================

.. warning::

   This is a **work** **in** **progress**.

Installation
------------

Using pip::

    pip install django-template-inheritance-helper

If you do not have ``pip`` installed, follow
`these instructions <https://pip.pypa.io/en/latest/installing.html#install-pip>`_.

Then, add ``template_inheritance_helper`` to the ``INSTALLED_APPS``
list in your project's ``settings.py``.

Commands
--------

``block_info BLOCK_NAME TEMPLATE_PATH``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Get a list of templates that either override or are overridden by the
block name you specify.

``template_info TEMPLATE_PATH``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Get a hierarchical chart explaining which templates were used to compose
each block of a given template.
