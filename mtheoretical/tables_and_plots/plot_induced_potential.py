from manim import *
from .plot_general import *
from scipy.optimize import fsolve

class Plot_Induced_Potential(Plot_General, Group):
    """This is a class to represent a 4D cosmo potential for the nucleated brane from the 10D.

    Parameters (see Plot_General Class)
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
    - show_jc: Modifies the barrier of the angular momentum.
    - restore_jc: Return the angular momentum to initial example value.
    - nucleate_brane: Moves the point to the nucleation point.
    - accelerate: Moves the point along the acceleration phase.
    - bounce: Moves the point back.
    - add_cc_and_expand: Adds a little bit of cosmological constant and expand.
    
    """
    
    #Scale any graph with respect to the center scale(3, about_point=graph.ax_ins.c2p(0, 0, 0)
    
    def __init__(self,
                 **kwargs):
        
        super().__init__(**kwargs)
        
        #Tracker and values
        aH= 1.2
        ah= 1
        
        
        #Axes and labels
        self.ax_4D_cosmos= NumberPlane(
            x_range= [1.2, 6, 1],
            y_range= [-1.6, 1.2, 1],
            x_length= 12,
            y_length= 6,
            tips= False,
            background_line_style= {"stroke_opacity":0}).set_color(BLACK)
        self.lab_ax_4D_cosmos= self.ax_4D_cosmos.get_axis_labels(x_label= MathTex("a",font_size= 40, color= self.func_main_color), y_label= MathTex("V(a)",font_size= 40, color= self.func_main_color))
        self.lab_ax_4D_cosmos[1].shift(0.5*DOWN)
        self.ax_4D_cosmos.y_axis.set_opacity(self.axis_opacity).set(stroke_width= self.axis_stroke)
        self.ax_4D_cosmos.x_axis.set_opacity(self.axis_opacity).set(stroke_width= self.axis_stroke)
        
        #Potential and labels
        self.pot_4D_cosmos_og= self.ax_4D_cosmos.plot(
            lambda x: 1.5*((1/x**4)*(1.2**2 - x**2)*(1 - x**2)*(1.2**2 + 1 + 1 +x**2) - (1/(5**2 + x**6))*(x**4 - 1.2**4 + (5/1.2)*((1+ 1.2**2 + 1)**(1/2))*(1- 1.2**2/x**2))**2 - (0/40)*x**2),
            color= self.func_main_color,
            stroke_width= self.decorator_stroke_w,
            use_smoothing= True,
            x_range=[1.2, 6])
        
        self.pot_4D_cosmos_jc_change= DashedVMobject(self.ax_4D_cosmos.plot(
            lambda x: 1.5*((1/x**4)*(1.2**2 - x**2)*(1 - x**2)*(1.2**2 + 1 + 1 +x**2) - (1/(10**2 + x**6))*(x**4 - 1.2**4 + (10/1.2)*((1+ 1.2**2 + 1)**(1/2))*(1- 1.2**2/x**2))**2 - (0/40)*x**2),
            color= self.func_2_color,
            stroke_width= self.decorator_stroke_w,
            use_smoothing= True,
            x_range=[1.2, 6]))
        
        self.pot_4D_cosmos_with_cc= self.ax_4D_cosmos.plot(
            lambda x: 1.5*((1/x**4)*(1.2**2 - x**2)*(1 - x**2)*(1.2**2 + 1 + 1 +x**2) - (1/(5**2 + x**6))*(x**4 - 1.2**4 + (5/1.2)*((1+ 1.2**2 + 1)**(1/2))*(1- 1.2**2/x**2))**2 - (0.9/40)*x**2),
            color= self.func_3_color,
            stroke_width= self.decorator_stroke_w,
            use_smoothing= True,
            x_range=[1.2, 6])
        
        self.position= Dot(color= self.decorator_color, stroke_width= self.stroke_w)
        self.pos_track= ValueTracker(1.2)
        self.position.add_updater(lambda y: y.move_to(self.ax_4D_cosmos.c2p(self.pos_track.get_value(),0)))


        if self.decorator_presence== "box":
            box= SurroundingRectangle(self.ax_4D_cosmos, corner_radius= self.corner_rad, color= self.decorator_color, fill_opacity= self.fill_opa, buff= self.tightness + 0.2, stroke_width= self.decorator_stroke_w)
            self.initial_show= VGroup(self.ax_4D_cosmos,self.lab_ax_4D_cosmos, box)
            self.add(self.initial_show, self.lab_ax_4D_cosmos, self.pot_4D_cosmos_og, self.pot_4D_cosmos_jc_change, self.pot_4D_cosmos_with_cc, self.position)
        
        else:
            self.add(self.ax_4D_cosmos, self.lab_ax_4D_cosmos, self.pot_4D_cosmos_og, self.pot_4D_cosmos_jc_change, self.pot_4D_cosmos_with_cc)
            
    def show_potential(self,
                  rt: float= 2,
                  rf: float= linear)-> Animation:
        """

        Args:
            rt (float, optional): Defaults to 2.
            rf (float, optional): Defaults to linear.

        Returns:
            Animation: Shows the original potential.
        """
        
        return Write(self.pot_4D_cosmos_og, run_time= rt, rate_func= rf) 
     
    def show_jc(self,
                  rt: float= 2,
                  rf: float= linear)-> Animation:
        """

        Args:
            rt (float, optional): Defaults to 2.
            rf (float, optional): Defaults to linear.

        Returns:
            Animation: Shows the potential with extra barrier of the angular momentum.
        """
        
        return Write(self.pot_4D_cosmos_jc_change, run_time= rt, rate_func= rf)
    
    
    
    def nucleate_brane(self,
                  rt: float= 0.5,
                  rf: float= linear)-> Succession:
        """

        Args:
            rt (float, optional): Defaults to 0.5.
            rf (float, optional): Defaults to linear.

        Returns:
            Animation: Moves the position in the potential to the outer horizon.
        """
        
        return Succession(FadeIn(self.position),
                          self.pos_track.animate(run_time= rt, rate_func= rf).set_value(1.7))
    
    def accelerate(self,
                  rt: float= 0.5,
                  rf: float= linear)-> Animation:
        """

        Args:
            rt (float, optional): Defaults to 0.5.
            rf (float, optional): Defaults to linear.

        Returns:
            Animation: Takes the brane to the minimum of the potential.
        """
        return self.pos_track.animate(run_time= rt, rate_func= rf).set_value(2.4)
    
    def bounce(self,
               rt: float= 4,
               rf: float= linear)-> Succession:
        """

        Args:
            rt (float, optional): Defaults to 4.
            rf (float, optional): Defaults to linear.

        Returns:
            Succession: Makes the system bounce in the potential.
        """
        
        return Succession(
            self.pos_track.animate(run_time= rt/2, rate_func= rf).set_value(3.9).build(),
            self.pos_track.animate(run_time= rt/2, rate_func= rf).set_value(1.72))
        
    def add_cc_and_expand(self,
                          rt: float= 6,
                          rf: float= linear)-> Succession:
        """

        Args:
            rt (float, optional): Defaults to 6.
            rf (float, optional): Defaults to linear.

        Returns:
            Succession: Shows the modified potential to add the presence of the cosmological constant and then expand the bubble forever.
        """
        
        return Succession(
            Write(self.pot_4D_cosmos_with_cc, run_time= rt/3, rate_func= rf),
            Wait(),
            self.pos_track.animate(run_time= 2*rt/3, rate_func= rf).set_value(6))
               
    
    

        
    
    