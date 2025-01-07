from manim import *

class Vacuum_General(VGroup):
    """This is a mock-up class to load all inputs for vacua and associated objects.

    Parameters:
    -----------
    - vacuum_color (ParsableManimColor, optional): _description_. Defaults to RED.
    - vacuum_fill_opa (float, optional): _description_. Defaults to 0.2.
    - vacuum_stroke_w: (float, optional). Defaults to 0.2.
    - vacuum_text_color (ParsableManimColor, optional): _description_. Defaults to WHITE.

    """
    def __init__(self, 
                 vacuum_color: ParsableManimColor= RED,
                 vacuum_fill_opa: float= 0.2,
                 vacuum_stroke_w: float= 0.2,
                 direction_corner_rad: list= [0,0,1,1],
                 corner_rad: float= 0.3,
                 vacuum_text_color: ParsableManimColor= WHITE,
                 **kwargs):
        
        super().__init__(**kwargs)
        self.vacuum_color= vacuum_color
        self.vacuum_fill_opa= vacuum_fill_opa
        self.vacuum_stroke_w= vacuum_stroke_w
        self.corner_rad= list(corner_rad*np.array(direction_corner_rad))
        self.vacuum_text_color= vacuum_text_color
        self.cr= corner_rad # To give the scalar value when displaying strings in the bubble 
        