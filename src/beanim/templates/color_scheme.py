import importlib

__all__= ['import_template']

#The following lines allow you to choose between different templates for each of the objects of the presentation.
#If you choose no template from the list, manim will render the default configuration (B/N).
#If you would like to create a new template, go to mtheoretical/src/templates and create a new template.
#Modify such template at your will and add it allowed_modules in this script and to the print list.

def import_template(module_name):
    """This function will be called everytime you run manim. It allows you to choose between, so far, two different templates, plus a default one in B/W.

    Returns:
        - The chosen template homogenised over all your objects.
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
            print(f"Template with the given name does not exit. I will use the default template (B/N) instead.")
            module= importlib.import_module("beanim.templates.template_0") #It seems one has to specify all the way down to the module
        except ImportError:
            return None

