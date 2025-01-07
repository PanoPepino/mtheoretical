from manim import *
from .plot_general import *

class Plot_Quantum(Plot_General, VGroup):
    """This class returns the simplest quantum cosmology potential to discuss the two different boundary conditions of this framework.

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
    ---------

    - create_wave_functions: (It shows both wave functions to H-Hawk and Vilenkin wave functions)
    
    """
    def __init__(self,
                 **kwargs):
        
        super().__init__(**kwargs)
        
        #Axes and labels
        self.ax_q_cosmo= NumberPlane(
                x_range= [0.01, 7, 1],
                y_range= [0.01, 4, 1],
                tips= False,
                background_line_style= {"stroke_opacity": 0}).set_color(BLACK).set(stroke_opacity= self.axis_opacity)
        region_point= self.ax_q_cosmo.coords_to_point(4, 4)
        split_regions= self.ax_q_cosmo.get_vertical_line(region_point).set_color(self.text_color)
        self.lab_ax_q_cosmo= self.ax_q_cosmo.get_axis_labels(x_label= MathTex("a",color= self.text_color,font_size= 25), y_label= MathTex("V(a)",color= self.text_color,font_size= 25))
        regions= MathTex("I", "II", color= self.text_color, font_size=30)
        regions[0].next_to(split_regions,LEFT, buff= 1)
        regions[1].next_to(split_regions,RIGHT, buff= 1)

        #Potential
        pot_q_cosmo= self.ax_q_cosmo.plot(
                    lambda x: x**2 - x**4/(4)**2 ,
                    color= self.func_main_color,
                    x_range= [0,4.07],
                    stroke_width= self.stroke_w,
                    use_smoothing= True)
        
        q_pot= VGroup(self.ax_q_cosmo, pot_q_cosmo, split_regions, regions, self.lab_ax_q_cosmo)
    
        #Wave functions and labels
        self.HHawking= self.ax_q_cosmo.plot(
                    lambda x:1/3*((1 - np.tanh(4*(x - 5)))*(np.e**(1 - np.abs(1 - 0.06*x**(2))**(3/2)))+ 2/((x+1)**(1/2))*(1 + np.tanh(2*(x - 4)))*np.cos(5*(0.06*x**(2) - 1)**(2)) ) ,
                    x_range= [0.01,7],
                    stroke_width= self.stroke_w,
                    use_smoothing= True).set_color(self.func_3_color)
        
        self.Vilenkin= self.ax_q_cosmo.plot(
                    lambda x:1/3* ((1 - np.tanh(x - 4))*np.e**(-1 + np.abs(1 - 0.06*x**(2))**(3/2))+ (np.tanh(2*(x - 4)) + 1)/2*np.cos((5*(0.06*x**(2) -1)**2 + np.pi/4))/(x)**(1/2)/2 ) ,
                    x_range= [0.01,7],
                    stroke_width= self.stroke_w,
                    use_smoothing= True).set_color(self.func_2_color)
        
        self.HH_label= self.ax_q_cosmo.get_graph_label(self.HHawking, label= "H-H").set_color(self.func_3_color).scale(0.6).next_to(q_pot, RIGHT, aligned_edge= LEFT, buff= 2.5)
        self.Vilenkin_label= self.ax_q_cosmo.get_graph_label(self.Vilenkin, label= "Vilenkin").set_color(self.func_2_color).scale(0.6).next_to(self.HH_label, DOWN, aligned_edge= LEFT, buff= 0.1)

        if self.decorator_presence== "box":
            box= SurroundingRectangle(self.ax_q_cosmo, corner_radius= self.corner_rad, color= self.decorator_color, fill_opacity= self.fill_opa, buff= self.tightness+ 0.4, stroke_width= self.decorator_stroke_w)
            self.to_draw= VGroup(self.HHawking, self.HH_label, self.Vilenkin, self.Vilenkin_label) 
            self.to_show= VGroup(q_pot, box)
            self.add(self.to_show, self.to_draw)
            

        #Observe that 0-th element are the axis and labels of these. Then 1st element is the group of elements to plot.  
        else:
            self.to_draw= VGroup(self.HHawking, self.HH_label, self.Vilenkin, self.Vilenkin_label) 
            self.to_show= q_pot
            self.add(self.to_show, self.to_draw)
    
    def create_wave_functions(self,
                              rt: float= 2,
                              rf: float= linear)-> Succession:
        """Write both wavefunctions for the discussion and its legend.

        Args:
            rt (float, optional): Defaults to 2.
            rf (float, optional): Defaults to linear.

        Returns:
            Succession: 
        """
        
        return Succession(
            *[Write(piece) for piece in self.to_draw])

        
        


    

        