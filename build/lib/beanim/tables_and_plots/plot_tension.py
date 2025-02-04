from .plot_general import *
from ..my_imports import *

__all__=['Plot_Lambda_Tension']

class Plot_Lambda_Tension(Plot_General, VGroup):
    """This class represents the tension of the nucleated brane with respect to the different values of the AdS scales inside and outside. See Plot_General Class.

    .. note::

        The 0-th element correspond to the axis and labels.

    - **Example**::

        from manim import *
        from beanim import *

        class Example_Plot_Tension(Scene):
            def construct(self):
                p_tension= Plot_Lambda_Tension()
                p_tension.scale(0.3, about_point= p_tension.ax_tension_DB.get_origin()).to_corner(LEFT)
                self.play(FadeIn(p_tension[0]))
                self.play(p_tension.create_function())

    """

    def __init__(self,
                 **kwargs):
        super().__init__(**kwargs)
        
    
        #Axes and labels
        self.ax_tension_DB= NumberPlane(
                    x_range= [0, 25, 1],
                    y_range= [-27, 20, 1],
                    x_length= 14,
                    y_length= 7,
                    tips= False,
                    background_line_style= {"stroke_opacity": 0}).set_color       (self.text_color).set(stroke_opacity= self.stroke_opa)

        self.lab_ax_tension_DB= self.ax_tension_DB.get_axis_labels(x_label= MathTex("\\sigma",font_size= 40, color= self.text_color), y_label=MathTex("\\Lambda_{4}",font_size= 40, color= self.text_color))
        self.lab_ax_tension_DB[1].shift(0.2*DOWN)
        kp= 3
        km=4

        #Potential and labels
        self.pot_tension_DB= self.ax_tension_DB.plot(
            lambda x: (x**2)/12 - 3/2 *(kp**2 + km**2) + 27/4 *((km**2 - kp**2)/x)**2,
            color= self.func_main_color ,
            stroke_width= self.stroke_w,
            use_smoothing= True,
            x_range=[2.4, 3])

        self.pot_tension_DB_2= DashedVMobject(self.ax_tension_DB.plot(
            lambda x: (x**2)/12 - 3/2 *(kp**2 + km**2) + 27/4 *((km**2 - kp**2)/x)**2,
            color=  self.func_2_color,
            stroke_width= self.stroke_w,
            use_smoothing=True,
            x_range=[3, 21]))
        
        self.pot_tension_DB_3= self.ax_tension_DB.plot(
            lambda x: (x**2)/12 - 3/2 *(kp**2 + km**2) + 27/4 *((km**2 - kp**2)/x)**2,
            color= self.func_main_color,
            stroke_width= self.stroke_w,
            use_smoothing= True,
            x_range=[21, 25])

        self.dot_1= Dot(color= self.func_3_color, stroke_width= self.stroke_w, fill_opacity= self.fill_opa).move_to(self.ax_tension_DB.c2p(3, 0)).scale(3)
        self.dot_2= Dot(color=  self.func_3_color, stroke_width= self.stroke_w, fill_opacity= self.fill_opa).move_to(self.ax_tension_DB.c2p(21, 0)).scale(3)

        if self.decorator_presence== "box":
            box= SurroundingRectangle(self.ax_tension_DB, corner_radius= self.corner_rad, color= self.decorator_color, fill_opacity= self.fill_opa, buff= self.tightness, stroke_width= self.decorator_stroke_w)
            self.to_draw= VGroup(self.pot_tension_DB, self.pot_tension_DB_2, self.pot_tension_DB_3,self.dot_1, self.dot_2) 
            self.to_show= VGroup(box, self.ax_tension_DB, self.lab_ax_tension_DB)
            self.add(self.to_show, self.to_draw)

        #Observe that 0-th element are the axis and labels of these. Then 1st element is the group of elements to plot. 
        else:
            self.to_draw= VGroup(self.pot_tension_DB, self.pot_tension_DB_2, self.pot_tension_DB_3,self.dot_1, self.dot_2) 
            self.to_show= VGroup(self.ax_tension_DB, self.lab_ax_tension_DB)
            self.add(self.to_show, self.to_draw)
    
    
    def create_function(self,
                        rt: float= 1,
                        rf: float= linear)-> Succession:
        """
        Args::

            - rt (float, optional): Defaults to 1.
            - rf (float, optional): Defaults to linear.

        Returns::

            Succession: Write the function for the tension of the brane as a function of the AdS scale.
        """
        
        return Succession(
            *[Write(piece, run_time= rt, rate_func= rf) for piece in self.to_draw])