from manim import *
from .title_general import *

class Title_Section(Title_General, VGroup):
    """Class to create title for sections. 

    Parameters: (See Organisation_General Class)
    ----------

    - title ("str")
    - text_size (float, optional): Defaults to 25.
    - text_color (ParsableManimColor, optional): Defaults to BLACK.
    - decorator_presence (str, optional): box/box_long_XX/back_frame/no. Defaults to box. Box_long_XX returns a long box stretching to the chosen corner. Back_frame means a long rectangle without borders and corners outside the screen (stroke= 0). If no, does not return the surrounding box.
    - decorator_color (ParsableManimColor, optional): Defaults to BLACK.
    - decorator_stroke_width (float, optional): Defaults to 2.
    - corner_rad (float, optional): Corner radious of surrounding box. Defaults to 0.3.
    - corner_rad_direction (list, optional): which corners get rounded. Defaults to [1, 1, 1, 1].
    - fill_opa (float, optional): Fill opacity of the surrounding box. Defaults to 0.1.
    - tightness (float, optional): How tight the box around the title is. Defaults to 0.5.
    - stroke_opa (float, optional): Defaults to 1.
    - dot_scale (float, optional): Defaults to 2.

    Note that the title is already defined in the UL corner.

    Methods:
    --------

    - show_title: Specially designed for the long_box, it fades in the title from the chosen direction.


    """ 
    
    def __init__(self,
                 title_sec, 
                 **kwargs)-> VGroup:
        
        super().__init__(**kwargs)
        #text
        self.tit= Tex(title_sec, font_size= 1.4*self.text_size, color= self.text_color)
        
        if self.decorator_presence== "box":
            self.box= SurroundingRectangle(self.tit, color= self.decorator_color, corner_radius= self.corner_rad, buff= self.tightness, fill_opacity= self.fill_opa, stroke_width= self.decorator_stroke_width, stroke_opacity= self.stroke_opa)
            self.t_sec= VGroup(self.tit, self.box).to_corner(UL)
            self.add(self.t_sec)
        
        if self.decorator_presence== "box_long_left":
            self.box_long= RoundedRectangle(height= self.tit.get_height()+self.tightness, width= config.frame_width+0.1, stroke_width= self.decorator_stroke_width, color= self.decorator_color, fill_opacity= self.fill_opa, corner_radius= self.corner_rad, stroke_opacity= self.stroke_opa)
            self.tit.next_to(self.box_long.get_left(), RIGHT, aligned_edge= LEFT, buff= 0.2)
            self.tit.to_corner(UL)
            self.box_long.next_to(self.tit.get_left(), RIGHT, aligned_edge= LEFT, buff= -self.tightness)
            
            self.t_sec= VGroup(self.tit, self.box_long)
            self.add(self.t_sec)

        if self.decorator_presence== "box_long_right":
            self.box_long= RoundedRectangle(height= self.tit.get_height()+self.tightness, width=  self.tit.get_width()+5, stroke_width= self.decorator_stroke_width, color= self.decorator_color, fill_opacity= self.fill_opa, corner_radius= self.corner_rad, stroke_opacity= self.stroke_opa)
            self.box_long.flip()
            self.tit.to_corner(UL)
            self.box_long.next_to(self.tit.get_right(), LEFT, aligned_edge= RIGHT, buff= -self.tightness)
            
            self.t_sec= VGroup(self.tit, self.box_long)
            self.add(self.t_sec)

        elif self.decorator_presence== "back_frame":
            self.rectangle= Rectangle(height= self.tit.get_height()+self.tightness, width=  config.frame_width+2, stroke_width= self.decorator_stroke_width, color= self.decorator_color, fill_opacity= self.fill_opa, stroke_opacity= self.stroke_opa)
            self.tit.to_corner(UL)
            self.rectangle.to_corner(UP).shift(self.tightness/2).set(z_index= -2)
            self.t_sec= VGroup(self.tit, self.rectangle)
            self.add(self.t_sec)

        else:
            self.add(self.tit)

    
    def show_title(self)-> AnimationGroup:
        
        if self.decorator_presence== "box_long_right":
            return FadeIn(self.t_sec, shift= 5*RIGHT)
        
        if self.decorator_presence== "box_long_left":
            return FadeIn(self.t_sec, shift= 5*LEFT)
        
        else:
            return Create(self.t_sec)

    
