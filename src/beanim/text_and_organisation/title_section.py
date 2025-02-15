from ..my_imports import *
from .title_general import *

__all__ = ["Title_Section"]


class Title_Section(Title_General, VGroup):
    """Class to create title for sections. Note that the title is already defined in the UL corner.

    - **Methods**::

    """

    def __init__(self, title_sec, **kwargs) -> VGroup:
        super().__init__(**kwargs)
        # text
        self.tit = Tex(title_sec, font_size=1.4 * self.text_size, color=self.text_color)

        if self.decorator_presence == "box":
            self.box = SurroundingRectangle(
                self.tit,
                color=self.decorator_color,
                corner_radius=self.corner_rad,
                buff=self.tightness,
                fill_opacity=self.fill_opa,
                stroke_width=self.decorator_stroke_width,
                stroke_opacity=self.stroke_opa,
            )
            self.t_sec = VGroup(self.tit, self.box).to_corner(UL)
            self.add(self.t_sec)

        if self.decorator_presence == "box_long_right":
            self.box_long_right = RoundedRectangle(
                height=self.tit.get_height() + self.tightness,
                width=config.frame_width + 5,
                stroke_width=self.decorator_stroke_width,
                color=self.decorator_color,
                fill_opacity=self.fill_opa,
                corner_radius=self.corner_rad,
                stroke_opacity=self.stroke_opa,
            )
            self.tit.to_corner(UL)
            self.box_long_right.next_to(
                self.tit.get_left(), RIGHT, aligned_edge=LEFT, buff=-self.tightness / 2
            )
            self.t_sec_right = VGroup(self.tit, self.box_long_right)
            self.add(self.t_sec_right)

        if self.decorator_presence == "box_long_left":
            self.box_long_left = RoundedRectangle(
                height=self.tit.get_height() + self.tightness,
                width=self.tit.get_width() + 5,
                stroke_width=self.decorator_stroke_width,
                color=self.decorator_color,
                fill_opacity=self.fill_opa,
                corner_radius=self.corner_rad,
                stroke_opacity=self.stroke_opa,
            )
            self.box_long_left.flip()
            self.tit.to_corner(UL)
            self.box_long_left.next_to(
                self.tit.get_right(), LEFT, aligned_edge=RIGHT, buff=-self.tightness
            )

            self.t_sec_left = VGroup(self.tit, self.box_long_left)
            self.add(self.t_sec_left)

        elif self.decorator_presence == "back_frame":
            self.rectangle = Rectangle(
                height=self.tit.get_height() + self.tightness,
                width=config.frame_width + 2,
                stroke_width=self.decorator_stroke_width,
                color=self.decorator_color,
                fill_opacity=self.fill_opa,
                stroke_opacity=self.stroke_opa,
            )
            self.tit.to_corner(UL)
            self.rectangle.to_corner(UP).shift(self.tightness / 2).set(z_index=-2)
            self.t_sec = VGroup(self.tit, self.rectangle)
            self.add(self.t_sec)

        else:
            self.t_sec = VGroup(self.tit)
            self.t_sec.to_corner(UL)
            self.add(self.t_sec)

    def show_title(self, rt: float = 1, rf: float = linear) -> AnimationGroup:
        """Simple animation to show the title of the slide. Depending of the decorator choice, the animation will be different.

        Args::

            - rf (float, optional): rate_function of the animation. Defaults to linear.
            - rt (float, optional): run_time of the animation. Defaults to 1.

        """
        if self.decorator_presence == "box_long_left":
            return FadeIn(
                self.t_sec_left,
                shift=5 * RIGHT,
                run_time=rt,
                rate_function=rate_functions.linear,
            )

        if self.decorator_presence == "box_long_right":
            return FadeIn(
                self.t_sec_right,
                shift=5 * LEFT,
                run_time=rt,
                rate_function=rate_functions.linear,
            )

        else:
            return Create(self.t_sec, run_time=rt, rate_function=rate_functions.linear)
