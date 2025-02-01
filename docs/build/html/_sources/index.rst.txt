.. Beanim documentation documentation master file, created by
   sphinx-quickstart on Sat Feb  1 18:33:17 2025.
   
Beanim documentation
====================

This webpage contains the documentation for beanim (beamer + manim), a (personal) library based in `Manim <https://docs.manim.community/en/stable/>`_ and `Manim-Slides <https://manim-slides.eertmans.be/latest/>`_, with the main focus of providing a straightforward way to craft presentations. Close to the totality of the contents of this library contains objects, its animations and equations related to `String Cosmology Presentations <https://panopepino.github.io/web_page/main_page/slides.html>`_. But the underlying idea is to offer a collection of elements to easily craft new slides with all previous creations gathered in the same libraries. 

These are divided into several sub-packages as:
   - **text_and_organisation**, which contains things like titles, bulleted lists and references. 
   - **equations**, where you can find, I do not know, perhaps some fancy chocolate(?)
   - **tables_and_plots**, containing any plots and tables required.
   - **objects**, which mainly contains 2D mobjects to be animated and discussed in the slides.

The main idea is to generalise the sub-packages for **refs** and **equations**, so any .bib and .tex file can be feed to some lines of code to spit out dictionaries to directly use in the slides.

.. note::
   These libraries will become updated as new objects and set of equations are required for presentations of the future. It can also be that some of the structure and notation gets modified.

.. attention::

   - Class Bubble lacks a B-field in the background to be added. Animation of the B-field surfing the brane will be changed.
   - Tools still require some work to avoid issues with \begin{align} and stuff. 
   - Extract references tool is still required.
   - Think of a way to remove the animation_overrides{} thing. 
   


.. toctree::
   :maxdepth: 2
   :caption: Contents of the package:

   beanim

   .. 
      Whenever you add a new class or sub-package, it seems that one has to rewite the corresponding .rst file to add that info.

.. note::

   Thanks to Uwezi, Abulafia, Jeertmans and the Manim Discord for all the help provided during these years. This humble library would not be possible without them.


