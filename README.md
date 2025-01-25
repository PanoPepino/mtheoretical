ABOUT THIS REPOSITORY

- This repository contains v2.0 of mtheoretical libraries. It is an improved version, with more straightforward commands and a better folder and files organisation, with more optional parameters and the cleanest documentation I am able to achieve.

- These libraries are supposed to be used with [manim-slides](https://manim-slides.eertmans.be/latest/) and [manim](https://www.manim.community). 

- These files contain my personal libraries to generate slide presentations about my scientific research. You can find examples of the results [here](https://panopepino.github.io/web_page/main_page/slides.html) . 

- The documentation webpage (ADD HYPERLINK) includes information about the characteristics and examples of each of the classes and their methods included in these libraries. The main reason of its existence is to easily access all objects of these libraries when crafting slides.

- TO DO:

- Elaborate on the Readme.txt
- Create package to be installed.
- Include old animations:
    - Diagrams
    - Pulling strings and bending branes.
- Code new animations:
    - (Non)-Normalisable modes and the bubble expanding.
    - Smooth transition between global and Poincaré coordinates for the bubble.
- General Python code to write:
    - Code to extract refs in the form of a dictionary {hep.th: '[names, hep.number]'}
    - Rewrite code to extract all the equations of a .tex file in the form of a dictionary {eq_label: 'equation'}, but taking into account
    things like \begin{split}, \begin{aligned} and so on. At the moment it only works with regular \begin{equation} enviroment.
