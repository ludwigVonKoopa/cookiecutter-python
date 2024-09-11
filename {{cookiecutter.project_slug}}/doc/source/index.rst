Welcome to {{ cookiecutter.project_name }}'s documentation!
{{"=" * (28 + cookiecutter.project_name|length)}}

.. toctree::
   :maxdepth: 1
   :caption: Contents:

   readme
   installation
   usage
   {% if cookiecutter.create_matplotlib_gallery -%}
   gallery/index
   {%- endif %}
   changelog
   api

Indices and tables
==================
* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
