from manim import *
from .table_general import *

class Table_Summary_Induce(Table_General, VGroup):
    """ Class to display a table with all relations between 4D and higher dimension fields and the papers where they are discussed. See Table_General Class.

    """
    
    def __init__(self, **kwargs):
        
        super().__init__(**kwargs)
        
        # To add more lines if new research happens   
        self.sum_tab= MathTable(
            [["5D", "4D", "Article"],
            ["\Lambda_{5}^{(\pm)} <0, \\: r= a(\\tau)", "\Lambda_{4}>0", "1807.01570"],
            ["M","Radiation \propto \\tfrac{1}{a^{4}}", "1907.04268"],
            ["Strings^{*}", "Dust \propto \\tfrac{1}{a^{3}}","1907.04268"],
            ["\delta g_{\mu \\nu}", "\delta g_{ab}", "2202.00545"],
            ["H_{\\mu \\nu \\gamma}", "F_{ab}", "2310.15032"]],line_config={"stroke_width": self.stroke_w, "color": self.text_color},
            include_outer_lines= False, v_buff= 0.2, h_buff= 0.7, stroke_opacity= self.fill_opa*2).set(color= self.text_color)
        self.sum_tab.set_color(self.text_color)
        self.box= RoundedRectangle(corner_radius= self.corner_rad, height= self.sum_tab.get_height(),  width= self.sum_tab.get_width(), stroke_width= self.decorator_stroke_w, color=  self.decorator_color, fill_opacity= 0).set_z_index(1)     
        self.sum_tab.add_highlighted_cell((1,1), color= self.hlight_1_color, corner_radius= list(0.2*np.array([1,0,0,0])), fill_opacity= self.fill_opa) #To bend only the left corners
        self.sum_tab.add_highlighted_cell((1,2), color= self.hlight_2_color, fill_opacity= self.fill_opa)
        self.sum_tab.add_highlighted_cell((1,3), color= self.hlight_3_color, corner_radius= list(0.2*np.array([0,0,0,1])), fill_opacity= self.fill_opa) #To bend only the left corners)
        
        self.add(self.sum_tab, self.box)