from manim import *
from .eq_general import *

class Eq_Junc(Eq_General, VGroup):
    """Class to create equations related to cosmology. It has a dictionary built in.

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