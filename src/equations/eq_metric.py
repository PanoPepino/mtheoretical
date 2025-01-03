from manim import *
from .eq_general import *

class Eq_Metric(Eq_General, VGroup):
    """Class to create equations related to metrics. It has a dictionary built in.

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
        self.eq_metric_refs= {
            'induced metric': 'ds^{2}= -N^{2} d \\tau^{2} + a^{2} d\\Omega_{3}^{2}', 
            'ads metric': 'ds^{2}= -\\left(1+ k_{\\pm}^{2} r^{2}\\right) dt^{2} + \\left(1+ k_{\\pm}^{2} r^{2}\\right)^{-1} dr^{2} + r^{2} d\Omega_{3}^{2}',
            'generic metric': 'ds^{2} = -f_{1}\\left(x^{\\mu}\\right) dt^{2} + f_{2}\\left(x^{\\mu}\\right)dr^{2}+ r^{2}d\\Omega^{2}_{D-2}',
            'ads sch metric': 'ds^{2}= -\\left(1+ k_{\\pm}^{2} r^{2} - \\tfrac{8 G_{5} M_{\\pm}}{3 \\pi r^{2}}\\right) dt^{2} + \\left(1+ k_{\\pm}^{2} r^{2} - \\tfrac{8 G_{5} M_{\\pm}}{3 \\pi r^{2}}\\right)^{-1} dr^{2} + r^{2} d\Omega_{3}^{2}',
            'ads sch strings metric': 'ds^{2}= -\\left(1+ k_{\\pm}^{2} r^{2} - \\tfrac{2 G_{5} \\alpha_{\pm}}{r}\\right) dt^{2} + \\left(1+ k_{\\pm}^{2} r^{2} - \\tfrac{2 G_{5} \\alpha_{\pm}}{r}\\right)^{-1} dr^{2} + r^{2} d\Omega_{3}^{2}',
            'ads sch gw': 'ds^{2}= -\\left(1+ k_{\\pm}^{2} r^{2}\\right) dt^{2} + \\left(1+ k_{\\pm}^{2} r^{2}\\right)^{-1} dr^{2} + r^{2} d\Omega_{3}^{2} + \\zeta^{2} f\\left(q_{i}\\right)\\left(dt^{2}+ dr^{2}\\right)',
            'bh 10d metric': 'ds_{10}^2= -h\\left(r\\right)^{-2} f\\left(r\\right) dt^2+h\\left(r\\right)\\left(f\\left(r\\right)^{-1} d r^2+r^2 d \\Omega_{3}^{2}\\right) + L^2 \\sum_{i=1}^{3}\\left\{d \\sigma_i^2+\\sigma_i^2\\left(d \\phi_i+L^{-1} A\\left(r\\right)\\right)^2\\right\}',
            'bh 10d rs metric': 'ds_{10}^2= -g\\left(z\\right)dt^2+g\\left(z\\right)^{-1}dz^2+z^2d \\Omega_3^2 + L^2 \\sum_{i=1}^3\\left\{d \\sigma_i^2+\\sigma_i^2\\left(d \\phi_i+L^{-1} A\\left(z\\right)\\right)^2\\right\}',
            'bh g piece metric': 'g\\left(z\\right)=1+k^2 z^2-\\frac{2 \\kappa_5 \\mu}{z^2}+\\frac{\\kappa_5^2 \\theta^2}{z^4}',  
            
         }
        
        self.chosen_equation= MathTex(str(self.eq_metric_refs[the_equation]), font_size= self.text_size, color= self.text_color)
        
        
        if self.decorator_presence== "box":
            self.box= SurroundingRectangle(self.chosen_equation, corner_radius= self.corner_rad, buff= self.tightness,  stroke_width= self.decorator_stroke_width, color= self.decorator_color, fill_opacity= self.fill_opa)
            self.add(self.chosen_equation, self.box)
        else:
            self.add(self.chosen_equation)