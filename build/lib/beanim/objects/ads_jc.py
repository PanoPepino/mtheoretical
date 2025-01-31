from .brane_general import *
from .vacuum_general import *
from ..my_imports import *

__all__= ['AdS_Jc']

class AdS_Jc(Vacuum_General, Brane_General, VGroup):
    """Class to represent the vacua discussion for RS and DB models. It includes an arrow to discuss the normal orientation changes ([-1] Entry). It has several animations in the form of methods. See Classes Vacuum and Brane General for further parameters. 

    - **Parameters**::
    
        - vacua_type (str, optional): To choose among Randall-Sundrum (RS) or DarkBubble (DB). Defaults to "DB".
        - arrow_color (ParsableManimColor, optional): Defaults to WHITE.
    
    - An **Example** of how this class works::

        from ..my_imports import *
        from mtheoretical import *

        class Example_AdS_Jc(Scene):
            def construct(self):
                show_db= AdS_Jc(vacua_type= "DB")
                show_rs= AdS_Jc(vacua_type= "RS")
                show= VGroup(show_db, show_rs).arrange(RIGHT, aligned_edge= DOWN, buff= 0.2)
                show.scale_to_fit_width(config.frame_width-2)

                self.play(AnimationGroup(map(lambda x: x.fade_in(), show)))
                self.play(AnimationGroup(map(lambda x: x.fade_in_arrow(), show)))
                self.play(show[1].show_symmetry(rt= 5))
                self.play(show[1].restore_symmetry())
                self.play(AnimationGroup(show[0].show_n_vector_db(rt= 5),
                                         show[1].show_n_vector_rs(rt= 5)))
                self.play(show.animate.shift(2*UP))
                self.play(FadeOut(show))
        
    - **Methods**::

    """
        
    def __init__(self,
                 vacua_type: str= "DB",
                 arrow_color: ParsableManimColor= WHITE,
                 **kwargs):
        
        super().__init__(**kwargs)
       
        #Geometry (RS)
        self.brane= Line(start= [0,-2,0], end= [0,2.2,0], color= self.brane_color, stroke_width= self.brane_stroke_w+1)
        self.adskpRS= RoundedRectangle(corner_radius= self.corner_rad, height= 4,  width= 4, stroke_width= self.vacuum_stroke_w, color= self.vacuum_color, fill_opacity= self.vacuum_fill_opa)
        self.adskmRS= self.adskpRS.copy().flip()
        self.adskpRS.next_to(self.brane, RIGHT, buff= 0.1, aligned_edge= DOWN)
        self.adskmRS.next_to(self.brane, LEFT, buff= 0.1, aligned_edge= DOWN)
        
        #Text (RS)
        self.in_text_RS= MathTex("\\Lambda_{5D}= -6 k_{-}^{2}", color= self.vacuum_text_color).move_to(self.adskmRS.get_center()).shift(0.5*DOWN)
        self.out_text_RS= self.in_text_RS.copy().move_to(self.adskpRS.get_center()).shift(0.5*DOWN)
        self.sym= MathTex("\\mathbb{Z}_{2}", color= self.brane_color).move_to(self.brane.get_corner(UL)+ [0.3,0.1,0])
        
        #Geometry (DB)
        self.adskpDB= RoundedRectangle(corner_radius= self.corner_rad, height= 4,  width= 4, stroke_width= self.vacuum_stroke_w, color= self.vacuum_color, fill_opacity= self.vacuum_fill_opa)
        self.adskmDB= RoundedRectangle(corner_radius= self.corner_rad, height= 4,  width= 4, stroke_width= self.vacuum_stroke_w, color= self.vacuum_color, fill_opacity= self.vacuum_fill_opa + 0.3).flip()
        self.adskpDB.next_to(self.brane, RIGHT, buff= 0.1, aligned_edge= DOWN)
        self.adskmDB.next_to(self.brane, LEFT, buff= 0.1, aligned_edge= DOWN)
        
        #Text (DB)
        in_text_DB= self.in_text_RS.copy().move_to(self.adskmDB.get_center()).shift(0.5*DOWN)
        self.out_text_DB= MathTex("\\Lambda_{5D}= -6 k_{+}^{2}", color= self.vacuum_text_color).move_to(self.adskpDB.get_center()).shift(0.5*DOWN)
        
        #Arrows
        self.arrowRS= Arrow(max_stroke_width_to_length_ratio= 8, color= arrow_color, start= LEFT, end= [0.3,0,0]).move_to(self.adskmRS.get_left())
        self.arrowDB= self.arrowRS.copy().set_color(arrow_color).move_to(self.adskmDB.get_left())
        
        if vacua_type== "RS":
            self.object= VGroup(self.brane, self.adskmRS, self.in_text_RS, self.adskpRS, self.out_text_RS, self.sym, self.arrowRS)
            self.add(self.object)
            
        if vacua_type== "DB":
            self.object= VGroup(self.brane, self.adskmDB, in_text_DB, self.adskpDB, self.out_text_DB, self.arrowDB)
            self.add(self.object)
            
    # Animations #
    @override_animation(FadeIn)

    def fade_in(
        self,
        rt: float= 1,
        rf: float= linear)-> Animation: #There is an issue with adding the group and scaling or shifting position of it. If I do not add the whole group from the very beginning, the system will not rescale those elements that I will add later. In order to solve this issue, I override the FadeIn animation to avoid this issue.

        """

        Args::

            - rt (float, optional): run_time animation. Defaults to 1.
            - rf (float, optioanl): rate function. Defaults to linear.

        Returns::

            - Animation: FadeIn animation of the group without the arrow.

        """

        return FadeIn(self.object[:-1], run_time= rt, rate_function= rf)
            
    def fade_in_arrow(self, 
               rt: float= 2,
               rf: float= linear)-> Animation: #The arrow associates this method with a class animation.
        """
        Args:

            - rt (float, optional): run_time animation. Defaults to 1.
            - rf (float, optioanl): rate function. Defaults to linear.

        Returns:

            - Animation: FadeIn the arrow of the group.

        """
        
        return FadeIn(self.object[-1],  run_time= rt, rate_func= rf)
    
    def show_symmetry(self, 
               rt: float= 2,
               rf= linear)-> Succession: # The arrow associated this method with a class animation.
        """
        Args:
            - rt (float, optional): run_time animation. Defaults to 1.
            - rf (float, optioanl): rate function. Defaults to linear.

        Returns:
            - Animation: Removes outside vacuum and bend over the Z2 sym to simulate the action of the self.symmetry.

        .. note::

            This method only works with RS-type. Recall. The Dark Bubble has a proper inside and outside.

        """
       
        return Succession(
            FadeOut(self.object[-3], run_time= rt/2, rate_func= rf),
            Rotate(self.object[-4], about_point= self.object[0].get_center(), axis= [0,-1,0], run_time= rt/2, rate_func= rf))
        
        
    def restore_symmetry(self,
                rt: float= 2,
                rf= linear)-> Succession:
        """
        Args:
            - rt (float, optional): Defaults to 1.
            - rf (_vacua_type_, optional): Defaults to linear.

        Returns:
            - Animation: Restores previous symmetry.

        """
            
        return Succession(
            Rotate(self.object[-4], about_point= self.object[0].get_center(), axis= [0,1,0], run_time= rt/2, rate_func= rf),
            FadeIn(self.object[-3], run_time= rt/2, rate_func= rf))
        
    
    def show_n_vector_rs(self,
                     rt: float= 2,
                     rf= linear)-> Succession:
        """
        Args:
            - rt (float, optional): Defaults to 1.
            - rf (_type_, optional): Defaults to linear.

        Returns:
           - Animation: Shows the behaviour of the normal vector across the vacua in the RS model.

        """
        center= self.object[0].get_center()
        
        return Succession(
                    self.object[-1].animate(rate_func= rf).move_to(center).build(),
                    Rotate(self.object[-1], angle= PI, about_point= center, rate_func= rf),
                    self.object[-1].animate(rate_func= rf).rotate(PI).move_to(self.object.get_right()), run_time= rt, rate_func= rf)
        
    def show_n_vector_db(self,
                     rt: float= 2,
                     rf= linear)-> Succession:
        """
        Args:
            - rt (float, optional): Defaults to 1.
            - rf (_type_, optional): Defaults to linear.

        Returns:
            - Animation: Shows the behaviour of the normal vector across the vacua in the DB model.
        """
        
        return Succession(
                    self.object[-1].animate(rate_func= rf).move_to(self.object.get_right()),
                    run_time= rt, rate_func= rf)
        
    
        
    
    
    
    