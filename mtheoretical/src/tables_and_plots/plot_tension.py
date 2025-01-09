from manim import *
from .plot_general import *

class Plot_Lambda_Tension(Plot_General, VGroup):
    """This class represents the tension of the nucleated brane with respect to the different values of the AdS scales inside and outside.

    Parameters (See Plot_General Class)
    ----------
   
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
                    background_line_style= {"stroke_opacity": 0}).set_color       (BLACK).set(stroke_opacity= self.stroke_opa)

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
                              rt: float= 4,
                              rf: float= linear)-> Succession:
        """Write the function for the tension of the brane as a function of the AdS scale.

        Args:
            rt (float, optional): Defaults to 2.
            rf (float, optional): Defaults to linear.

        Returns:
            Succession: 
        """
        
        return Succession(
            *[Write(piece) for piece in self.to_draw])