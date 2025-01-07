from manim import *
from .eq_general import *



class Eq_GC(Eq_General, VGroup):
    """Class to create equations related to Gauss-Codazzi tech. It has a dictionary built in.

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
        self.eq_gc_refs= {
            
            'gc initial': '\\mathcal{J}_{a b}= R_{\\alpha \\beta \\gamma \\delta}^{(5)} e_c^\\alpha e_a^\\beta e_d^\\gamma e_b^\\delta h^{c d}=R_{a b}^{(4)}+\\left(K_{a c} K_b^c-K_c^c K_{a b}\\right)',
            'gc reversed': 'G_{ab}^{(4)}=\left(\\frac{k_{+} k_{-}}{k_{-}-k_{+}}\\right)\\left[\\left(\\frac{\\mathcal{J}_{ab}^{+}}{k_{+}}-\\frac{\\mathcal{J}_{ab}^{-}}{k_{-}}\\right)-\\frac{1}{2} h_{ab}\\left(\\frac{\\mathcal{J}^{+}}{k_{+}}-\\frac{\\mathcal{J}^{-}}{k_{-}}\\right)-3\\left(k_{-}-k_{+}\\right) h_{ab}-2 \\kappa_{5} S_{ab}\\right]',    
            'einstein 4d': ' R_{a b}^{(4)} - \\tfrac{1}{2} R^{(4)} h_{ab} + \\Lambda_{4} h_{ab}= T_{ab}^{\\rm extrinsic} - T_{ab}^{\\rm brane}= T^{\\rm effective}_{ab}'
         }
        
        self.chosen_equation= MathTex(str(self.eq_gc_refs[the_equation]), font_size= self.text_size, color= self.text_color)
        
        
        if self.decorator_presence== "box":
            self.box= SurroundingRectangle(self.chosen_equation, corner_radius= self.corner_rad, buff= self.tightness,  stroke_width= self.decorator_stroke_width, color= self.decorator_color, fill_opacity= self.fill_opa)
            self.add(self.chosen_equation, self.box)
        else:
            self.add(self.chosen_equation)

        