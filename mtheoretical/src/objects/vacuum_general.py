from manim import *

class Vacuum_General(VGroup):
    """General class to load all inputs related to color and shape of vacua.

    - **Parameters**::

        - vacuum_color (ParsableManimColor, optional): Defaults to RED.
        - vacuum_fill_opa (float, optional): Defaults to 0.2.
        - vacuum_stroke_w: (float, optional). Defaults to 0.2.
        - corner_rad (float, optional): Corner radious of surrounding box. Defaults to 0.3.
        - corner_rad_direction (list, optional): which corners of the surrounding rectangle
        get rounded. Defaults to [1, 1, 1, 1].

    """
    def __init__(self, 
                 vacuum_color: ParsableManimColor= RED,
                 vacuum_fill_opa: float= 0.2,
                 vacuum_stroke_w: float= 0.2,
                 vacuum_text_color: ParsableManimColor= WHITE,
                 corner_rad: float= 0.3,
                 corner_rad_direction: list= [0,0,1,1],
                 **kwargs):
        
        super().__init__(**kwargs)
        self.vacuum_color= vacuum_color
        self.vacuum_fill_opa= vacuum_fill_opa
        self.vacuum_stroke_w= vacuum_stroke_w
        self.corner_rad= list(corner_rad*np.array(corner_rad_direction))
        self.vacuum_text_color= vacuum_text_color
        self.cr= corner_rad # To give the scalar value when displaying strings in the bubble 
        