import importlib

#The following lines allow you to choose between different templates for each of the objects of the presentation.
#If you choose no template from the list, manim will render the default configuration (B/N).
#If you would like to create a new template, go to mtheoretical/src/templates and create a new template.
#Modify such template at your will and add it allowed_modules in this script and to the print list.

def import_module_from_input():
    print("Before you run your presentation, choose among the following templates:\n"
          "-------------------------------------------------------------------------------\n"
          "- fancy_mint\n"
          "- dark_depths\n"
          "-------------------------------------------------------------------------------\n")
    module_name = input("If you choose none, the libraries will display the default (B/N) template. Please, enter the name of the template you would like to display: ")
    allowed_modules = ["fancy_mint", "dark_depths"]
    if module_name in allowed_modules:
        try:
            module = importlib.import_module("mtheoretical.src.templates." + module_name) #It seems one has to specify all the way down to the module
            print("-------------------------------------------------------------------------------")
            print(f"Successfully imported template -> {module_name}")
            return module
        except ImportError:
           
            return None
    if module_name not in allowed_modules:
        try:
            print("-------------------------------------------------------------------------------")
            print(f"Template with the given name does not exit. I will use the default template (B/N) instead.")
            module = importlib.import_module("mtheoretical.src.templates.template_0") #It seems one has to specify all the way down to the module
        except ImportError:
            return None


#Example usage
imported_module = import_module_from_input()

if imported_module:
    #You can now use functions or variables from the imported module
    if hasattr(imported_module, 'main'):
        imported_module.main()
    else:
        pass
    #print(f"The module does not have a 'main' function")