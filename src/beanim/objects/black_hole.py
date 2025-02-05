from ..my_imports import *
from .brane_general import *

__all__ = ["Black_Hole"]


class Black_Hole(Brane_General, VGroup):
    """This class creates a black hole group that can potentialy emmit a brane. See Brane General for further information.

    .. note::

       Obs! the expanding bubble will always be the [-1] element of the object.

    - **Parameters**::

        - bh_size (float, optional): Defaults to brane_radius= 1.
        - bh_color (ParsableManimColor, optional): Defaults to Black.
        - bh_fill_opa (float, optional): Defaults to 0.8.
        - bh_type:
            - "fragmentation": the written elements will be Q > T, corresponding to
            the nucleation of a brane a la AdS fragmentation by Maldacena.
            - "spinning": written elements will be theta and mu, as in the rotating black
            hole.
            - none: empty black hole. No text.

    - **Example**::

        from manim  import *
        from beanim import *

        class Example_Black_Hole(Scene):
            def construct(self):
                bh_sp= Black_Hole(bh_type= "spinning")
                bh_frag= Black_Hole(bh_type= "fragmentation")
                bh= Black_Hole()
                bh_group= VGroup(bh_sp, bh_frag, bh).arrange(RIGHT, buff= 3)
                bh_group.scale_to_fit_width(config.frame_width-1)
                self.add(bh_group)
                self.play(AnimationGroup(map(lambda x: x.nucleate(), bh_group)))
                self.play(AnimationGroup(map(lambda x: x.expand(), bh_group)))

    - **Methods**::

    """

    def __init__(
        self,
        bh_size: float = Brane_General().brane_radius,
        bh_color: ParsableManimColor = BLACK,
        bh_fill_opa: float = 0.8,
        bh_type: str = "none",
        **kwargs,
    ):
        super().__init__(**kwargs)
        self.bh_type = bh_type
        # Geometry

        bh = Circle(
            radius=bh_size,
            color=bh_color,
            fill_opacity=bh_fill_opa,
            stroke_width=self.brane_stroke_w,
        ).set_z_index(3)
        self.brane = Circle(
            radius=bh_size,
            color=self.brane_color,
            fill_opacity=self.brane_fill_opa,
            stroke_width=1,
        )
        self.theta_path = Circle(
            radius=bh_size - (bh_size * 3 / 10),
            color=WHITE,
            fill_opacity=0,
            stroke_width=0,
        )

        # Text
        qt = (
            MathTex("Q > T", font_size=35 * bh_size, color=self.brane_text_color)
            .move_to(bh.get_center())
            .set_z_index(8)
        )
        self.mu = (
            MathTex("\\mu", font_size=35 * bh_size, color=self.brane_text_color)
            .move_to(bh.get_center())
            .set_z_index(7)
        )
        self.theta = (
            MathTex("\\theta", font_size=35 * bh_size, color=self.brane_text_color)
            .move_to(self.theta_path.get_right())
            .set_z_index(7)
        )

        if self.bh_type == "spinning":
            self.add(self.brane, bh, self.mu, self.theta, self.theta_path)
        if self.bh_type == "fragmentation":
            self.add(self.brane, bh, qt)
        if self.bh_type == "none":
            self.add(self.brane, bh)

    def nucleate(
        self, rt: float = 0.5, rf: float = linear, scaling: float = 1.1
    ) -> Animation:
        """Args::

            - rt (float, optional): Run time animation. Defaults to 3.
            - rf (float, optional): Rate funciton. Defaults to linear.
            - scaling (float, optional): How much it scales. Defaults to 1.1.

        Returns::

            - Animation: Nucleation of the brane through the horizon of the black hole.
        """
        return AnimationGroup(
            self.brane.animate(run_time=rt, rate_func=rf).scale(scaling)
        )

    def expand(
        self, rt: float = 3, rf: float = linear, scaling: float = 2.5
    ) -> Animation:
        """Args::

            - rt (float, optional): Defaults to 3.
            - rf (float, optional): Defaults to linear.
            - scaling (float, optional): Defaults to 2.5.

        Returns::

            - Animation: Expansion of the brane.
        """
        if self.bh_type == "spinning":
            return AnimationGroup(
                self.brane.animate(run_time=rt, rate_func=rf).scale(scaling),
                MoveAlongPath(self.theta, self.theta_path, run_time=rt, rate_func=rf),
            )

        else:
            return AnimationGroup(
                self.brane.animate(run_time=rt, rate_func=rf).scale(scaling)
            )
