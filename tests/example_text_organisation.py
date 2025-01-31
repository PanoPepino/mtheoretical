from manim import *
from beanim import *

class Title_Slide(Scene):
    def construct(self):
        self.add(Title_Presentation("An Useless Title to Show", "Your Mama University", author= "A Dashing Monkey"))

class Generic_Slide(Scene):
    def construct(self):
        slide_title= Title_Section("This is a really long title to check capabilities")
        ref1= Ref("fake ref").to_corner(UR)
        important_points= BlB(["This is extremely important",
                              "Use .next\\_point() to iterate over points",
                              "... And for the last point you can recover all points in the initial color"]).to_corner(LEFT)
        self.play(slide_title.show_title())
        self.play(FadeIn(ref1, important_points))
        for point in range(len(important_points)+2):
            self.play(important_points.next_point())

class Example_Equation(Scene):
    def construct(self):
        eq_show= Eq_General(the_dictionary= 'equation_dictionaries/eq_quantum.txt', the_equation= 'prob boundaries')
        self.add(eq_show)

