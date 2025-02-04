from ..my_imports import *
from .text_general import *

__all__ = ["BlB"]


class BlB(Text_General, Group):
    """Class to create a bulleted list.

    .. note::

        You can find an example in Text_General class.

    - **Methods**::
    """

    def __init__(self, list_input, **kwargs) -> VGroup:
        super().__init__(**kwargs)

        # Geometry
        self.order_list = BulletedList(
            *list_input,
            font_size=1.2 * self.text_size,
            buff=self.tightness,
            stroke_color=self.text_color,
            dot_scale_factor=self.dot_scale,
        )
        self.order_list.set_color(self.text_color)
        self.count = 0

        if self.decorator_presence == "box":
            self.box = SurroundingRectangle(
                self.order_list,
                corner_radius=self.corner_rad,
                buff=self.tightness,
                stroke_width=self.decorator_stroke_width,
                color=self.decorator_color,
                fill_opacity=self.fill_opa,
                stroke_opacity=self.stroke_opa,
            )
            self.add(self.order_list, self.box)

        else:
            self.add(self.order_list)

    def next_point(self, rf: float = linear, rt: float = 1) -> Succession:
        """Method to iterate over each of the points of the bullets points. For each iteration, makes the n-th bullet point completely black and greys out the rest.

        Args::

            - rf (float, optional): rate_function of the animation. Defaults to linear.
            - rt (float, optional): run_time of the animation. Defaults to 1.

        """
        if self.count == 0:
            self.count += 1

            return Succession(
                self.order_list[1:].animate(run_time=rt, rate_func=rf).set_opacity(0.2)
            )

        if 0 < self.count < len(self.order_list):
            self.count += 1
            return Succession(
                self.order_list.animate(run_time=rt, rate_func=rf).set_opacity(0.2),
                self.order_list[self.count - 1]
                .animate(run_time=rt, rate_func=rf)
                .set_opacity(1),
            )
        if self.count == len(self.order_list):
            self.count += 1
            return Succession(
                self.order_list.animate(run_time=rt, rate_func=rf).set_opacity(1)
            )

        else:
            return Wait()
