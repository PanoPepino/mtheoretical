ABOUT THIS REPOSITORY

- This repository contains v1.0 of beanim (Beamer + Manim) libraries. It is an improved version, with more straightforward commands and a better folder and files organisation, with more optional parameters and the cleanest documentation I am able to achieve.

- These libraries are supposed to be used with [manim-slides](https://manim-slides.eertmans.be/latest/) and [manim](https://www.manim.community).

- The main idea of this package is to offer a beamer-like experience. Are you tired of beamer stiffness? Experience its wonders when used with Manim and Manim Slides.

- These files contains to different, but useful approaches:

    - A small, yet practical set of tools:
        - To extract equations and references from .tex and .bib files.
        - Simple structures to organise your slides with Titles, bulleted lists, general equations, etc.

    - And then my personal libraries to generate animations to present my scientific research. 
    
You can find examples of the overall results [here](https://panopepino.github.io/web_page/main_page/slides.html).

- The [documentation webpage](https://panopepino.github.io/beanim/) includes information about the characteristics and examples of each of the classes and their methods included in these libraries. The main reason of its existence is to easily access all objects of these libraries when crafting slides.

-----------------------------------------------------------------------

In order to install this library, do the following:

- clone this repository in your desired folder.
- in your terminal, navigate to that folder and pip install .


- TO DO:

- Include old animations:
    - Diagrams (gravity and EM)
    - Pulling strings and bending branes.

- Code new animations:
    - (Non)-Normalisable modes and the bubble expanding.
    - Smooth transition between global and Poincaré coordinates for the bubble.

- General Python code to write:
    - Code to extract refs in the form of a dictionary {hep.th: '[names, hep.number]'}
    - Rewrite code to extract all the equations of a .tex file in the form of a dictionary {eq_label: 'equation'}, but taking into account
    things like \begin{split}, \begin{aligned} and so on. At the moment it only works with regular \begin{equation} enviroment.
    - Think how to choose among equations in the package and equations from outside.

- Changes to make in webpage:

    - Add required configuration in the conf.py file to automatically remove Submodule headings, Module contents at the end of the page, and any name displayed as pkg.sub_pkg.module.