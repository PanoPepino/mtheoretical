from os import path

from ..my_imports import *
from .brane_general import *
from .vacuum_general import *

__all__ = ["Bubble"]


class Bubble(Brane_General, Vacuum_General, Group):
    """Class to represent Dark Bubble discussions in 2 dimensions. See Brane and Vacuum General for further information.

    - **Parameters**::

        - bubble_type (str, optional): Choose the type of bubble to represent.
        Defaults to empty.
            - empty: Regular inside/outside with both AdS scales.
            - instanton: Same as before, but AdS scales are replaced by potentials.
            - radiation: Add mass to the inside vacuum.
            - strings: Add radially stretching strings to the bulk.
            - GW: Add gravitational waves to the bulk.
            - em: Add background B-field to bulk and on the brane.
            - energy_discussion: An "energy bar" appears below the box, to discuss
            energy conservation.
        - box_height (float, optional):Height of vacuum. Defaults to 6.
        - box_width (float, optional): Length of vacuum. Defaults to 8.
        - string_color (ParsableManimColor, optional): Colors of strings. Defaults to BLUE.
        - string_stroke_w (float, optional): Defaults to 1.5.
        - field_gradient (float, optional): Represents how good the gradient of the source
        field ON the brane is. Defaults to 50.
        - field_top_color (ParsableManimColor, optional): Color of field on top of the brane.
        Defaults to BLUE.
        - field_bulk_color (ParsableManimColor, optional): (To be constructed).
        Defaults to PINK.

    .. note::

        The bubble is always the 2nd entry of the class.

    .. attention::

        The "em" mode lacks the representation of the B-field in the bulk

    - **Examples**::

        from manim  import *
        from beanim import *

        class Example_Bubble(Scene):
            def construct(self):
                bubble_types= ["empty", "radiation", "em", "strings", "GW"]
                bubble_group= Group(*[Bubble(bubble_type= style).scale(0.4) for style in bubble_types])
                bubble_group.arrange_in_grid(2,3)

                self.play(AnimationGroup(map(lambda x: x.fade_in_bulk(), bubble_group)))
                self.play(AnimationGroup(map(lambda x: x.create_bubble(), bubble_group)))
                self.play(AnimationGroup(map(lambda x: x.expand_bubble(), bubble_group)))

        class Example_Energy_Discussion(Scene):
            def construct(self):
                bub= Bubble(bubble_type= "energy_discussion").scale(0.8)
                self.play(bub.fade_in_bulk())
                self.play(bub.fail_creation())
                self.play(bub.create_bubble())
                self.play(bub.expand_bubble())
                self.play(FadeOut(bub))

    - **Methods**::

    """

    def __init__(
        self,
        bubble_type: str = "empty",
        box_height: float = 6,
        box_width: float = 8,
        string_color: ParsableManimColor = BLUE,
        string_stroke_w: float = 1.5,
        field_gradient: float = 50,
        field_top_color: ParsableManimColor = BLUE,
        field_bulk_color: ParsableManimColor = PINK,
        **kwargs,
    ):
        super().__init__(**kwargs)

        # It seems I have to do this to define properties inside animation functions
        self.bubble_type = bubble_type

        # Geometry Bubbles
        self.background = RoundedRectangle(
            corner_radius=self.corner_rad,
            height=box_height,
            width=box_width,
            stroke_width=self.vacuum_stroke_w,
            color=self.vacuum_color,
            fill_opacity=self.vacuum_fill_opa,
        )
        self.brane = Circle(
            radius=self.brane_radius,
            color=self.brane_color,
            fill_opacity=1.5 * self.brane_fill_opa,
            stroke_width=self.brane_stroke_w,
        )

        # Text
        self.in_text = (
            MathTex("k_{-}", font_size=35, color=self.vacuum_text_color)
            .move_to(self.background.get_center())
            .set_z_index(4)
        )
        self.out_text = (
            MathTex("k_{+}", font_size=35, color=self.vacuum_text_color)
            .move_to(self.background.get_corner(UR) - [0.45, 0.45, 0])
            .set_z_index(4)
        )

        self.in_insta_text = (
            MathTex("V(\\phi_{-})", font_size=35, color=self.vacuum_text_color)
            .move_to(self.background.get_center())
            .set_z_index(4)
        )
        self.out_insta_text = (
            MathTex("V(\\phi_{+})", font_size=35, color=self.vacuum_text_color)
            .move_to(self.background.get_corner(UR) - [0.55, 0.55, 0])
            .set_z_index(4)
        )
        self.radius_line = Line(
            start=self.brane.get_center(),
            end=2.5 * self.brane.point_at_angle(PI / 4),
            color=self.vacuum_text_color,
            stroke_width=self.brane_stroke_w,
        )
        self.radius_text = (
            MathTex("r=a(\\tau)", font_size=30, color=self.vacuum_text_color)
            .rotate(PI / 4)
            .next_to(self.radius_line.get_center(), LEFT, buff=0.05)
        )
        self.radius_info = VGroup(self.radius_line, self.radius_text)

        # matter
        get_mass_path = path.join(path.dirname(__file__), "../figures/weight.svg")
        self.mass = SVGMobject(get_mass_path).scale(0.5)

        # strings
        self.strings = VGroup()
        box_positions = [RIGHT, UR, UP, UL, LEFT, DL, DOWN, DR]
        dots = VGroup(
            *[
                Dot(
                    radius=0,
                    fill_opacity=0,
                    point=self.brane.point_at_angle(i * 360 / 8 * DEGREES),
                )
                for i in range(len(box_positions))
            ]
        )
        self.brane_w_anchor = VGroup(dots, self.brane)

        # This simple list is more elegant. Impressive that for the iteration to work, one needs to "rewrite" initial and final positions.
        for angle, position in zip(dots, box_positions):
            if (
                np.linalg.norm(position) > 1
            ):  # To avoid strange position if corner radius is big.
                string = always_redraw(
                    lambda angle=angle, position=position: Line(
                        start=angle,
                        end=self.background.get_corner(position)
                        - self.cr / 6 * position,
                        stroke_width=string_stroke_w,
                        stroke_color=string_color,
                    )
                )
                self.strings.add(string)
            else:
                string = always_redraw(
                    lambda angle=angle, position=position: Line(
                        start=angle,
                        end=self.background.get_corner(position),
                        stroke_width=string_stroke_w,
                        stroke_color=string_color,
                    )
                )
                self.strings.add(string)

        # Grav. Waves
        def func_waves(t):
            return (
                (self.brane_radius + 0.01 * np.sin(25 * t)) * np.cos(t),
                (self.brane_radius + 0.01 * np.sin(25 * t)) * np.sin(t),
                0,
            )

        self.brane_waves = ParametricFunction(
            func_waves,
            t_range=(0, 2 * TAU),
            stroke_width=self.brane_stroke_w,
            fill_opacity=self.brane_fill_opa,
        ).set_color(self.brane_color)
        self.waves = ParametricFunction(
            func_waves,
            t_range=(0, 2 * TAU),
            stroke_width=self.brane_stroke_w / 3,
            fill_opacity=0,
        ).set_color(self.brane_color)

        # Extra Fields
        # Electromagnetism (Note 5% extra radius)
        def field(
            grad,
            mobject,
            rad=self.brane_radius + 0.6,
            inner_rad=1.05 * self.brane_radius,
            col=field_top_color,
        ):
            glow_group = VGroup()
            for idx in range(grad):
                new_circle = Annulus(
                    inner_radius=inner_rad,
                    outer_radius=inner_rad + idx / grad * (rad - inner_rad),
                    stroke_opacity=0,
                    fill_color=col,
                    fill_opacity=0.75 / grad,
                ).move_to(mobject)
                glow_group.add(new_circle)
            return glow_group

        self.field_glow = field(field_gradient, self.brane)
        self.field_top = Circle(
            radius=1.05 * self.brane_radius,
            color=field_top_color,
            fill_opacity=0,
            stroke_width=4,
        )

        # Energy Discussion
        self.vacuum_tracker = ValueTracker(0.8)
        self.bar_outside = RoundedRectangle(
            corner_radius=self.corner_rad,
            height=0.6,
            width=box_width,
            stroke_width=self.vacuum_stroke_w + 0.2,
            color=self.brane_color,
            fill_opacity=0,
        )
        self.bar_outside.next_to(self.background, DOWN, buff=0.2)
        self.energy_gain = always_redraw(
            lambda: RoundedRectangle(
                corner_radius=self.corner_rad,
                height=0.5,
                width=self.vacuum_tracker.get_value(),
                stroke_width=0.1,
                fill_opacity=self.brane_fill_opa,
            )
            .next_to(self.bar_outside.get_left(), aligned_edge=LEFT, buff=0)
            .set_color(self.bar_outside.get_color())
        )
        self.energy_cost_bubble = DashedVMobject(
            Circle(
                radius=self.brane_radius,
                color=self.brane_color,
                fill_opacity=0,
                stroke_width=self.vacuum_stroke_w + 0.9,
            )
        )

        # Note that position of the brane is always [2] in the bubble_group.
        if bubble_type == "empty":
            self.bubble = VGroup(
                self.background,
                self.out_text,
                self.brane,
                self.in_text,
                self.radius_info,
            )
            self.add(self.bubble)

        if bubble_type == "instanton":
            self.bubble = VGroup(
                self.background, self.out_insta_text, self.brane, self.in_insta_text
            )
            self.add(self.bubble)

        if bubble_type == "radiation":
            self.in_text.next_to(self.mass, DOWN, buff=0.2)
            self.bubble = VGroup(
                self.background, self.out_text, self.brane, self.in_text, self.mass
            )
            self.add(self.bubble)

        if bubble_type == "GW":
            self.bubble = VGroup(
                self.background, self.out_text, self.brane_waves, self.in_text
            )
            self.add(self.bubble)

        if bubble_type == "strings":
            self.out_text.shift(0.3 * DOWN)
            self.bubble = VGroup(
                self.background,
                self.out_text,
                self.brane_w_anchor,
                self.strings,
                self.in_text,
            )
            self.add(self.bubble)

        if bubble_type == "em":
            self.bubble = VGroup(
                self.background,
                self.out_text,
                self.brane,
                self.in_text,
                self.field_top,
                self.field_glow,
            )
            self.add(self.bubble)

        if bubble_type == "energy_discussion":
            self.fake_brane = self.brane.copy()
            self.bubble = VGroup(
                self.background,
                self.out_text,
                self.fake_brane,
                self.brane,
                self.energy_cost_bubble,
            )
            self.add(self.bubble, self.bar_outside, self.in_text, self.energy_gain)

    # Methods
    def fade_in_bulk(
        self, rt: float = 1, rf: float = linear
    ) -> Animation:  # The arrow associates this method with a class animation.
        """
        
        Args::

            - rt (float, optional): run_time animation. Defaults to 1.
            - rf (float, optional): rate function. Defaults to linear.

        Returns::
            
            - Animation: Returns the creation of the bulk box and the value of the cosmological constant outside.
        """
        if self.bubble_type == "energy_discussion":
            return Succession(
                FadeIn(self.bubble[:2], run_time=rt, rate_func=rf),
                FadeIn(self.bubble[-1], run_time=rt, rate_func=rf),
                Create(
                    VGroup(self.bar_outside, self.energy_gain),
                    run_time=rt,
                    rate_func=rf,
                ),
            )

        else:
            return FadeIn(self.bubble[:2], run_time=rt, rate_func=rf)

    def fail_creation(
        self, rt: float = 3, rf: float = there_and_back_with_pause
    ) -> AnimationGroup:
        """.. note::

            This method only works with energy_discussion.

        Args::

            - rt (float, optional): Defaults to 2.
            - rf (float, optional): Defaults to linear.

        Returns::

            - Animation: The creation of the bubble fails due to lack of energy.
        """
        return AnimationGroup(
            self.vacuum_tracker.animate(run_time=rt, rate_func=rf).set_value(2),
            GrowFromCenter(self.bubble[2].scale(0.8), run_time=rt, rate_func=rf),
        )

    def create_bubble(
        self, rt: float = 0.2, rf: float = linear
    ) -> Succession:  # The arrow associates this method with a class succession.
        """Args::

            - rt (float, optional): run_time animation. Defaults to 1.
            - rf (float, optioanl): rate function. Defaults to linear.

        Returns::

            - Animation: Shows the creation of the bubble and its inside value of the scale curvature.
        """
        if self.bubble_type == "energy_discussion":
            return Succession(
                self.vacuum_tracker.animate(run_time=5 * rt, rate_func=rf).set_value(
                    2.5
                ),
                GrowFromCenter(self.bubble[3], run_time=5 * rt, rate_func=rf),
                self.energy_cost_bubble.animate.set_opacity(0),
            )

        if self.bubble_type == "em":
            return Succession(
                GrowFromCenter(self.bubble[2], run_time=rt, rate_func=rf),
                FadeIn(self.bubble[3:-2], run_time=rt, rate_function=rt),
                Create(self.field_top, run_time=rt, rate_function=rf),
                Wait(),
                Create(self.field_glow, run_time=2 * rt, rate_func=rf),
            )

        if self.bubble_type == "strings":
            return Succession(
                GrowFromCenter(self.bubble[2], run_time=rt, rate_func=rf),
                Create(self.strings, run_time=rt, rate_func=rf),
                FadeIn(self.bubble[-1], run_time=rt, rate_function=rt),
            )

        if self.bubble_type == "radiation":
            return Succession(
                GrowFromCenter(self.bubble[2], run_time=rt, rate_func=rf),
                FadeIn(self.bubble[3:], run_time=rt, rate_function=rt),
            )

        else:
            return Succession(
                GrowFromCenter(self.bubble[2], run_time=rt, rate_func=rf),
                FadeIn(self.bubble[3:-1], run_time=rt, rate_function=rt),
            )

    def expand_bubble(
        self, rt: float = 6, rf: float = linear, sca: float = 2.5
    ) -> AnimationGroup:  # The arrow associates this method with a class animation.
        """Args::

            - rt (float, optional): run_time animation. Defaults to 6.
            - rf (float, optional): rate function. Defaults to linear.
            - sca (float, optional): size for the scaling of the brane.

        Returns::

            - Animation: Returns the expansion of the bubble. Denpeding on the type of bubble,
            it automatically shows the evolution of energy densities in the bulk.
        """
        if self.bubble_type == "energy_discussion":
            return Succession(
                self.vacuum_tracker.animate(run_time=rt / 3, rate_func=rf).set_value(
                    4.5
                ),
                self.bubble[3].animate(run_time=rt, rate_func=rf).scale(sca),
            )

        if self.bubble_type == "GW":
            return AnimationGroup(
                self.brane_waves.animate(run_time=rt, rate_func=rf).scale(sca),
                Broadcast(
                    self.waves.scale(0.6 * sca),
                    focal_point=self.bubble[2].get_center(),
                    initial_opacity=1,
                    final_opacity=0,
                    n_mobs=15,
                    run_time=rt,
                    rate_func=rf,
                ),
            )

        if self.bubble_type == "em":
            return AnimationGroup(
                self.brane.animate(run_time=rt, rate_func=rf).scale(0.8 * sca),
                self.bubble[-2:].animate(run_time=rt, rate_func=rf).scale(0.8 * sca),
            )

        if self.bubble_type == "strings":
            return AnimationGroup(
                self.brane_w_anchor.animate(run_time=rt, rate_func=rf).scale(sca)
            )

        else:
            return AnimationGroup(
                self.brane.animate(run_time=rt, rate_func=rf).scale(sca)
            )

    def show_radius(self, rt: float = 1, rf: float = linear) -> Succession:
        """Args::

            - rt (float, optional): run_time animation. Defaults to 1.
            - rf (float, optional): rate function. Defaults to linear.

        Returns::

            - Succession: Shows the time dependence of the radius of the bubble.
        """
        return Succession(
            self.in_text.animate.next_to(self.brane.get_center(), DOWN, buff=0.2),
            Create(self.radius_info, run_time=rt, rate_function=rf),
        )
