#This file is to define imports all parameter choices for the template file and load it to any of the classes in these libraries.
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))) #To import the documentation from the mtheoretical directory
from mtheoretical.src.text_and_organisation import *
from mtheoretical.src.equations import *
from mtheoretical.src.tables_and_plots import *
from mtheoretical.src.objects import *
from manim import *
from .template_1 import *

""".. note::
        Here I add some test info.
    """


#Defining the background color of the video. Check how to define a background_color for presentations

config.background_color= bg_color

#Definition of Tex defaults. This will change font and its color.
#Carefull! It seems that there exist some FontTemplates which do not automatically scale the parenthesis. This drove me crazy for some hours. Be aware of what font you choose.

Tex.set_default(tex_template= tex_temp)
MathTex.set_default(tex_template= tex_temp)

#Titles #Note that the corner_rad can be negative!
#It seems that back_frame fits good both with box in text and nothing as decorator.

Title_General.set_default( #Be careful with general size and observe that title_sections are defined to UL corner by default.
    text_size= t_size,
    text_color= t_color,
    decorator_presence= d_presence_1,
    decorator_color= d_color,
    decorator_stroke_width= d_s_w,
    corner_rad= c_rad,
    corner_rad_direction= c_rad_dir_title,
    fill_opa= f_opa,
    tightness= tight,
    stroke_opa= s_opa)

#Bulleted Box and References recommended to mirror if two different boxes are displayed close to each other

Text_General.set_default( #Be careful with general size
    text_size= t_size,
    text_color= t_color,
    decorator_presence= d_presence_2,
    decorator_color= d_color,
    decorator_stroke_width= d_s_w,
    corner_rad= c_rad,
    corner_rad_direction= c_rad_dir_boxes,
    fill_opa= f_opa,
    tightness= tight,
    stroke_opa= s_opa,
    dot_scale= dot_size)

Ref.set_default(
    text_color= d_color,
    decorator_presence= d_ref) #Each reference will require its own definition, as one can play with the boxes and flip them to close the design and so on. To think if this can be optimised.

#Any equation 
Eq_General.set_default(
    text_size= t_size, 
    text_color= t_color,
    decorator_presence= "box",
    decorator_color= d_color,
    decorator_stroke_width= d_s_w,
    corner_rad= c_rad,
    corner_rad_direction= c_rad_dir_boxes,
    fill_opa= f_opa,
    tightness= tight)

#Any Table
Table_General.set_default(
    text_color= t_color,
    hlight_1_color= h_1,
    hlight_2_color= h_2,
    hlight_3_color= h_3,
    corner_rad= c_rad,
    corner_rad_direction= c_rad_dir_boxes,
    decorator_color= t_color,
    decorator_stroke_w= d_s_w,
    stroke_opa= s_opa,
    fill_opa= f_opa)

#Any Plot (There are things to change and solve)
Plot_General.set_default(
    func_main_color= h_1,
    func_2_color= h_2,
    func_3_color= h_3,
    text_color= t_color,
    axis_opacity= s_opa,
    axis_stroke= d_s_w,
    decorator_presence= "box",
    decorator_color= h_1,
    decorator_stroke_w= d_s_w,
    corner_rad= c_rad,
    corner_rad_direction= c_rad_dir_boxes,
    fill_opa= 0,
    stroke_w= d_s_w,
    stroke_opa= s_opa,
    tightness= tight)

#Figures and Objects
Brane_General.set_default( #Any brane appearing in objects
    brane_color= h_1,
    brane_fill_opa= 0.1,
    brane_text_color= WHITE,
    brane_stroke_w= 2)

Vacuum_General.set_default( #Any vacuum appearing in objects
    vacuum_color= h_3,
    vacuum_fill_opa= f_opa,
    vacuum_stroke_w= d_s_w,
    direction_corner_rad= c_rad_dir_boxes,
    corner_rad= c_rad,
    vacuum_text_color= t_color)

#Black hole
Black_Hole.set_default(
    bh_size= 1,
    bh_color= t_color,
    bh_fill_opa= 0.7)

#Random Photo Frame
Photo.set_default(
    style= "techno", 
    text_size= t_size,
    text_color= t_color,
    decorator_color= h_1,
    pin_color= h_1,
    corner_rad= c_rad,
    decorator_stroke_w= 5*d_s_w) #Recommended high width to not see picture borders

#Post-it
Post_It.set_default(
    text_color= t_color,
    text_size= t_size,
    pin_color= h_2) 



####################################################

