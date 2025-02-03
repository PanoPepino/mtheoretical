from ..my_imports import *
from pathlib import Path

__all__= ['Eq_General']

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

    .. note::

        In case you want to first extract all the equations of a given .tex file in the form of a dictionary, please, check the "tools" package.
        
    .. attention::

        This class requires to think of special methods if the loaded dictionary is load_the_dic. There are several equations there that go in a group.
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

            Args::

                - input_string (str)

            Returns::
            
                list: ["everything up to the last "/" symbol, "the remaining"]

            - An **Example**::

                split_dictionary_path(the_dictionary) -> ["the path", "the dictionary file"]
            """

            return input_string.rsplit('/', 1)
        
        my_path= split_dictionary_path(the_dictionary)[0] # Uses previous function to split the relative path
        my_file= split_dictionary_path(the_dictionary)[-1]
        

        def check_file_exists(directory, filename):
            """This methods checks if a given file exists in a given directory.

            Args::

                - directory
                - filename

            Returns::
            
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
                  "Consider running the code \"extract equation from tex\" in the tools subpackage\n"
                  "to extract the equations in a dictionary."
                  )

        # To split the dictionary, use {{}} on each element you want to separate.
        print(my_file)
        if the_equation in load_the_dic:
            self.chosen_equation= MathTex(str(load_the_dic[the_equation]), font_size= text_size, color= text_color)

        # Personal modifications for a specific set of equations that require to appear together in my slides #

        elif my_file== "eq_quantum.txt":
            if the_equation== 'wave':
                p0= MathTex(str(load_the_dic['wave0']), font_size= text_size, color= text_color)
                p1= MathTex(str(load_the_dic['wave1']), font_size= 1.2*text_size, color= text_color).next_to(p0, RIGHT, buff= tightness)
                p2= MathTex(str(load_the_dic['wave2']), font_size= text_size, color= text_color).next_to(p1, RIGHT, buff= tightness).shift(0.4*UP)
                p3= MathTex(str(load_the_dic['wave3']), font_size= text_size, color= text_color).next_to(p2, DOWN, aligned_edge= LEFT, buff= tightness)
                self.chosen_equation= VGroup(p0, p1, p2, p3)
            if the_equation== 'prob boundaries':
                p0= MathTex(str(load_the_dic['prob hh']), font_size= text_size, color= text_color)
                p1= MathTex(str(load_the_dic['prob vil']), font_size= text_size, color= text_color).next_to(p0, DOWN, aligned_edge= LEFT, buff= tightness)
                self.chosen_equation= VGroup(p0, p1)
            if the_equation== 'prob comparison':
                p0= MathTex(str(load_the_dic['prob BT']), font_size= text_size, color= text_color)
                p1= MathTex(str(load_the_dic['prob WKB']), font_size= text_size, color= text_color).next_to(p0, DOWN, aligned_edge= LEFT)
                self.chosen_equation= VGroup(p0, p1)
        
        ###########################

        else:
            print("The equation you are looking for is not in this dictionary.")
                 
        if decorator_presence== "box":
            self.box= SurroundingRectangle(self.chosen_equation, corner_radius= list(corner_rad*np.array(corner_rad_direction)), buff= tightness,  stroke_width= decorator_stroke_width, color= decorator_color, fill_opacity= fill_opa)
            self.add(self.chosen_equation, self.box)
        else:
            self.add(self.chosen_equation)

        # Personal modifications for a specific set of equations that require to appear together in my slides #

        
        