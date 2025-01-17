from manim import *

class Table_General(VMobject):
    """ Class to load all necessary common inputs for any table in this library through inheritance propertiy.

    - **Parameters**::
        
        - text_color (ParsableManimColor, optional): Defaults to WHITE.
        - hlight_1_color (ParsableManimColor, optional): Highlight color 
        for some of the cells. Defaults to GREEN.
        - hlight_2_color (ParsableManimColor, optional): Defaults to RED.
        - hlight_3_color (ParsableManimColor, optional): Defaults to BLUE.
        - corner_rad (float, optional): Defaults to 0.
        - corner_rad_direction (list, optional). To modify which vertex bend and not.
        Defaults to [0, 0, 0, 0].
        - decorator_color (ParsableManimColor, optional): Defaults to WHITE.
        - decorator_stroke_w (float, optiona): Defaults to 1.
        - stroke_w (float, optional): Defaults to 1.
        - stroke_opa (float, optional): Defaults to 1,
        - fill_opa (float, optional): Defaults to 0.3.

    - **Example**::

        from manim import *
        from manim theoretical import *

        class Example_Table_Summary_Bubble_and_Scales(Scene):
            def construct(self):
                gp= VGroup(Table_Summary_Induce(), Table_Energy_Scales()).arrange(RIGHT)
                gp.scale_to_fit_width(config.frame_width-1)
                self.add(gp)
        
    """

    def __init__(self,
                 text_color: ParsableManimColor= WHITE,
                 hlight_1_color: ParsableManimColor= GREEN,
                 hlight_2_color: ParsableManimColor= RED,
                 hlight_3_color: ParsableManimColor= BLUE,
                 decorator_color: ParsableManimColor= WHITE,
                 decorator_stroke_w: float= 1,
                 corner_rad: float= 0,
                 corner_rad_direction: list= [0, 0, 0, 0],
                 stroke_w: float= 1,
                 stroke_opa: float= 1,
                 fill_opa: float= 0.3,                  
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