from manim import *
from .eq_general import *


class Eq_EM(Eq_General, VGroup):
    r"""Class to create equations related to electromagnetic field in higher dimensions. It has a dictionary built in.

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



        