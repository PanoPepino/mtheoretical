.. Beanim documentation documentation master file, created by
   sphinx-quickstart on Sat Feb  1 18:33:17 2025.

Beanim documentation
====================

This webpage contains the documentation for beanim (beamer + manim), a (personal) library based in `Manim <https://docs.manim.community/en/stable/>`_ and `Manim-Slides <https://manim-slides.eertmans.be/latest/>`_, with the main focus of providing a straightforward way to craft presentations. Close to the totality of the contents of this library contains objects, its animations and equations related to `String Cosmology Presentations <https://panopepino.github.io/web_page/main_page/slides.html>`_. But the underlying idea is to offer a collection of elements to easily craft new slides with all previous creations gathered in the same libraries.

These are divided into several sub-packages as:
   - **text_and_organisation**, which contains things like titles, bulleted lists, equations and references.
   - **tables_and_plots**, containing plots and tables related to string cosmology research.
   - **objects**, which mainly contains 2D mobjects to be animated and discussed in the slides.
   - **templates**, which includes a method to include different slide templates depending on the input.
   - **tools**, where you will find useful code to extract equations from .tex files and references from .bib files.

.. note::
   These libraries will become updated as new objects and set of equations are required for presentations of the future. It can also be that some of the structure and notation gets modified.

.. attention::

   - Class Bubble lacks a B-field in the background to be added. Animation of the B-field surfing the brane will be changed.
   - Extract equation requires work to avoid issues with \\begin{align} and stuff.



.. toctree::
   :maxdepth: 2
   :titlesonly:
   :caption: Contents of the package:

   beanim.text_and_organisation
   beanim.objects
   beanim.tables_and_plots
   beanim.templates
   beanim.tools




.. note::

   Thanks to Uwezi, Abulafia, Jeertmans and the Manim Discord for all the help provided during these years. This humble library would not be possible without them.
