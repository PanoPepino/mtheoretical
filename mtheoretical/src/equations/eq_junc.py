from manim import *
from .eq_general import *

class Eq_Junc(Eq_General, VGroup):
    """Class to create equations related to cosmology. It has a dictionary built in.
    
    """

    def __init__(self,
                 the_equation,
                 **kwargs):
        
        super().__init__(**kwargs)
        # To split the dictionary, use {{}} on each element you want to separate.
        self.eq_junc_refs= {
            
            'junc generic 1': 'h_{ab}^{(+)}= h_{ab}^{(-)}', 
            'junc generic 2': 'S_{ab}= \\kappa_{5}^{-1}\\left([\\Delta K_{ab}]^{+}_{-} -[\\Delta K]^{+}_{-}h_{ab}\\right)',
            'junc db':  'S_{ab}= \\kappa_{5}^{-1}\\left([K_{ab}^{(+)} - K_{ab}^{(-)}]-[K^{(+)} - K^{(-)}]h_{ab}\\right)',
            'crit tension rs': '\\sigma= \\frac{3 \\left(k + k \\right)}{\\kappa_{5}}',
            'crit tension db': '\\sigma_{cr}= \\frac{3}{\\kappa_{5}}\\left(k_{-}-k_{+}\\right)',
            'brane tension db': '\\sigma= \\frac{3}{\\kappa_{5}} \\left(\\sqrt{k_{-}^{2} + \\frac{1+ \\dot{a}^{2}}{a^{2}}} -\\sqrt{k_{+}^{2} + \\frac{1+ \\dot{a}^{2}}{a^{2}}} \\right)',
            'junc bh rs': 'T_3=\\frac{3}{\\kappa_5}\\left(\\sqrt{\\frac{g_{-}(a)+\\dot{a}^2}{a^2}}-\\sqrt{\\frac{g_{+}(a)+\\dot{a}^2}{a^2}}\\right)'
         }
   
        self.chosen_equation= MathTex(str(self.eq_junc_refs[the_equation]), font_size= self.text_size, color= self.text_color)
        
        
        if self.decorator_presence== "box":
            self.box= SurroundingRectangle(self.chosen_equation, corner_radius= self.corner_rad, buff= self.tightness,  stroke_width= self.decorator_stroke_width, color= self.decorator_color, fill_opacity= self.fill_opa)
            self.add(self.chosen_equation, self.box)
        else:
            self.add(self.chosen_equation)