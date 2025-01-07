from manim import *
from os import path

class Post_It(Group):
    """This is a class that creates a Group that represents a Post it sticker with text. 

    Parameters:
    -----------
    - to_dos (list): The bullet points to add to the post it.
    - text_color (ParsableManimColor, optional): _description_. Defaults to BLACK.
    - text_size (float, optional): _description_. Defaults to 30.
    - pin_color (ParsableManimColor, optional): _description_. Defaults to RED.
    
    Returns:
    -------
    
    - A post it with the bulleted list written on top and a pin on top.
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