import importlib

__all__= ['import_template']

#The following lines allow you to choose between different templates for each of the objects of the presentation.
#If you choose no template from the list, manim will render the default configuration (B/W).
#If you would like to create a new template, go to beanim/src/templates and create a new template.
#Modify such template at your will and add it allowed_modules in this script and to the print list.

def import_template(module_name):
    """This function, at the beginning of your main.py file, allows you to call one template among different ones. If this function is not called, beanim will provide a default B/W template.
 
    Returns::
    
        - The chosen template homogenised over all your objects.

    - **Example**::

        from manim import *
        from beanim import *

        import_template('fancy_mint')

    - The templates looks as follow:

    **B/W**

    .. image:: images/bw_1.png
        :width: 49%
    .. image:: images/bw_2.png
        :width: 49%

    **fancy_mint**

    .. image:: images/fm_1.png
        :width: 49%
    .. image:: images/fm_2.png
        :width: 49%

    **dark_depths**

    .. image:: images/dd_1.png
        :width: 49%
    .. image:: images/dd_2.png
        :width: 49%

    """

    allowed_modules= ["fancy_mint", "dark_depths"]
    if module_name in allowed_modules:
        try:
            module= importlib.import_module("beanim.templates." + module_name) #It seems one has to specify all the way down to the module
            print("-------------------------------------------------------------------------------")
            print(f"Successfully imported template -> {module_name}")
            return module
        except ImportError:
            return None
    if module_name not in allowed_modules:
        try:
            print("-------------------------------------------------------------------------------")
            print(f"Template with the given name does not exit. I will use the default template (B/W) instead.")
            module= importlib.import_module("beanim.templates.template_0") #It seems one has to specify all the way down to the module
        except ImportError:
            return None

