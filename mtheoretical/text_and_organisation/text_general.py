from manim import *

class Text_General(VGroup):
    """Class to load all inputs for the subsequent classes with Text (no equations, no tables. Just bullet points and refs). In this way the template becomes homogenous.

    - **Parameters**::
   
        - text_size (float, optional): Defaults to 25.
        - text_color (ParsableManimColor, optional): Defaults to BLACK.
        - decorator_presence (str, optional): This has several options (Defaults to box)
            - "box": A simple surrounding rectangle around the title.
            - "no": Nothing. Plain text. 
        - decorator_color (ParsableManimColor, optional): Defaults to BLACK.
        - decorator_stroke_width (float, optional): Defaults to 2.
        - corner_rad (float, optional): Corner radious of surrounding box. Defaults to 0.3.
        - corner_rad_direction (list, optional): which corners of the surrounding rectangle
        get rounded. Defaults to [1, 1, 1, 1].
        - fill_opa (float, optional): Fill opacity of the surrounding box. Defaults to 0.1.
        - tightness (float, optional): How tight the box around the title is. Defaults to 0.5.
        - stroke_opa (float, optional): Opacity of the strokes. Defaults to 1.
        - dot_scale (float, optional): Size of bullets. Defaults to 2.

    - An **Example** of how text and organisation elements look like is::

        from manim import *
        from mtheoretical import *

        class Generic_Slide(Scene):
            def construct(self):
                slide_title= Title_Section("This is a really long title to check capabilities")
                ref1= Ref("fake ref").to_corner(UR)
                important_points= BlB(["This is extremely important",
                                      "Use .next\\_point() to iterate over points",
                                      "... And for the last point you can recover all points in the initial color"]).to_corner(LEFT)
                self.play(slide_title.show_title())
                self.play(FadeIn(ref1, important_points))
                for point in range(len(important_points)):
                    self.play(important_points.next_point()+2)

              
    """ 
     
    def __init__(self,
                 text_size: float= 25,
                 text_color: ParsableManimColor= BLACK,
                 decorator_presence: str= "box",
                 decorator_color: ParsableManimColor= BLACK,
                 decorator_stroke_width: float= 2,
                 corner_rad: float= 0.3,
                 corner_rad_direction: list= [1,1,1,1],
                 fill_opa: float= 0.1,
                 tightness: float= 0.5,
                 stroke_opa: float= 1,
                 dot_scale: float= 2,
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
        self.dot_scale= dot_scale