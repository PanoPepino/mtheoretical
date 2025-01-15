from manim import *
from .eq_general import *


class Eq_Brane_Corrections(Eq_General, VGroup):
    """Class to create equations related to higher curvature corrections in DBI + WZ terms of branes. It has a dictionary built in.
  
    """
    
    def __init__(self,
                 the_equation,
                 **kwargs):
        
        super().__init__(**kwargs)
        
        # To split the dictionary, use {{}} on each element you want to separate.
        self.eq_brane_corrections_refs= {

            'action D3 corrections': 'S[g_{\\mu \\nu}, C_{4}]= \\text{DBI}^{(0)} + \\alpha \\prime {}^{2} \\text{DBI}^{(2)} + \\text{WZ}^{(0)} + \\alpha \\prime {}^{2} \\text{WZ}^{(2)}',
            'correction to D3': '\\sigma \sim T_{D3} \\left(1 - \\frac{1}{g_{s} N}\\right)',
            'new lambda': 'N= \\sqrt{\\frac{3 \\pi}{G_{4}^{2} g_{s} \\rho_{\\Lambda}}'
        }
        
        self.chosen_equation= MathTex(str(self.eq_brane_corrections_refs[the_equation]), font_size= self.text_size, color= self.text_color)
        
        
        if self.decorator_presence== "box":
            self.box= SurroundingRectangle(self.chosen_equation, corner_radius= self.corner_rad, buff= self.tightness,  stroke_width= self.decorator_stroke_width, color= self.decorator_color, fill_opacity= self.fill_opa)
            self.add(self.chosen_equation, self.box)
        else:
            self.add(self.chosen_equation)



        