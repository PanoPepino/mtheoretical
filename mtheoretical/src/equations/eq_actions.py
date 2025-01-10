from manim import *
from .eq_general import *

class Eq_Action(Eq_General, VGroup):
    """Class to create equations related to Actions. The following equations are listed in the inbuilt dictionary:

    - bubble action 5d: 
    .. math::
        
        \\mathcal{S}= \\frac{1}{2 \\kappa_{5}} \\int d^{5} x \\sqrt{|g|}\\left(R^{(5)}-2 \\Lambda_{5}\\right) - \\sigma \\int d^{4} \\zeta \\sqrt{|\\eta|} + \\frac{1}{\\kappa_{5}} \\oint d^{4} x \\sqrt{|h|} K

    - hamil quantum 5d: 
    .. math::

        \\mathcal{H} \\psi_{5D}= \\left(\\left(-\\frac{1}{24 \\pi^{2}}\\frac{1}{a^{3 / 2}} \\frac{d^{2}}{d a^{2}}\\right)+6 \\pi^{2} V(a)\\right) {{a^{3 / 2} \\psi_{5D}}}= 0

    - dbi action: 
    .. math::
    
        S_{D 3}= -T_3 \\int d^4 \\xi \\sqrt{- det P[G]} + T_3 \\int P\\left[C_4\\right]

    - hamil from dbi:
    .. math::
    
        \\mathcal{H}= 2 \\pi^2 T_3\\left(\\sqrt{-g_{tt}\\left(\\mathcal{Z}^6+\\frac{J_C^2}{L^2}\\right)} \\sqrt{1+g_{zz} \\dot{\\mathcal{Z}}^2}-\\left(C_4\\right)_{t}-\\frac{A_t}{L} J_c \\right)

    """
    def __init__(self,
                 the_equation,
                 **kwargs):
        
        super().__init__(**kwargs)
        

        # To split the dictionary, use {{}} on each element you want to separate.
        self.eq_action_refs= {
            'bubble action 5d': '\\mathcal{S}= \\frac{1}{2 \\kappa_{5}} \\int d^{5} x \\sqrt{|g|}\\left(R^{(5)}-2 \\Lambda_{5}\\right) - \\sigma \\int d^{4} \\zeta \\sqrt{|\\eta|} + \\frac{1}{\\kappa_{5}} \\oint d^{4} x \\sqrt{|h|} K',
            'hamil quantum 5d': '\\mathcal{H} \\psi_{5D}= \\left(\\left(-\\frac{1}{24 \\pi^{2}}\\frac{1}{a^{3 / 2}} \\frac{d^{2}}{d a^{2}}\\right)+6 \\pi^{2} V(a)\\right) {{a^{3 / 2} \\psi_{5D}}}= 0',
            'dbi action': 'S_{D 3}= -T_3 \\int d^4 \\xi \\sqrt{- det P[G]} + T_3 \\int P\\left[C_4\\right]',
            'hamil from dbi': '\\mathcal{H}= 2 \\pi^2 T_3\\left(\\sqrt{-g_{tt}\\left(\\mathcal{Z}^6+\\frac{J_C^2}{L^2}\\right)} \\sqrt{1+g_{zz} \\dot{\\mathcal{Z}}^2}-\\left(C_4\\right)_{t}-\\frac{A_t}{L} J_c \\right)'
         }
        
        self.chosen_equation= MathTex(self.eq_action_refs[the_equation], font_size= self.text_size, color= self.text_color)
        
        
        if self.decorator_presence== "box":
            self.box= SurroundingRectangle(self.chosen_equation, corner_radius= self.corner_rad, buff= self.tightness,  stroke_width= self.decorator_stroke_width, color= self.decorator_color, fill_opacity= self.fill_opa)
            self.add(self.chosen_equation, self.box)
        else:
            self.add(self.chosen_equation)