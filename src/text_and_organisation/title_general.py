from manim import *

class Title_General(VGroup):
    """Class to load all inputs for the subsequent classes of titles (main and sections). In this way the template because homogenous.
    
    Parameters: 
    ----------

    - text_size (float, optional): Defaults to 25.
    - text_color (ParsableManimColor, optional): Defaults to BLACK.
    - decorator_presence (str, optional): box/box_long_left/box_long_right/back_frame/no. Defaults to box surrounding the text. Box_long_XX means a box that stretches to the chosen side of the screen. Back_frame means a long rectangle without borders and corners outside the screen. If no, does not return the surrounding box.
    - decorator_color (ParsableManimColor, optional): Defaults to BLACK.
    - decorator_stroke_width (float, optional): Defaults to 2.
    - corner_rad (float, optional): Corner radious of surrounding box. Defaults to 0.3.
    - corner_rad_direction (list, optional): which corners get rounded. Defaults to [1, 1, 1, 1].
    - fill_opa (float, optional): Fill opacity of the surrounding box. Defaults to 0.1.
    - tightness (float, optional): How tight the box around the title is. Defaults to 0.5.
    - stroke_opa (float, optional): Defaults to 1.
    
    """ 
     
    def __init__(self,
                 text_size: float= 25,
                 text_color: ParsableManimColor= BLACK,
                 decorator_presence: str= "box",
                 decorator_color: ParsableManimColor= BLACK,
                 decorator_stroke_width: float= 2,
                 corner_rad: float= 0.3,
                 corner_rad_direction: list= [1, 1, 1, 1],
                 fill_opa: float= 0.1,
                 tightness: float= 0.5,
                 stroke_opa: float= 1,
                 **kwargs)-> VGroup:
        
        super().__init__(**kwargs)
        self.text_size= text_size
        self.text_color= text_color
        self.decorator_presence= decorator_presence
        self.decorator_color= decorator_color
        self.fill_opa= fill_opa
        self.tightness= tightness
        self.decorator_stroke_width= decorator_stroke_width
        self.stroke_opa= stroke_opa
        self.corner_rad= list(corner_rad*np.array(corner_rad_direction))