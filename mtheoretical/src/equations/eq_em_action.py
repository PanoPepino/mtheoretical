from manim import *
from .eq_general import *


class Eq_EM(Eq_General, VGroup):
    """Class to create equations related to electromagnetic field in higher dimensions. It has a dictionary built in.
    
    """

    def __init__(self,
                 the_equation,
                 **kwargs):
        
        super().__init__(**kwargs)
        
        # To split the dictionary, use {{}} on each element you want to separate.
        self.eq_em_refs= {
            
            'action em' : 'S_{5}[H, \\mathcal{F}] \sim \int d^{5}x \\sqrt{g_{5}} \\: \\left(R - H^{2}\\right) - T_{D3} \int d^{5}x \\: \\delta \\left(r - a(\\eta)\\right) \\:\\sqrt{g_{4} + \\mathcal{F}}',
            'EOM': '\\partial_r H^{r\\mu \\nu}= \\frac{2 \\kappa_{5} \\:kr}{\\alpha\\prime \\: \\pi^{2} } \\:{\\mathcal{F}}^{\\mu \\nu} \\:\\delta \\left(r-a(\\eta)\\right)'
         }
        
        self.chosen_equation= MathTex(str(self.eq_em_refs[the_equation]), font_size= self.text_size, color= self.text_color)
        
        
        if self.decorator_presence== "box":
            self.box= SurroundingRectangle(self.chosen_equation, corner_radius= self.corner_rad, buff= self.tightness,  stroke_width= self.decorator_stroke_width, color= self.decorator_color, fill_opacity= self.fill_opa)
            self.add(self.chosen_equation, self.box)
        else:
            self.add(self.chosen_equation)



        