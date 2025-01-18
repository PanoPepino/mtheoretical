from manim import *

class Eq_General(VGroup):
    """Class to create a mock-up general description of equations to be inherited by specific types of equations. 

    - **Parameters**::

        - the_dictionary: The path to the .txt file you would like the Class to read.
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

        THIS REQUIRES SOME LINES SUCH THAT, IF THE CHOSEN SET OF EQUATIONS IS NOT PART OF AN INNER LIBRARY, IT LOOKS FOR THOSES FILES IN THE RELATIVE PATH WRT THE MANIM RENDERER FILE.

        It also requires to transfer all dictionaries to new .txt files for this class to read them.

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

        open_the_dic= open(the_dictionary+ ".txt")
        read_the_dic= open_the_dic.read()
        load_the_dic= eval(read_the_dic)
        open_the_dic.close()

        # To split the dictionary, use {{}} on each element you want to separate.

        self.chosen_equation= MathTex(str(load_the_dic[the_equation]), font_size= text_size, color= text_color)
           
        if decorator_presence== "box":
            self.box= SurroundingRectangle(self.chosen_equation, corner_radius= list(corner_rad*np.array(corner_rad_direction)), buff= tightness,  stroke_width= decorator_stroke_width, color= decorator_color, fill_opacity= fill_opa)
            self.add(self.chosen_equation, self.box)
        else:
            self.add(self.chosen_equation)