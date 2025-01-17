from manim import *
from .table_general import *


class Table_Bh_Embedding(Table_General, Group):
    """Class to represent a table of the coordinates of the embedding of the dark bubble. See Table_General Class. It can display the whole table (type= together) or divided (type= split). It has three methods (animations).

    - **Parameters**::

        - type (str, optional): There are two types:
            - "together", this will display all 9 spatial directions in
            the same row.
            - "split": It will display compact and non-compact dimesions 
            in two different tables.
        - chosen_position (str, optional): The relative position of the
        compact dimensions with respect to uncompact. Defaults to RIGHT.

    - **Example**::

        from manim import*
        from mtheoretical import *

        class Example_Table_Bh_Embedding(Scene):
            def construct(self):
                together= Table_Bh_Embedding(type= "together")
                together.scale_to_fit_width(config.frame_width-1).shift(UP)
                split= Table_Bh_Embedding(type= "split", chosen_position= RIGHT)
                split.scale_to_fit_width(config.frame_width-1).next_to(together, DOWN, buff= 0.2)
                self.add(together, split)
                self.play(AnimationGroup(together.move_all(), 
                                        split.move_non_compact(), 
                                        split.move_compact()))
        
            
    - **Methods**:
   
    """
    
    def __init__(self,
                 type: str= "together", 
                 chosen_position: list= RIGHT,
                 **kwargs):
        
        super().__init__(**kwargs)
        
        ### DEFINITION OF COORDINATES ####
            
        #Coordinates
        coordinates= ["\\alpha", "\\beta", "\\gamma", "\\mathcal{Z}", "\\Theta","\\Psi", "\phi_{1}","\phi_{2}","\phi_{3}"]
        
        coordinates_non_compact= coordinates[0:4]
        coordinates_compact= coordinates[4:]
            
        coordinates_mob_non_compact= VGroup(*[MathTex(coordinates_non_compact[i], font_size=60) for i in  range(len(coordinates_non_compact))])
        coordinates_mob_compact= VGroup(*[MathTex(coordinates_compact[i], font_size=60) for i in range(len(coordinates_compact))])
           
        
        #Dimension representation
        
        #4D
        three_dim= VGroup(*[RoundedRectangle(corner_radius= self.corner_rad, height= 1.4, width= 1.4, color= self.hlight_1_color, fill_opacity= 2*self.fill_opa, stroke_width= self.stroke_w) for _ in range(3)])
        
        #Ads Throat
        self.ads_dim= Line(color= self.hlight_2_color, stroke_width= 0.7).rotate(PI/4)
        self.position_ads_dim= Dot(color= self.hlight_2_color).scale(1.5).move_to(self.ads_dim.get_start())
        
        non_compact_dim= VGroup().add(*[ts for ts in three_dim]).add(VGroup(self.ads_dim, self.position_ads_dim))
        
        #Compact space
        cicle= Circle(radius= 0.7, stroke_width= self.stroke_w, color= self.hlight_3_color).rotate(-PI/2)
        position_cicle= Dot(color= self.hlight_3_color).scale(1.5).move_to(cicle.get_end())
            
        comp= VGroup(cicle, position_cicle)
        self.compact_dim= VGroup(*[comp.copy() for _ in range(len(   coordinates_mob_compact))])

        for i in range(1,4):
            self.compact_dim[-i][-1].move_to(cicle[-1][0].get_start())
            
        tab_non_compact= MobjectTable([coordinates_mob_non_compact, non_compact_dim],
        line_config={"stroke_width": self.stroke_w, "color": self.decorator_color},
        include_outer_lines= False)
        box_non_compact= RoundedRectangle(corner_radius= self.corner_rad, height= tab_non_compact.get_height(),  width= tab_non_compact.get_width(), stroke_width= self.decorator_stroke_w, color= self.decorator_color, fill_opacity= 0).set_z_index(-3)
        
        for i in range(4):
            if i==0:
                tab_non_compact.add_highlighted_cell((1,i+1), color= self.hlight_1_color, fill_opacity= self.fill_opa, corner_radius= list(0.2*np.array([1, 0, 0, 0]))) # to bend only left corner
                coordinates_mob_non_compact[i].set(color= self.hlight_1_color, fill_opacity= self.fill_opa)
            elif i==3:
                tab_non_compact.add_highlighted_cell((1,i+1), color= self.hlight_2_color, fill_opacity= self.fill_opa, corner_radius= list(0.2*np.array([0, 0, 0, 1])))
                coordinates_mob_non_compact[i].set(color= self.hlight_2_color, fill_opacity= self.fill_opa)
            else:
                tab_non_compact.add_highlighted_cell((1,i+1), color= self.hlight_1_color, fill_opacity= self.fill_opa)
                coordinates_mob_non_compact[i].set(color= self.hlight_1_color, fill_opacity= self.fill_opa)
        
        tab_compact= MobjectTable([coordinates_mob_compact, self.compact_dim],
        line_config= {"stroke_width": self.stroke_w, "color": self.decorator_color},
        include_outer_lines= False)
        box_compact= RoundedRectangle(corner_radius= self.corner_rad, height= tab_compact.get_height(),  width= tab_compact.get_width(), stroke_width= self.decorator_stroke_w, color= self.decorator_color, fill_opacity= 0).set_z_index(-3)
        
        for i in range(len(coordinates_mob_compact)):
            if i==0:
                tab_compact.add_highlighted_cell((1,i+1), color= self.hlight_3_color, fill_opacity= self.fill_opa, corner_radius= list(0.2*np.array([1, 0, 0, 0])))
                coordinates_mob_compact[i].set(color= self.hlight_3_color, fill_opacity= self.fill_opa)
            elif i==4:
                tab_compact.add_highlighted_cell((1,i+1), color= self.hlight_3_color, fill_opacity= self.fill_opa, corner_radius= list(0.2*np.array([0, 0, 0, 1])))
                coordinates_mob_compact[i].set(color= self.hlight_3_color, fill_opacity= self.fill_opa)
            else:
                tab_compact.add_highlighted_cell((1,i+1), color= self.hlight_3_color, fill_opacity= self.fill_opa)
                coordinates_mob_compact[i].set(color= self.hlight_3_color, fill_opacity= self.fill_opa)
            
           
        ## ALL DIMENSIONS TOGETHER ##
             
        self.all_dimensions= non_compact_dim.copy().add(*[element.copy() for element in self.compact_dim.copy()])
        self.all_coordinates= coordinates_mob_non_compact.copy().add(*[element.copy() for element in coordinates_mob_compact.copy()])
        
        tab_all= MobjectTable([self.all_coordinates, self.all_dimensions],
                               line_config={"stroke_width": self.stroke_w, "color": self.decorator_color},include_outer_lines= False)
        box_all= RoundedRectangle(corner_radius= self.corner_rad, height= tab_all.get_height(),  width= tab_all.get_width(), stroke_width= self.decorator_stroke_w, color= self.decorator_color, fill_opacity= 0).set_z_index(-3)
        
        for i in range(9):
            if i==0:
                tab_all.add_highlighted_cell((1,i+1), color= self.hlight_1_color, fill_opacity= self.fill_opa, corner_radius= list(0.2*np.array([1, 0,0,0])))
                self.all_coordinates[i].set(color= self.hlight_1_color, fill_opacity= self.fill_opa)
            elif i==8:
                tab_all.add_highlighted_cell((1,i+1), color= self.hlight_3_color, fill_opacity= self.fill_opa, corner_radius= list(0.2*np.array([0, 0,0, 1])))
                self.all_coordinates[i].set(color= self.hlight_3_color, fill_opacity= self.fill_opa)
            elif 0< i < 3:
                tab_all.add_highlighted_cell((1,i+1), color= self.hlight_1_color, fill_opacity= self.fill_opa)
                self.all_coordinates[i].set(color= self.hlight_1_color, fill_opacity= self.fill_opa)
            elif i== 3:
                tab_all.add_highlighted_cell((1,i+1), color= self.hlight_2_color, fill_opacity= self.fill_opa)
                self.all_coordinates[i].set(color= self.hlight_2_color, fill_opacity= self.fill_opa)
            else:
                tab_all.add_highlighted_cell((1,i+1), color= self.hlight_3_color, fill_opacity= self.fill_opa)
                self.all_coordinates[i].set(color= self.hlight_3_color, fill_opacity= self.fill_opa)
        
            
        if type== "together":
            self.add(tab_all, box_all)
            
        elif type== "split":
            comp= VGroup(tab_non_compact, box_non_compact)
            noncomp= VGroup(tab_compact, box_compact).scale_to_fit_width(comp.get_width())
            noncomp.next_to(comp, chosen_position)
            self.add(comp, noncomp)
        
    def move_non_compact(self,
                         rt: float= 3,
                         rf: float= rate_functions.linear)-> Animation:
        """

        Args:
            - rt (float, optional): Defaults to 3.
            - rf (float, optional): Defaults to rate_functions.linear.

        Returns: Animation to move the brane through the AdS throat.

        """
        
        return MoveAlongPath(self.position_ads_dim, self.ads_dim, rate_functions= rf, run_time= rt)
    
    def move_compact(self,
                     rt: float= 3,
                     rf: float= rate_functions.linear)-> AnimationGroup:
        """

        Args:
            - rt (float, optional): Defaults to 3.
            - rf (float, optional): Defaults to rate_functions.linear.

        Returns: To move the brane through the compact dimensions.
        """
        
        return AnimationGroup(*[MoveAlongPath(self.compact_dim[-i][-1], self.compact_dim[-i][0], rate_functions= rf, run_time= rt) for i in range(1,4)])
    
    def move_all(self,
                 rt: float= 3,
                 rf: float= rate_functions.linear)-> AnimationGroup:
        """

        Args:
            - rt (float, optional): Defaults to 3.
            - rf (float, optional): Defaults to rate_functions.linear.

        Returns: To move the brane through all coordinates.

        """
        
        return AnimationGroup(*[MoveAlongPath(self.all_dimensions[-i][-1], self.all_dimensions[-i][0], rate_functions= rf, run_time= rt) for i in range(1,4)], MoveAlongPath(self.all_dimensions[3][-1], self.all_dimensions[3][0], rate_functions= rf, run_time= rt))
        
            
            
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
  
        
        
        
            
    


