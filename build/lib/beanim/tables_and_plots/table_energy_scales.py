from .table_general import *
from ..my_imports import *

__all__=['Table_Energy_Scales']

class Table_Energy_Scales(Table_General, VMobject):
    """ Class to display the table of energy scales of the dark bubble embedding. See Table_General Class.
      
    """

    def __init__(self,              
                 **kwargs):
    
        super().__init__(**kwargs)
        
        #Coordinates
        title= VGroup(Tex("Scale"), MathTex("{\\rm Length} (m)"), Tex("Energy"))
        ads_scale= VGroup(MathTex("L"), MathTex("5.1 \\times10^   {-5} "), MathTex("3.8 \\, {\\rm meV}"))
        string_scale= VGroup(MathTex("\\sqrt{\\alpha'}"),MathTex  ("1.8 \\times 10^{-20} "), MathTex("11.2 \\,{\\rm TeV}"))
        sugra_scale= VGroup(MathTex("\\tilde{\\ell}_{10}"),MathTex    ("1.4 \\times 10^{-20} "), MathTex("13.7 \\,{\\rm TeV}"))
        bulk_scale= VGroup(MathTex("\\tilde{\\ell}_{5}"),MathTex  ("3.9 \\times 10^{-45} "), MathTex("5.1 \\times10^{28} \\,   {\\rm TeV}"))
        
        #Table definition and border
        opa_table= self.fill_opa+0.1 #So it is a little more intense.
        self.tab= MobjectTable([title, ads_scale, string_scale, sugra_scale, bulk_scale],
            line_config= {"stroke_width": self.stroke_w, "color": self.text_color},
            include_outer_lines= False, v_buff= 0.2, h_buff= 0.7, stroke_opacity= self.fill_opa*2).set(color= self.text_color)
        self.tab.add_highlighted_cell((1,1), color= self.hlight_1_color, fill_opacity= opa_table, corner_radius= list(self.corner_rad[0]*np.array([1, 0, 0, 0]))).set_z_index(-1) # to bend only left side.
        self.tab.add_highlighted_cell((1,2), color= self.hlight_2_color, fill_opacity= opa_table).set_z_index(-1)       
        self.tab.add_highlighted_cell((1,3), color= self.hlight_3_color,
        fill_opacity= opa_table, corner_radius= list(self.corner_rad[0]*np.array([0, 0, 0, 1]))).set_z_index(-1) 
               
        self.box= RoundedRectangle(corner_radius= self.corner_rad, height=self.tab.get_height(),  width=self.tab.get_width(), stroke_width= self.decorator_stroke_w, color= self.decorator_color,  fill_opacity= 0)
        self.add(self.tab, self.box)