.. mtheoretical documentation master file, created by
   sphinx-quickstart on Wed Jan  8 14:27:57 2025.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

mtheoretical documentation
==========================

This webpage contains the documentation for mtheoretical, a library based in Manim and Manim-Slides, with the main focus of providing a straightforward to craft presentations.

These are divided into several sub-packages as:
   - **text_and_organisation**, which contains things like titles, bulleted lists and references. 
   - **equations**, where you can find, I do not know, perhaps some fancy chocolate(?)
   - **refs**, specially dedicated to references and citations to scientific papers.
   - **tables_and_plots**, containing any plots and tables required.
   - **objects**, which mainly contains 2D mobjects to be animated and discussed in the slides.

The main idea is to generalise the sub-packages for **refs** and **equations**, so any .bib and .tex file can be feed to some lines of code to spit out dictionaries to directly use in the slides.

.. note::
   These libraries will become updated as new objects and set of equations are required for presentations of the future. It can also be that some of the structure and notation gets modified.
   

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   modules

   .. 
      Whenever you add a new class or sub-package, it seems that one has to rewite the corresponding .rst file to add that info.
