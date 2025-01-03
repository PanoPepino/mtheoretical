from manim import *
from .eq_general import *

class Eq_Scales_DB(Eq_General, VGroup):
    """Class to create equations related to hierarchy of scales in the Dark Bubble model. It has a dictionary built in.

    Parameters (See Eq_General Class):
    -----------
    - text_size (float, optional): Defaults to 20.
    - text_color (ParsableManimColor, optional): Defaults to BLACK.
    - decorator_presence (str, optional). yes/no. Defaults to yes. If no, does not return the surrounding box.
    - decorator_color (ParsableManimColor, optional): Defaults to BLACK.
    - decorator_stroke_width (float, optional): Defaults to 2.
    - corner_rad (float, optional): Corner radious of surrounding box. Defaults to 0.3.
    - corner_rad_direction (list, optional): Which corners get rounded. Defaults to [1, 1, 1, 1].
    - fill_opa (float, optional): Fill opacity of the surrounding box. Defaults to 0.1.
    - tightness (float, optional): How tight the box around the title is. Defaults to 0.2.
    
    """

    def __init__(self, 
                 the_equation,
                 **kwargs):
        
        super().__init__(**kwargs)
        
        # To split the dictionary, use {{}} on each element you want to separate.
        self.eq_scales_db_refs= {

            'hierarchy expected': 'L > \\ell_{10} > \\ell_{5} > \\ell_{4}',
            'hierarchy dark bubble': 'L > \\ell_{10} > \\ell_{4} > \\ell_{5}',
            'hierarchy with N': 'N^{1/2}\\ell_{4} > N^{1/4}\\ell_{4} > \\ell_{4} > N^{-1/6} \\ell_{4}', 
            'hierarchy numeric size': '10^{-5} m > 10^{-20} m > 10^{-35} m > 10^{-45} m', 
            'hierarchy energy value': '3.8 \\, meV < 13.7 \\, TeV < 1.22 \\times 10^{19} \\, GeV  < 5.1 \\times 10^{28}  \\, GeV',
            'tension correction': '\\sigma \sim T_{D_{3}}\\left(1- \\frac{1}{g_{s} N}\\right)'
        }
        
        self.chosen_equation= MathTex(str(self.eq_scales_db_refs[the_equation]), font_size= self.text_size, color= self.text_color)
        
        
        if self.decorator_presence== "box":
            self.box= SurroundingRectangle(self.chosen_equation, corner_radius= self.corner_rad, buff= self.tightness,  stroke_width= self.decorator_stroke_width, color= self.decorator_color, fill_opacity= self.fill_opa)
            self.add(self.chosen_equation, self.box)
        else:
            self.add(self.chosen_equation)



        