import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from manim import *
from mtheoretical.src.equations import *
from mtheoretical.src.templates import *

class Example_Eq_Metric(Scene):
    def construct(self):
        keys= list(Eq_Metric("induced metric").eq_metric_refs.keys()) #to get the keys of the dictionary
        keys_tex= VGroup(*[Tex(key, color= BLUE, font_size= 20) for key in keys]).arrange(DOWN, aligned_edge= LEFT, buff= 0.1) # to print the keys
        eq_try= VGroup(*[Eq_Metric(key)for key in keys]).arrange(DOWN, aligned_edge= LEFT, buff= 0.1).scale_to_fit_height(keys_tex.get_height()).next_to(keys_tex, RIGHT, buff= 0.1)
        all_together= Group(eq_try, keys_tex).scale_to_fit_width(config.frame_width-1).to_corner(LEFT)

        self.add(all_together)
        
class Example_Eq_Cosmo(Scene):
    def construct(self):
        keys= list(Eq_Cosmo("fried ind").eq_cosmo_refs.keys())
        keys_tex= VGroup(*[Tex(key, color= BLUE, font_size= 10) for key in keys]).arrange(DOWN, aligned_edge= LEFT, buff= 0.1)
        eq_try= VGroup(*[Eq_Cosmo(key) for key in keys]).arrange(DOWN, aligned_edge= LEFT, buff= 0.1).scale_to_fit_height(keys_tex.get_height()).next_to(keys_tex, RIGHT, buff= 0.1)
        all_together= Group(eq_try, keys_tex).scale_to_fit_height(config.frame_height-1).to_corner(LEFT)

        self.add(all_together)

class Example_Eq_Action(Scene):
    def construct(self):
        keys= list(Eq_Action("bubble action 5d").eq_action_refs.keys())
        keys_tex= VGroup(*[Tex(key, color= BLUE, font_size= 15) for key in keys]).arrange(DOWN, aligned_edge= LEFT, buff= 0.1)
        eq_try= VGroup(*[Eq_Action(key).scale_to_fit_height(keys_tex[0].get_height())for key in keys]).arrange(DOWN, aligned_edge= LEFT, buff= 0.1).scale_to_fit_height(keys_tex.get_height()).next_to(keys_tex, RIGHT, buff= 0.1)
        all_together= Group(eq_try, keys_tex).scale_to_fit_width(config.frame_width-1).to_corner(LEFT)

        self.add(all_together)
        
class Example_Eq_Junc(Scene):
    def construct(self):
        keys= list(Eq_Junc("junc generic 1").eq_junc_refs.keys())
        keys_tex= VGroup(*[Tex(key, color= BLUE, font_size= 20) for key in keys]).arrange(DOWN, aligned_edge= LEFT, buff= 0.1)
        eq_try= VGroup(*[Eq_Junc(key).scale_to_fit_height(keys_tex[0].get_height())for key in keys]).arrange(DOWN, aligned_edge= LEFT, buff= 0.1).scale_to_fit_height(keys_tex.get_height()).next_to(keys_tex, RIGHT, buff= 0.1)
        all_together= Group(eq_try, keys_tex).scale_to_fit_height(config.frame_height-1).to_corner(LEFT)

        self.add(all_together)
        
class Example_Eq_GC(Scene):
    def construct(self):
        keys= list(Eq_GC("gc initial").eq_gc_refs.keys())
        keys_tex= VGroup(*[Tex(key, color= BLUE, font_size= 5) for key in keys]).arrange(DOWN, aligned_edge= LEFT, buff= 0.1)
        eq_try= VGroup(*[Eq_GC(key).scale_to_fit_height(keys_tex[0].get_height())for key in keys]).arrange(DOWN, aligned_edge= LEFT, buff= 0.1).scale_to_fit_height(keys_tex.get_height()).next_to(keys_tex, RIGHT, buff= 0.1)
        all_together= Group(eq_try, keys_tex).scale_to_fit_width(config.frame_width-1).to_corner(LEFT)

        self.add(all_together)
        
class Example_Eq_EM(Scene):
    def construct(self):
        keys= list(Eq_EM("action em").eq_em_refs.keys())
        keys_tex= VGroup(*[Tex(key, color= BLUE, font_size= 20) for key in keys]).arrange(DOWN, aligned_edge= LEFT, buff= 0.1)
        eq_try= VGroup(*[Eq_EM(key).scale_to_fit_height(keys_tex[0].get_height())for key in keys]).arrange(DOWN, aligned_edge= LEFT, buff= 0.1).scale_to_fit_height(keys_tex.get_height()).next_to(keys_tex, RIGHT, buff= 0.1)
        all_together= Group(eq_try, keys_tex).scale_to_fit_width(config.frame_width-1).to_corner(LEFT)

        self.add(all_together)

class Example_Eq_Corrections(Scene):
    def construct(self):
        keys= list(Eq_Brane_Corrections("new lambda").eq_brane_corrections_refs.keys())
        keys_tex= VGroup(*[Tex(key, color= BLUE, font_size= 20) for key in keys]).arrange(DOWN, aligned_edge= LEFT, buff= 0.1)
        eq_try= VGroup(*[Eq_Brane_Corrections(key).scale_to_fit_height(keys_tex[0].get_height())for key in keys]).arrange(DOWN, aligned_edge= LEFT, buff= 0.1).scale_to_fit_height(keys_tex.get_height()).next_to(keys_tex, RIGHT, buff= 0.1)
        all_together= Group(eq_try, keys_tex).scale_to_fit_width(config.frame_width-1).to_corner(LEFT)

        self.add(all_together)
        
class Example_Eq_Scales(Scene):
    def construct(self):
        keys= list(Eq_Scales_DB("hierarchy expected").eq_scales_db_refs.keys())
        keys_tex= VGroup(*[Tex(key, color= BLUE, font_size= 20) for key in keys]).arrange(DOWN, aligned_edge= LEFT, buff= 0.1)
        eq_try= VGroup(*[Eq_Scales_DB(key).scale_to_fit_height(keys_tex[0].get_height())for key in keys]).arrange(DOWN, aligned_edge= LEFT, buff= 0.1).scale_to_fit_height(keys_tex.get_height()).next_to(keys_tex, RIGHT, buff= 0.1)
        all_together= Group(eq_try, keys_tex).scale_to_fit_width(config.frame_width-1).to_corner(LEFT)

        self.add(all_together)

class Example_Eq_Quantum(Scene):
    def construct(self):
        #This one has several equations in groups. Requires a different way
        keys= ['wdw', 'wave', 'prob boundaries', 'prob comparison']
        keys_tex= VGroup(*[Tex(key, color= BLUE, font_size= 70) for key in keys]).arrange(DOWN, aligned_edge= LEFT, buff= 0.1)
        eq_try= VGroup(*[Eq_Quantum_Cosmo(key).scale_to_fit_height(keys_tex[0].get_height())for key in keys]).arrange(DOWN, aligned_edge= LEFT, buff= 0.1).scale_to_fit_height(keys_tex.get_height()).next_to(keys_tex, RIGHT, buff= 0.1)
        all_together= Group(eq_try, keys_tex).scale_to_fit_width(config.frame_width-1).to_corner(LEFT)
        
        self.add(all_together)