from textwrap import fill
from manim import *
from .plot_general import Plot_General

class Plot_Instanton(Plot_General, Group):
    """This is a class to represent an instanton potential with a false and true minima. 
    
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
    
    Methods
    -------
    
    - fade_in_field_position (rt= 0.5, rf= linear)
    - decay (rt= 0.5, rf= linear)
     
    """
    
    # Scale any graph with respect to the center scale(3, about_point=graph.ax_ins.c2p(0, 0, 0)
    
    def __init__(self,
                 **kwargs):
        
        super().__init__(**kwargs)
        
        self.ax_ins= NumberPlane(
            x_range=[-2.1, 2.1, 1],
            y_range=[-1, 1.5, 1],
            tips= False,
            background_line_style= {"stroke_opacity": 0}).set_color(BLACK).set(stroke_opacity= self.axis_opacity)
        lab_ax_ins= self.ax_ins.get_axis_labels(x_label= MathTex("\phi",font_size= 20, color= self.func_main_color), y_label= MathTex("V(\phi)",font_size= 25, color= self.func_main_color))
        lab_ax_ins[1].shift(0.2*DOWN)
        lab_ax_ins[0].shift(0.2*LEFT)
        self.ax_ins.y_axis.set_opacity(self.axis_opacity).set(stroke_width= self.axis_stroke)
        self.ax_ins.x_axis.set_opacity(self.axis_opacity).set(stroke_width= self.axis_stroke)
        
        #Potential and labels
        pot_ins= self.ax_ins.plot(
            lambda x: (-2 *x**2 + (x - 0.1)**4 + 0.64) ,
            color= self.func_main_color,
            stroke_width= self.axis_stroke,
            use_smoothing= True,
            x_range=[-1.3, 1.6])
        t_label= self.ax_ins.get_T_label(x_val= -0.845649, graph= pot_ins, label= MathTex("V_{+}", font_size= 20, color= self.func_main_color), triangle_size= 0)
        t_label.shift(0.6*UP+0.05*RIGHT)
        t_label_2= self.ax_ins.get_T_label(x_val= 1.15, graph= pot_ins, label= MathTex("V_{-}", font_size= 20, color= self.func_main_color), triangle_size= 0)
        t_label_2[0].shift(0.20*DOWN)
        t_label_2[-1].shift(30*UP)
        
        
        minima_labels=VGroup(t_label, t_label_2)

        self.field_position= Dot(color= self.decorator_color, stroke_width= self.stroke_w, fill_opacity= 1)
        self.tracker_ins= ValueTracker(-0.845649)
        self.field_position.add_updater(lambda y: y.move_to(self.ax_ins.c2p(self.tracker_ins.get_value(),0)))
        
        
        if self.decorator_presence== "box":
            box= SurroundingRectangle(self.ax_ins, corner_radius= self.corner_rad, color= self.decorator_color, fill_opacity= self.fill_opa, buff= self.tightness, stroke_width= self.decorator_stroke_w)
            self.initial_show= VGroup(self.ax_ins, lab_ax_ins, pot_ins, minima_labels, box)
            self.add(self.initial_show, self.field_position)
        else:
            self.initial_show= VGroup(self.ax_ins, lab_ax_ins, pot_ins, minima_labels)
            self.add(self.initial_show, self.field_position)
            
    
    def fade_in_field_position(self,
                        rt: float= 0.5,
                        rf: float= linear)-> Animation:
        """

        Args:
            rt (float, optional): Defaults to 0.5.
            rf (float, optional): Defaults to linear.

        Returns:
            Animation: Fades the field position in.
        """
        return FadeIn(self.field_position, run_time= rt, rate_func= rf)
    
    def decay(self,
              rt: float= 0.5,
              rf: float= linear)-> Animation:
        """_summary_

        Args:
            rt (float, optional): Defaults to 0.5.
            rf (float, optional): Defaults to linear.

        Returns:
            Animation: Describes the decay process in the potential.
        """
        
        return self.tracker_ins.animate(run_time= rt, rate_func= rf).set_value(0.7)
    
    