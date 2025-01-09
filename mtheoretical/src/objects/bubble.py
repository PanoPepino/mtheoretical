from manim import *
from os import path
from .vacuum_general import *
from .brane_general import *


class Bubble(Brane_General, Vacuum_General, Group): 
    """Class to represent Braneworld bubbles in string theory.

    Parameters (See Brane_General and Vacuum_General classes)
    -----------
    - bubble_type (str, optional): Choose the type of Bubble to represent. To choose between Empty, Instanton, Radiation, Matter, Strings, GW, EM, Energy_Discussion. Defaults to "Empty".
    - box_height (float, optional): Defaults to 6.
    - box_width (float, optional): Defaults to 8.
    - vacuum_color (ParsableManimColor, optional): _description_. Defaults to RED.
    - vacuum_fill_opa (float, optional): _description_. Defaults to 0.2.
    - vacuum_stroke_w: (float, optional). Defaults to 0.2.
    - vacuum_text_color (ParsableManimColor, optional): _description_. Defaults to WHITE.
    - brane_color (ParsableManimColor, optional): _description_. Defaults to RED.
    - brane_fill_opa (float, optional): _description_. Defaults to 0.2.
    - brane_radius (float, optional): Size of brane. Defaults to 1.
    - brane_text_color (ParsableManimColor, optional): _description_. Defaults to WHITE.
    - brane_stroke_w: (float, optional). Defaults to 0.2.
    - string_color (ParsableManimColor, optional): Defaults to BLUE.
    - string_stroke_w (float, optional): Defaults to 1.5.
    - field_gradient (float, optional): Represents how good the gradient of thesource bulk field is. Defaults to 50.
    - field_top_color (ParsableManimColor, optional): Color of field on top of the brane. Defaults to BLUE.
    - field_bulk_color (ParsableManimColor, optional): (To be constructed). Defaults to PINK.
    - stroke_w (float, optional): Stroke width of rectangle and bubble boundaries. Defaults to 1.
    - self.brane_fill_opa (float, optional): Defaults to 0.2.
    - self.brane_fill_opa (float, optional): Defaults to 0.4.
        
    Methods
    -----------
    - fade_in_bulk(): Fades in the bulk (Background rectangle).
    - create_bubble(): Create the bubble and any other feature associated with it. (i.e. strings attached or fields on top)
    - expand_bubble(): Expands the bubble and create the dynamics of each of features on it.
    - For the Energy_Discussion type there are extra methods:
        - create_fail():
        - more_energy():

    """
    
    def __init__(self,
                 bubble_type: str= "Empty",
                 box_height: float= 6,
                 box_width: float= 8,
                 string_color: ParsableManimColor= BLUE,
                 string_stroke_w: float= 1.5,
                 field_gradient: float= 50,
                 field_top_color: ParsableManimColor= BLUE,
                 field_bulk_color: ParsableManimColor= PINK,
                 **kwargs):
        
        super().__init__(**kwargs)

        #It seems I have to do this to define properties inside animation functions
        self.bubble_type= bubble_type
        
        #Geometry Bubbles
        self.background= RoundedRectangle(corner_radius= self.corner_rad, height= box_height,  width= box_width, stroke_width= self.vacuum_stroke_w, color= self.vacuum_color, fill_opacity= self.vacuum_fill_opa)
        self.brane= Circle(radius= self.brane_radius, color= self.brane_color, fill_opacity= 1.5*self.brane_fill_opa, stroke_width= self.brane_stroke_w)

        #Text
        self.in_text= MathTex("k_{-}", font_size= 35, color= self.vacuum_text_color).move_to(self.background.get_center()).set_z_index(4)
        self.out_text= MathTex("k_{+}",font_size= 35, color= self.vacuum_text_color).move_to(self.background.get_corner(UR) -[0.45,0.45,0]).set_z_index(4)

        self.in_insta_text= MathTex("V(\phi_{-})", font_size= 35, color= self.vacuum_text_color).move_to(self.background.get_center()).set_z_index(4)
        self.out_insta_text= MathTex("V(\phi_{+})", font_size= 35, color= self.vacuum_text_color).move_to(self.background.get_corner(UR) -[0.55,0.55,0]).set_z_index(4)
        self.radius_line= Line(start= self.brane.get_center(), end= 2.5*self.brane.point_at_angle(PI/4), color= self.vacuum_text_color, stroke_width= self.brane_stroke_w)
        self.radius_text= MathTex("r=a(\\tau)", font_size= 30, color= self.vacuum_text_color).rotate(PI/4).next_to(self.radius_line.get_center(), LEFT, buff= 0.05)
        self.radius_info= VGroup(self.radius_line, self.radius_text)

        #Matter
        get_mass_path= path.join(path.dirname(__file__), '../figures/weight.svg')
        self.mass= SVGMobject(get_mass_path).scale(0.5)

        #Strings
        self.strings= VGroup()
        box_positions= [RIGHT, UR, UP, UL, LEFT, DL, DOWN, DR]
        dots= VGroup(*[Dot(radius= 0, fill_opacity= 0, point= self.brane.point_at_angle(i*360/8*DEGREES)) for i in range (len(box_positions))])
        self.brane_w_anchor = VGroup(dots, self.brane)
    
        # This simple list is more elegant. Impressive that for the iteration to work, one needs to "rewrite" initial and final positions.
        for angle, position in zip(dots, box_positions):
            if np.linalg.norm(position) > 1: # To avoid strange position if corner radius is big.
                string= always_redraw(lambda angle= angle, position= position: Line(start= angle, end= self.background.get_corner(position)-self.cr/6*position, stroke_width= string_stroke_w, stroke_color= string_color))
                self.strings.add(string)
            else:
                string= always_redraw(lambda angle= angle, position= position: Line(start= angle, end= self.background.get_corner(position), stroke_width = string_stroke_w, stroke_color = string_color))
                self.strings.add(string)

        #Grav. Waves
        def func_waves(t):
            return ((self.brane_radius + 0.01 * np.sin(25 * t)) * np. cos(t), 
                    (self.brane_radius + 0.01 * np.sin(25 * t)) * np. sin(t), 
                    0)
    
        self.brane_waves= ParametricFunction(func_waves, t_range= (0, 2 * TAU), stroke_width= self.brane_stroke_w, fill_opacity= self.brane_fill_opa).set_color(self.brane_color)
        self.waves= ParametricFunction(func_waves, t_range= (0, 2 * TAU), stroke_width= self.brane_stroke_w/3, fill_opacity= 0).set_color(self.brane_color)

        #Extra Fields
        #Electromagnetism (Note 5% extra radius)
        def field(grad, mobject, rad= self.brane_radius + 0.6, inner_rad= 1.05* self.brane_radius, col= field_top_color):
            glow_group= VGroup()
            for idx in range(grad):
                new_circle= Annulus(inner_radius= inner_rad, outer_radius= inner_rad + idx/grad * (rad - inner_rad), stroke_opacity= 0,
                fill_color= col, fill_opacity=0.75/grad).move_to(mobject)
                glow_group.add(new_circle)
            return glow_group
        
        self.field_glow= field(field_gradient, self.brane)
        self.field_top= Circle(radius= 1.05* self.brane_radius, color= field_top_color, fill_opacity= 0, stroke_width= 4)

        #Energy Discussion
        self.vacuum_tracker = ValueTracker(0.8)
        self.bar_outside = RoundedRectangle(corner_radius= self.corner_rad, height= 0.6,  width= box_width ,stroke_width= self.vacuum_stroke_w+0.2 , color= self.brane_color, fill_opacity= 0)
        self.bar_outside.next_to(self.background, DOWN, buff= 0.2)
        self.energy_gain = always_redraw(lambda: RoundedRectangle(corner_radius= self.corner_rad, height= 0.5,  width= self.vacuum_tracker.get_value() ,stroke_width= 0.1, fill_opacity= self.brane_fill_opa).next_to(self.bar_outside.get_left(), aligned_edge= LEFT, buff= 0).set_color(self.bar_outside.get_color()))
        self.energy_cost_bubble= DashedVMobject(Circle(radius= self.brane_radius, color= self.brane_color, fill_opacity= 0, stroke_width= self.vacuum_stroke_w +0.9))
        
        #Note that position of the brane is always [2] in the bubble_group.
        if bubble_type== "Empty":
            self.bubble= VGroup(self.background, self.out_text, self.brane, self.in_text, self.radius_info)
            self.add(self.bubble)

        if bubble_type== "Instanton":
            self.bubble= VGroup(self.background, self.out_insta_text, self.brane, self.in_insta_text)
            self.add(self.bubble)

        if bubble_type== "Radiation":
            self.in_text.next_to(self.mass, DOWN, buff= 0.2)
            self.bubble= VGroup(self.background, self.out_text, self.brane, self.in_text, self.mass)
            self.add(self.bubble)

        if bubble_type== "GW":
            self.bubble= VGroup(self.background, self.out_text, self.brane_waves, self.in_text)
            self.add(self.bubble)

        if bubble_type== "Strings":
            self.out_text.shift(0.3*DOWN)
            self.bubble= VGroup(self.background, self.out_text, self.brane_w_anchor, self.strings, self.in_text)
            self.add(self.bubble)

        if bubble_type== "EM":
            self.bubble= VGroup(self.background, self.out_text, self.brane, self.in_text, self.field_top, self.field_glow)
            self.add(self.bubble)

        if bubble_type== "Energy_Discussion":
            self.fake_brane= self.brane.copy()
            self.bubble= VGroup(self.background, self.out_text, self.fake_brane, self.brane, self.energy_cost_bubble)
            self.add(self.bubble, self.bar_outside, self.in_text, self.energy_gain)

    # Methods
    def fade_in_bulk(self, 
            rt: float= 1,
            rf: float=  linear)-> Animation: # The arrow associates this method with a class animation.
        """
        Args:
            - rt (float, optional): run_time animation. Defaults to 1.
            - rf (float, optioanl): rate function. Defaults to linear.

        Returns:
            - Animation: Returns the creation of the bulk box and the value of the cosmological constant outside.
        """
        if self.bubble_type== "Energy_Discussion":
            return Succession(
                FadeIn(self.bubble[:2], run_time= rt, rate_func= rf),
                FadeIn(self.bubble[-1], run_time= rt, rate_func= rf),
                Create(VGroup(self.bar_outside, self.energy_gain), run_time= rt, rate_func= rf))
        
        else:
            return FadeIn(self.bubble[:2], run_time= rt, rate_func= rf)
        
    def fail_creation(self,
            rt: float= 3,
            rf: float= there_and_back_with_pause)-> AnimationGroup:
        """Fails to create bubble for discussion of energy.

        Args:
            rt (float, optional): _description_. Defaults to 2.
            rf (float, optional): _description_. Defaults to linear.

        Returns:
            - Animation: The creation of the bubble fails due to lack of energy.
        """
        return AnimationGroup(
            self.vacuum_tracker.animate(run_time= rt, rate_func= rf).set_value(2),
            GrowFromCenter(self.bubble[2].scale(0.8), run_time= rt, rate_func= rf))
    
    def create_bubble(self, 
            rt: float= 0.2,
            rf: float= linear)-> Succession: #The arrow associates this method with a class succession.
        """
        Args:
            - rt (float, optional): run_time animation. Defaults to 1.
            - rf (float, optioanl): rate function. Defaults to linear.

        Returns:
            - Animation: Returns the creation of the bubble and its inside value of the scale curvature.
        """
        if self.bubble_type== "Energy_Discussion":
            return Succession(
                self.vacuum_tracker.animate(run_time= 5*rt, rate_func= rf).set_value(2.5),
                GrowFromCenter(self.bubble[3], run_time= 5*rt, rate_func= rf),
                self.energy_cost_bubble.animate.set_opacity(0))
        
        if self.bubble_type== "EM":
            return Succession(
                GrowFromCenter(self.bubble[2], run_time= rt, rate_func= rf),
                FadeIn(self.bubble[3:-2], run_time= rt, rate_function= rt),
                Create(self.field_top, run_time= rt, rate_function= rf),
                Wait(),
                Create(self.field_glow, run_time= 2*rt, rate_func= rf))
        
        if self.bubble_type== "Strings":
            return Succession(
                GrowFromCenter(self.bubble[2], run_time= rt, rate_func= rf),
                Create(self.strings, run_time= rt, rate_func= rf),
                FadeIn(self.bubble[-1], run_time= rt, rate_function= rt))
        
        if self.bubble_type== "Radiation":
            return Succession(
                GrowFromCenter(self.bubble[2], run_time= rt, rate_func= rf),
                FadeIn(self.bubble[3:], run_time= rt, rate_function= rt))

        else:
            return Succession(
                GrowFromCenter(self.bubble[2], run_time= rt, rate_func= rf),
                FadeIn(self.bubble[3:-1], run_time= rt, rate_function= rt))

    
    def expand_bubble(self, 
            rt: float= 6,
            rf: float= linear,
            sca: float= 2.5)-> AnimationGroup: #The arrow associates this method with a class animation.
        """
        Args:
            - rt (float, optional): run_time animation. Defaults to 6.
            - rf (float, optional): rate function. Defaults to linear.
            - sca (float, optional): size for the scaling of the brane.

        Returns:
            - Animation: Returns the expansion of the bubble. Depeding on the type of bubble, it will also add other features.
        """

        if self.bubble_type== "Energy_Discussion":
            return Succession(
                self.vacuum_tracker.animate(run_time= rt/3, rate_func= rf).set_value(4.5),
                self.bubble[3].animate(run_time= rt, rate_func= rf).scale(sca))
        
        if self.bubble_type== "GW":
            return AnimationGroup(self.brane_waves.animate(run_time= rt, rate_func= rf).scale(sca), Broadcast(self.waves.scale(0.6*sca), focal_point= self.bubble[2].get_center(), initial_opacity= 2,  final_opacity= 0, n_mobs= 10, run_time= rt, rate_func= rf))
        
        if self.bubble_type== "EM":
            return AnimationGroup(self.brane.animate(run_time= rt, rate_func= rf).scale(0.8*sca),self.bubble[-2:].animate(run_time= rt, rate_func= rf).scale(0.8*sca))
        
        if self.bubble_type== "Strings":
            return AnimationGroup(self.brane_w_anchor.animate(run_time= rt, rate_func= rf).scale(sca))

        else:
            return AnimationGroup(self.brane.animate(run_time= rt, rate_func= rf).scale(sca))
        
    def show_radius(self, 
            rt: float= 1,
            rf: float= linear)-> Succession:
        return Succession(
            self.in_text.animate.next_to(self.brane.get_center(), DOWN, buff= 0.2),
            Create(self.radius_info, run_time= rt, rate_function= rf))
        
        

        