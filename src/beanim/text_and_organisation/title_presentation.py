from ..my_imports import *
from .title_general import *

__all__ = ["Title_Presentation"]


class Title_Presentation(Title_General, VGroup):
    """Class to generate titles for presentations. Generates a group with the title and a background decorator.

    - **Parameters**::

            - title ("str"): Title of your talk.
            - affiliation ("str"): Your university or institution.
            - author ("str"): Who has crafted the slides.

    - An **Example** of this is::

        from manim  import *
        from beanim import *

        class Title_Slide(Scene):
            def construct(self):
                self.add(Title_Presentation(title= "An Useless Title to Show",
                                            affiliation= "Your Mama University",
                                            author= "A Dashing Monkey"))

    """

    def __init__(self, title, affiliation, author, **kwargs) -> VGroup:
        super().__init__(**kwargs)

        # text
        tit = Tex(title, font_size=2 * self.text_size, color=self.text_color)
        nam = Tex(author, font_size=1.5 * self.text_size, color=self.text_color)
        uni = Tex(affiliation, font_size=self.text_size, color=self.text_color)
        self.text_group = VGroup(tit, nam, uni).arrange(DOWN, buff=0.4)
        self.text_group.scale_to_fit_width(config.frame_width - 3)

        if self.decorator_presence == "box":
            self.box = SurroundingRectangle(
                self.text_group,
                corner_radius=self.corner_rad,
                buff=self.tightness,
                stroke_width=self.decorator_stroke_width,
                color=self.decorator_color,
                fill_opacity=self.fill_opa,
                stroke_opacity=self.stroke_opa,
            )
            self.add(self.text_group, self.box)

        if self.decorator_presence == "box_long_right":
            self.box_long = RoundedRectangle(
                height=self.text_group.get_height() + self.tightness,
                width=self.text_group.get_width() + 5,
                stroke_width=self.decorator_stroke_width,
                color=self.decorator_color,
                fill_opacity=self.fill_opa,
                corner_radius=self.corner_rad,
                stroke_opacity=self.stroke_opa,
            )
            self.box_long.next_to(
                self.text_group.get_left(),
                RIGHT,
                aligned_edge=LEFT,
                buff=-self.tightness,
            )
            self.text_group.move_to([0, 0, 0])
            t_sec = VGroup(self.text_group, self.box_long)
            self.add(t_sec)

        if self.decorator_presence == "box_long_left":
            self.box_long = RoundedRectangle(
                height=self.text_group.get_height() + self.tightness,
                width=self.text_group.get_width() + 5,
                stroke_width=self.decorator_stroke_width,
                color=self.decorator_color,
                fill_opacity=self.fill_opa,
                corner_radius=self.corner_rad,
                stroke_opacity=self.stroke_opa,
            )
            self.box_long.flip()
            self.box_long.next_to(
                self.text_group.get_right(),
                LEFT,
                aligned_edge=RIGHT,
                buff=-self.tightness,
            )
            self.text_group.move_to([0, 0, 0])
            t_sec = VGroup(self.text_group, self.box_long)
            self.add(t_sec)

        if self.decorator_presence == "back_frame":
            self.rectangle = Rectangle(
                height=self.text_group.get_height() + self.tightness,
                width=config.frame_width + 0.1,
                stroke_width=self.decorator_stroke_width,
                color=self.decorator_color,
                fill_opacity=self.fill_opa,
                stroke_opacity=self.stroke_opa,
            )
            self.add(self.text_group, self.rectangle)

        else:
            self.add(self.text_group)
