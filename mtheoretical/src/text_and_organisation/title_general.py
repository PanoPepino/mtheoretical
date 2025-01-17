from manim import *

class Title_General(VGroup):
    """Class to load all inputs for the subsequent classes of titles (main and sections).
    
    - **Parameters**::
   
        - text_size (float, optional): Defaults to 25.
        - text_color (ParsableManimColor, optional): Defaults to WHITE.
        - decorator_presence (str, optional): This has several options (Defaults to no)
            - "box": A simple surrounding rectangle around the title.
            - "box_long_left"/"box_long_right": A surrounding rectangle that stretches
              to the chosen corner.
            - "back_frame": A whole back frame behind the text, spanning from side to side.
            - "no": Nothing. Plain text. 
        - decorator_color (ParsableManimColor, optional): Defaults to WHITE.
        - decorator_stroke_width (float, optional): Defaults to 1.
        - corner_rad (float, optional): Corner radious of surrounding box. Defaults to 0.
        - corner_rad_direction (list, optional): which corners of the surrounding rectangle
        get rounded. Defaults to [0, 0, 0, 0].
        - fill_opa (float, optional): Fill opacity of the surrounding box. Defaults to 0.1.
        - tightness (float, optional): How tight the box around the title is. Defaults to 0.3.
        - stroke_opa (float, optional): Opacity of the strokes. Defaults to 1.
    
    """ 
     
    def __init__(self,
                 text_size: float= 25,
                 text_color: ParsableManimColor= WHITE,
                 decorator_presence: str= "no",
                 decorator_color: ParsableManimColor= WHITE,
                 decorator_stroke_width: float= 1,
                 corner_rad: float= 0,
                 corner_rad_direction: list= [0, 0, 0, 0],
                 fill_opa: float= 0.1,
                 tightness: float= 0.3,
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