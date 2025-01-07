from manim import *

class Eq_General(VGroup):
    """Class to create a mock-up general description of equations to be inherited by specific types of equations. 

    Parameters:
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
                 text_size: float= 40, 
                 text_color: ParsableManimColor= BLACK,
                 decorator_presence: str= "box",
                 decorator_color: ParsableManimColor= BLACK,
                 decorator_stroke_width: float= 2,
                 corner_rad: float= 0.3,
                 corner_rad_direction: list= [1,1,1,1],
                 fill_opa: float= 0.1,
                 tightness: float= 0.2,
                 **kwargs):
        
        super().__init__(**kwargs)
        self.text_size= text_size
        self.text_color= text_color
        self.corner_rad_direction= corner_rad_direction
        self.corner_rad= list(corner_rad*np.array(corner_rad_direction))
        self.decorator_presence= decorator_presence
        self.decorator_color= decorator_color
        self.fill_opa= fill_opa
        self.tightness= tightness
        self.decorator_stroke_width= decorator_stroke_width