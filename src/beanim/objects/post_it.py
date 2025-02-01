from ..my_imports import *
from os import path


__all__= ['Post_It']

class Post_It(Group):
    """This is a class represents a Post-it sticker with a list of To-Do and a pin on top.

    - **Parameters**::

        - to_dos (list): The bullet points to add to the post it.
        - text_color (ParsableManimColor, optional): Defaults to BLACK.
        - text_size (float, optional): Defaults to 30.
        - pin_color (ParsableManimColor, optional): Defaults to RED.
    
    - **Example**::

        from manim  import *
        from beanim import *

        class Example_Photo_Post_it(Scene):
        def construct(self):
            photo_1= Photo("pedro.png", decorator_style= "polaroid", caption= "Perro Xanxe")
            photo_2= Photo("pedro.png", decorator_style= "techno", caption= "Perro Xanxe")
            p_it= Post_It(to_dos= ["Random example", "Just Do It!"]).scale(0.9)
            all_them= Group(photo_1, photo_2, p_it).arrange(RIGHT, buff= 0.2)
            all_them.scale_to_fit_width(config.frame_width-1)
            self.add(all_them)
    """
    
    def __init__(self, 
                 to_dos: list, 
                 text_color: ParsableManimColor= BLACK,
                 text_size: float= 30,
                 pin_color: ParsableManimColor= RED, 
                 **kwargs):
        super().__init__(**kwargs)
        
        #postit
        get_post_it_path= path.join(path.dirname(__file__), '../figures/post_it.svg')
        post= SVGMobject(get_post_it_path).set(z_index= -1).scale(2)
        
        get_pin_path= path.join(path.dirname(__file__), '../figures/pin.svg') # This gets the svg path in the package, wherever the package is (I hope it still works when transformed into a pip package) and then add the desired svg. Observe that path.dirname gets the path where this file is located. I then go back to the parent directory, where the figure folder is.
        pin= SVGMobject(get_pin_path).scale(0.2).next_to(post,UP, buff=-0.1).shift(0.2*RIGHT).set(color= pin_color)
        
        #text
        td= BulletedList(*to_dos, color= text_color, font_size= text_size, buff= 0.3, dot_scale_factor=2)
        td.set(color= text_color)
        td.next_to(post.get_left(), RIGHT, aligned_edge= LEFT, buff=0.2).shift(0.5*UP)
        
        #texto
        
        self.post_it= Group(post, td, pin)
        
        self.add(self.post_it)