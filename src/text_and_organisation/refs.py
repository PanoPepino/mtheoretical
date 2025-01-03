from manim import *
from .text_general import *

class Ref(Text_General, VGroup):
    """Class to create citations of References. It has a dictionary built in.

    Parameters: (See Text_General Class)
    -----------

    - ref_number (str): the hepth number of the article to refer to.
    - text_size (float, optional): Defaults to 25.
    - text_color (ParsableManimColor, optional): Defaults to BLACK.
    - decorator_presence (str, optional): box/no. Defaults to box. If no, does not return the surrounding box.
    - decorator_color (ParsableManimColor, optional): Defaults to BLACK.
    - decorator_stroke_width (float, optional): Defaults to 2.
    - corner_rad (float, optional): Corner radious of surrounding box. Defaults to 0.3.
    - corner_rad_direction (list, optional): which corners get rounded. Defaults to [1, 1, 1, 1].
    - fill_opa (float, optional): Fill opacity of the surrounding box. Defaults to 0.1.
    - tightness (float, optional): How tight the box around the title is. Defaults to 0.5.
    - stroke_opa (float, optional): Defaults to 1.
    - dot_scale (float, optional): Defaults to 2.
    
    """
    def __init__(self,
                 ref_number,
                 **kwargs):
        
        super().__init__(**kwargs)
        
        dic_refs= {
            
            'fake ref': '[Adonis, Basado, Charo, XXYYZZ]',
            'Is 1966': '[W. Israel, Nuovo Cim. B44S10, (1966)]',
            'CL 1980': '[Coleman, de Lucia,Phys. Rev. D 21, 3305, (1980)]', 
            '9812073': '[Maldacena, Michelson, Strominger, 9812073]', 
            '990522': '[Randall, Sundrum, hep-th/990522]', 
            '161001533': '[Oouguri, Vafa,  1610.01533]',
            '161004564': '[Freivogel, Kleban, 1610.04564]', 
            '180401120': '[Danielsson, Van Riet, 1804.01120]', 
            '180608362': '[Obied, Ooguri, Spodyneiko,Vafa, 1806.08362]', 
            '180701570': '[Banerjee, Danielsson, Dibitetto, Giri, Schillo, 1807.01570]', 
            '190701562': '[Henrikson, Hoyo, Jokela, 1907.01562]', 
            '190704628': '[Banerjee, Danielsson, Dibitetto, Giri, Schillo, 1907.04268]', 
            '200713757': '[Basile, Lanza, 2007.13757]', 
            '21020111': '[van Beest, Calderón-Infante, Mirfendereski, Valenzuela, 2102.0111]', 
            '210202164': '[Barnejee, Danielsson, Giri, 2102.02164]', 
            '210503253': '[Danielsson, DP, Tielemans, van Riet, 2105.03253]', 
            '220200545': '[Danielsson, DP, Tielemans, 2202.00545]', 
            '220512293': '[Montero, Vafa, Valenzuela, 2205.12293]', 
            '221110191': '[Danielsson, Henriksson, DP, 2211.10191]', 
            '231015032': '[Basile, Danielsson, Giri, DP, 2310.15032]', 
            '231114589': '[Danielsson, DP, 2311.14589]',
            '241105912': '[Muntz, Padilla, Saffin, 2411.05192]'
         }
        
        self.chosen_ref= Tex(dic_refs[ref_number], font_size= 0.8*self.text_size, color= self.text_color)
        
        if self.decorator_presence == "box":
            self.box= SurroundingRectangle(self.chosen_ref, corner_radius= self.corner_rad, buff= self.tightness,  stroke_width= self.decorator_stroke_width, color= self.decorator_color, fill_opacity= self.fill_opa, stroke_opacity= self.stroke_opa)
            self.add(self.chosen_ref, self.box)
        else:
            self.add(self.chosen_ref)
        
            
        
        