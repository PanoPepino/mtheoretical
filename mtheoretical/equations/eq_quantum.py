from manim import *
from .eq_general import *

class Eq_Quantum_Cosmo(Eq_General, VGroup):
    
    """Class to create equations related to quantum bubble disucssion. It has a dictionary built in.

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
        self.eq_quantum= {
            
            'wdw': '\\mathcal{H} \\psi(a)= \\frac{N}{a} \\left(-\\frac{1}{24 \\pi^{2}} \\frac{d^{2}}{da^{2}} + 6 \\pi^{2} \\left(a^{2} -\\frac{a^{4}}{a_{0}^{2}}\\right)\\right)\\psi(a)= 0', 
            'wave0': '\\Psi(a)=',
            'wave1': ' \\bigg\\{',
            'wave2': 'a \\:e^{S(a_{0},0)} + b\\: e^{-S(a_{0},0)}, \\quad a \\leq a_{0} ',
            'wave3': 'c \\:e^{i\\:S(a,a_{0})} + d\\: e^{-i\\: S(a,a_{0})}, \\quad a \\geq a_{0}',
            'prob hh': 'P_{HH} \\propto e^{+2 S_{0}}',
            'prob vil': 'P_{Vil} \\propto e^{-2 S_{0}}',
            'prob BT': 'P \\propto e^{-B}=e^{ \\frac{-8 \\pi^{2} a_{0}^{2}}{\\kappa_{4}}}',
            'prob WKB': 'P \\propto e^{-2 \\int p d\\tau}= e^{\\frac{-8 \\pi^{2} a_{0}^{2}}{\\kappa_{4}}}' 
         }
        
        if the_equation== 'wdw': 
            self.chosen_equation= MathTex(str(self.eq_quantum['wdw']), font_size= self.text_size, color= self.text_color)
        if the_equation== 'wave':
            p0= MathTex(str(self.eq_quantum['wave0']), font_size= self.text_size, color= self.text_color)
            p1= MathTex(str(self.eq_quantum['wave1']), font_size= 1.2*self.text_size, color= self.text_color).next_to(p0, RIGHT, buff= self.tightness)
            p2= MathTex(str(self.eq_quantum['wave2']), font_size= self.text_size, color= self.text_color).next_to(p1, RIGHT, buff= self.tightness).shift(0.4*UP)
            p3= MathTex(str(self.eq_quantum['wave3']), font_size= self.text_size, color= self.text_color).next_to(p2, DOWN, aligned_edge= LEFT, buff= self.tightness)
            self.chosen_equation= VGroup(p0, p1, p2, p3)
        if the_equation== 'prob boundaries':
            p0= MathTex(str(self.eq_quantum['prob hh']), font_size= self.text_size, color= self.text_color)
            p1= MathTex(str(self.eq_quantum['prob vil']), font_size= self.text_size, color= self.text_color).next_to(p0, DOWN, aligned_edge= LEFT, buff= self.tightness)
            self.chosen_equation= VGroup(p0, p1)
        if the_equation== 'prob comparison':
            p0= MathTex(str(self.eq_quantum['prob BT']), font_size= self.text_size, color= self.text_color)
            p1= MathTex(str(self.eq_quantum['prob WKB']), font_size= self.text_size, color= self.text_color).next_to(p0, DOWN, aligned_edge= LEFT)
            self.chosen_equation= VGroup(p0, p1)

        if self.decorator_presence== "box":
            self.box= SurroundingRectangle(self.chosen_equation, corner_radius= self.corner_rad, buff= self.tightness,  stroke_width= self.decorator_stroke_width, color= self.decorator_color, fill_opacity= self.fill_opa)
            self.add(self.chosen_equation, self.box)
        else:
            self.add(self.chosen_equation)