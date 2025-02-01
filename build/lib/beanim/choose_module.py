from .templates import *

ch= input()
imported_module = import_template(ch)
#
if imported_module:
#You can now use functions or variables from the imported module
    if hasattr(imported_module, 'main'):
        imported_module.main()
    else:
        pass
print(f"The module does not have a 'main' function")