from manim import *

#Here you can modify almost all parameters of objects used in these libraries. In this way you can generate new homogenous templates for your presentations.

#Color of the background
bg_color= WHITE

#Font color and text size for any text and MathTex
tex_temp= TexFontTemplates.latin_modern_tw
t_size= 30
t_color= BLACK

#Design of all the surrounding boxes (titles, refs, bullet points, vacua and similar) and general opacities
d_presence_1= "back_frame" #What type of decorator surrounding the main title and section titles
d_presence_2= "box" #What type of decorator surrounding bulleted lists
d_ref= "none" #What type of decorator surrounding references. Notice that refs that do not go to the UR corner should be individually modified to have a box. Refs have the color of the decorator
d_color= GREEN #Color of all decorators
d_s_w= 0 #Stroke width of all decorator and surrounding boxes
c_rad= 0.1 #Curvature of the corners of such objects
c_rad_dir_title= [1, 1, 0, 0] #Which corners get curved for titles
c_rad_dir_boxes= [1, 1, 1, 1] #Same, but for boxes
f_opa= 0.2 #Opacity of background of things
tight= 0.3 #How tight is the decorator with respect to the object it contains.
s_opa= 0.2 #Stroke opacity of the border
dot_size= 2 #How big the bullet points are

#Color homogenisation
h_1= GREEN
h_2= DARK_GRAY
h_3= DARK_BLUE
b_color= RED
v_color= RED_C