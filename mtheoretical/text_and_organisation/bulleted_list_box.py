from manim import *
from .text_general import *

class BlB(Text_General, Group):
    """Class to create a bulleted list surrounded by a box if chosen.

    Parameters: (See Text_general Class)
    -----------
    
    - list_input (list of strings): Each of the points to describe.
    - text_size (float, optional): Defaults to 25.
    - text_color (ParsableManimColor, optional): Defaults to BLACK.
    - decorator_presence (str, optional): box/no. Defaults to box. If no, does not return the surrounding box.
    - decorator_color (ParsableManimColor, optional): Defaults to BLACK.
    - decorator_stroke_width (float, optional): Defaults to 2.
    - corner_rad (float, optional): Corner radious of surrounding box. Defaults to 0.3.
    - corner_rad_direction (list, optional): which corners get rounded. Defaults to [1, 1, 1, 1].
    - fill_opa (float, optional): Fill opacity of the surrounding box. Defaults to 0.1.
    - tightness (float, optional): How tight the box around the title is. Defaults to 0.5.
    - stroke_opa (float, optional): Defaults to 1.
    - dot_scale (float, optional): Defaults to 2.

    Methods:
    --------

    - next_point: It animates the bullet point in an iterative way. It keeps black the n-th point and greys out the rest. 

    """
    
    def __init__(self,
                 list_input, 
                 **kwargs)-> VGroup:
        
        super().__init__(**kwargs)
        
        #Geometry
        self.order_list= BulletedList(*list_input, font_size= 1.2*self.text_size, buff= self.tightness, stroke_color= self.text_color, dot_scale_factor= self.dot_scale)
        self.order_list.set_color(self.text_color)
        self.count= 0
        
        if self.decorator_presence== "box":
            self.box= SurroundingRectangle(self.order_list, corner_radius= self.corner_rad, buff= self.tightness, stroke_width= self.decorator_stroke_width, color= self.decorator_color, fill_opacity= self.fill_opa, stroke_opacity= self.stroke_opa)
            self.add(self.order_list, self.box)

        else: 
            self.add(self.order_list)

    def next_point(self,
                    rf: float= linear,
                    rt: float= 1)-> Succession:
        
            
        if self.count== 0:
            self.count+= 1
           
            return Succession(self.order_list[1:].animate(run_time= rt, rate_func= rf).set_opacity(0.2))
        
        if 0< self.count< len(self.order_list):
            self.count+= 1
            return Succession(
                self.order_list.animate(run_time= rt, rate_func= rf).set_opacity(0.2),
                self.order_list[self.count-1].animate(run_time= rt, rate_func= rf).set_opacity(1))
        if self.count== len(self.order_list):
            self.count+= 1
            return Succession(
                self.order_list.animate(run_time= rt, rate_func= rf).set_opacity(1))
        
        else:
            return Wait()
        
    

        
        

