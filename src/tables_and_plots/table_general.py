from manim import *

class Table_General(VMobject):
    """ Class to load all necessary common inputs for any table in this library.

    Parameters:
    -----------
        
    - text_color (ParsableManimColor, optional): Defaults to BLACK.
    - hlight_1_color (ParsableManimColor, optional): _description_. Defaults to RED.
    - hlight_2_color (ParsableManimColor, optional): _description_. Defaults to BLUE.
    - hlight_3_color (ParsableManimColor, optional): _description_. Defaults to PURPLE.
    - corner_rad (float, optional): _description_. Defaults to 0.3.
    - corner_rad_direction (list, optional). To modify which vertex bend and not.Defaults to [1, 1, 1, 1].
    - decorator_color (ParsableManimColor, optional): _description_. Defaults to BLACK.
    - decorator_stroke_w (float, optiona): Defaults to 1.
    - stroke_w (float, optional): _description_. Defaults to 7.
    - stroke_opa (float, optional): Defaults to 1,
    - fill_opa (float, optional): _description_. Defaults to 0.05.
        
    """

    def __init__(self,
                 text_color: ParsableManimColor= BLACK,
                 hlight_1_color: ParsableManimColor= RED,
                 hlight_2_color: ParsableManimColor= BLUE,
                 hlight_3_color: ParsableManimColor= PURPLE,
                 decorator_color: ParsableManimColor= BLACK,
                 decorator_stroke_w: float= 1,
                 corner_rad: float= 0.2,
                 corner_rad_direction: list= [1, 1, 1, 1],
                 stroke_w: float= 7,
                 stroke_opa: float= 1,
                 fill_opa: float= 0.05,                  
                 **kwargs):
    
        super().__init__(**kwargs)
        self.text_color= text_color
        self.hlight_1_color= hlight_1_color
        self.hlight_2_color= hlight_2_color
        self.hlight_3_color= hlight_3_color
        self.corner_rad= list(corner_rad*np.array(corner_rad_direction))
        self.decorator_color= decorator_color
        self.decorator_stroke_w= decorator_stroke_w
        self.stroke_w= stroke_w
        self.stroke_opa= stroke_opa
        self.fill_opa= fill_opa