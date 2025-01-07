from manim import *

class Plot_General(Group):
    """This class is a mock class to control the apareance of all other plots through the inheritance property.


    - **Parameters**::
   
            - func_main_color (ParsableManimColor, optional): Defaults to GREEN.
            - func_2_color (ParsableManimColor, optional): Defaults to RED.
            - func_3_color (ParsableManimColor, optional): Defaults to BLUE.
            - text_color (ParsableManimColor, optional): Defaults to BLACK.
            - axis_opacity (float, optional): Defaults to 1.
            - axis_stroke (float, optional): Defaults to 2.
            - decorator_presence (str, optional): Defaults to "box".
            - decorator_color (ParsableManimColor, optional): Defaults to BLACK.
            - decorator_stroke_w: (float, optional). Defaults to 1.
            - corner_rad (float, optional): Defaults to 0.3.
            - corner_rad_direction (list, optional): Defaults to [1,1,1,1].
            - fill_opa (float, optional): Defaults to 0.1.
            - stroke_w (float, optional): Defaults to 1.
            - stroke_opa (float, optional): Defaults to 0.1.
            - tightness (float, optional): Defaults to 0.2.

    - **Example**::

            from manim import *
            from mtheoretical import *

            class SquareExample(Scene):
                def construct(self):
                    square_1 = Square(side_length=2.0).shift(DOWN)
                    square_2 = Square(side_length=1.0).next_to(square_1,direction=UP)
                    square_3 = Square(side_length=0.5).next_to(square_2, direction=UP)
                    self.add(square_1, square_2, square_3)

    """ 
    def __init__(self,
                 func_main_color: ParsableManimColor= GREEN,
                 func_2_color: ParsableManimColor= RED,
                 func_3_color: ParsableManimColor= BLUE,
                 text_color: ParsableManimColor= BLACK,
                 axis_opacity: float= 0.5,
                 axis_stroke: float= 2,
                 decorator_presence: str= "box",
                 decorator_color: ParsableManimColor= BLACK,
                 decorator_stroke_w: float= 0.5,
                 corner_rad: float= 0.3,
                 corner_rad_direction: list= [1, 1, 1, 1],
                 fill_opa: float= 0.1,
                 stroke_w: float= 1,
                 stroke_opa: float= 0.1,
                 tightness: float= 0.2,
                 **kwargs):
        
        super().__init__(**kwargs)
        self.func_main_color= func_main_color
        self.func_2_color= func_2_color
        self.func_3_color= func_3_color
        self.text_color= text_color
        self.axis_opacity= axis_opacity
        self.axis_stroke= axis_stroke
        self.decorator_presence= decorator_presence
        self.decorator_color= decorator_color
        self.decorator_stroke_w= decorator_stroke_w
        self.corner_rad= list(corner_rad*np.array(corner_rad_direction))
        self.fill_opa= fill_opa
        self.stroke_w= stroke_w
        self.stroke_opa= stroke_opa
        self.tightness= tightness