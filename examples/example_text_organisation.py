import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from manim import *
from mtheoretical.text_and_organisation import *
from mtheoretical.equations import *
from mtheoretical.templates import *


class Title_Slide(Scene):
    def construct(self):
        self.add(Title_Presentation("An Useless Title to Show", "Your Mama University", author= "A Dashing Monkey"))

class Generic_Slide(Scene):
    def construct(self):
        slide_title= Title_Section("This is a really long title to check capabilities")
        ref1= Ref("fake ref").to_corner(UR)
        
        important_point= BlB(["This is extremely important", "Use .next\\_point() to iterate over points", "... And for the last point you can recover all points in the initial color"]).to_corner(LEFT)
        eq= Eq_Metric("induced metric").to_corner(DOWN)

        self.play(slide_title.show_title())
        self.play(FadeIn(ref1, important_point))
        self.play(important_point.next_point())
        self.play(important_point.next_point())
        self.play(important_point.next_point())
        self.play(important_point.next_point())
        self.play(FadeIn(eq, shift= UP))
    