from ..my_imports import *
from os import path

__all__= ['Photo']

class Photo(Group):
    """Class to represent a Photography. Find and example in Post_It Class.
    
    - **Parameters**::

        - photo (str): path to the desired photo. It assumes your photo is located in a 
        folder called figures, at the same level of the main script where you call this class.
        - decorator_style (str, optional): Defaults to "techno".
            - polaroid: It resembles a polaroid photo, with a pin on top.
            - techno: It is just a frame of the decorator_color.
        - decorator_color (ParsableManimColor, optional): Defaults to RED.
        - decorator_stroke_w (float, optional): Thickness of the frame.
        Defaults to 5.
        - caption (str, optional): The text to add under the polaroid picture.
        Defaults to "".
        - text_size (float, optional): text_size of font for the text mentioned above. 
        Defaults to 30.
        - text_color (ParsableManimColor, optional): Defaults to BLACK.
        - pin_color (ParsableManimColor, optional): Color of the pin on top of the polaroid. 
        Defaults to RED.
       
    .. note::

        Captions are only allowed in decorator_style= "polaroid" 

    """
    
    def __init__(self,
                 photo, 
                 decorator_style: str= "techno", 
                 caption: str= "",
                 text_size: float= 30,
                 text_color: ParsableManimColor= BLACK,
                 decorator_color: ParsableManimColor= RED,
                 pin_color: ParsableManimColor= RED,
                 corner_rad: float= 0.2,
                 decorator_stroke_w: float= 5,
                 **kwargs):
       
        super().__init__(**kwargs)
             
            
        # This gets the svg path in the package, wherever the package is (I hope it still works when transformed into a pip package) and then add the desired svg. Observe that path.dirname gets the path where this file is located. I then go back to the parent directory, where the figure folder is.

        #get_image_path= path.join(path.dirname(__file__), '../figures/', photo)
        get_svg_path= path.join(path.dirname(__file__), '../figures/pin.svg')
        
        # Polaroid
        if decorator_style== "polaroid":
            r1= Rectangle(width= 2, height= 2.9)
            r2= Rectangle(width= 1.8, height= 2.1).move_to(r1.get_center()).shift(0.3*UP)
            polaroid= Cutout(r1, r2, fill_opacity= 1, color= WHITE, stroke_color= GRAY_A).scale(1.5)

            image= ImageMobject("figures/" + photo).set(z_index= -1).scale_to_fit_width(polaroid.get_width()).move_to(polaroid.get_center() + [0,0.5,0])
    
            pin= SVGMobject(get_svg_path).scale(0.2).next_to(polaroid,UP, buff=-0.1).shift(0.2*RIGHT)
            pin.set_color(pin_color)
        
        # Text under polaroid
            texto= Tex(caption, font_size= text_size, color= text_color).next_to(polaroid, DOWN, buff= -0.7).set(z_index= 4)
        
            self.chosen_photo= Group(polaroid, image, texto, pin)
            self.add(self.chosen_photo)
         
        # Technophoto   
        if decorator_style== "techno":
            image= ImageMobject("figures/" + photo).set(z_index= -1)
            frame= SurroundingRectangle(image, corner_radius= corner_rad, color= decorator_color, stroke_width= 2*decorator_stroke_w, buff= 0.03)
            self.chosen_photo= Group(frame.set_z_index(3), image)
            self.add(self.chosen_photo)
            