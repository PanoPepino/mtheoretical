from manim import *
from pathlib import Path

class Eq_General(VGroup):
    """Class to create a mock-up general description of equations to be inherited by specific types of equations. 

    - **Parameters**::

        - the_dictionary: The path to the file () you would like the Class to read.
        - the_equation: The key (label in the .tex file) associated to the equation you would like to print.
        - text_size (float, optional): Defaults to 20.
        - text_color (ParsableManimColor, optional): Defaults to WHITE.
        - decorator_presence (str, optional). box/no. Defaults to no. If no, does not return the surrounding box.
        - decorator_color (ParsableManimColor, optional): Defaults to WHITE.
        - decorator_stroke_width (float, optional): Defaults to 1.
        - corner_rad (float, optional): Corner radious of surrounding box. Defaults to 0.
        - corner_rad_direction (list, optional): Which corners get rounded. Defaults to [0, 0, 0, 0].
        - fill_opa (float, optional): Fill opacity of the surrounding box. Defaults to 0.1.
        - tightness (float, optional): How tight the box around the title is. Defaults to 0.3.

    .. attention::

        This class requires to think of special methods if the loaded dictionary is eq_quantum. There are several equations there that go in a group.
    """
    def __init__(self,
                 the_dictionary,
                 the_equation,
                 text_size: float= 40, 
                 text_color: ParsableManimColor= WHITE,
                 decorator_presence: str= "no",
                 decorator_color: ParsableManimColor= WHITE,
                 decorator_stroke_width: float= 1,
                 corner_rad: float= 0,
                 corner_rad_direction: list= [0, 0, 0, 0],
                 fill_opa: float= 0.1,
                 tightness: float= 0.3,
                 **kwargs):
        
        super().__init__(**kwargs)

        def split_dictionary_path(input_string):
            """This method splits a given string only in the last "/" symbol.

            Args:
                - input_string (str)

            Returns:
                list: ["everything up to the last "/" symbol, "the remaining"]

            - An **Example**::

                split_dictionary_path(the_dictionary) -> ["the path", "the dictionary file"]
            """

            return input_string.rsplit('/', 1)
        
        my_path= split_dictionary_path(the_dictionary)[0] # Uses previous function to split the relative path
        my_file= split_dictionary_path(the_dictionary)[-1]
        

        def check_file_exists(directory, filename):
            """This methods checks if a given file exists in a given directory.

            Args:
                - directory
                - filename

            Returns:
                True or False
            """

            file_path = Path(directory) / filename
            return file_path.is_file()

        if check_file_exists(my_path, my_file): # Checks if the dictionary input exist
            open_the_dic= open(the_dictionary)
            read_the_dic= open_the_dic.read()
            load_the_dic= eval(read_the_dic)
            open_the_dic.close()
        
        else: # If not, it recommends to run first the code to extract dictionaries.
            print("The are two possible options for this error: \n"
                "---------------------------------------------------\n"
                  "- The path you have specified is wrong. Double check.\n"
                  "- The dictionary you refer to does not exist yet.\n"
                  "---------------------------------------------------\n"
                  "Consider running the function BLA BLA to extract the equations in a dictionary."
                  )

        # To split the dictionary, use {{}} on each element you want to separate.

        if the_equation in load_the_dic:
            self.chosen_equation= MathTex(str(load_the_dic[the_equation]), font_size= text_size, color= text_color)

        else:
            print("The equation you are looking for is not in this dictionary.")
                 
        if decorator_presence== "box":
            self.box= SurroundingRectangle(self.chosen_equation, corner_radius= list(corner_rad*np.array(corner_rad_direction)), buff= tightness,  stroke_width= decorator_stroke_width, color= decorator_color, fill_opacity= fill_opa)
            self.add(self.chosen_equation, self.box)
        else:
            self.add(self.chosen_equation)