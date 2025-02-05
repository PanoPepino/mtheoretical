from ..my_imports import *

__all__ = ["Plot_General"]


class Plot_General(Group):
    """This class is a general class to control the apareance of all other plots through the inheritance property.

    - **Parameters**::

            - func_main_color (ParsableManimColor, optional): Defaults to GREEN.
            - func_2_color (ParsableManimColor, optional): Defaults to RED.
            - func_3_color (ParsableManimColor, optional): Defaults to BLUE.
            - text_color (ParsableManimColor, optional): Defaults to WHITE.
            - axis_opacity (float, optional): Defaults to 0.5.
            - axis_stroke (float, optional): Defaults to 1.
            - decorator_presence (str, optional): Several options:
                - "box": A simple surrounding rectangle around the title.
                - "no": Nothing. Plain text.
            - decorator_color (ParsableManimColor, optional): Defaults to WHITE.
            - decorator_stroke_w: (float, optional). Defaults to 1.
            - corner_rad (float, optional): Defaults to 0.
            - corner_rad_direction (list, optional): Defaults to [0, 0, 0, 0].
            - fill_opa (float, optional): Defaults to 0.1.
            - stroke_w (float, optional): Defaults to 1.
            - stroke_opa (float, optional): Defaults to 1.
            - tightness (float, optional): Defaults to 0.3.

    .. note::

        Scale any graph with respect to the center scale(3, about_point=graph.ax_ins.c2p(0, 0, 0))

    """

    def __init__(
        self,
        func_main_color: ParsableManimColor = GREEN,
        func_2_color: ParsableManimColor = RED,
        func_3_color: ParsableManimColor = BLUE,
        text_color: ParsableManimColor = WHITE,
        axis_opacity: float = 0.5,
        axis_stroke: float = 1,
        decorator_presence: str = "box",
        decorator_color: ParsableManimColor = WHITE,
        decorator_stroke_w: float = 1,
        corner_rad: float = 0,
        corner_rad_direction: list = [0, 0, 0, 0],
        fill_opa: float = 0.1,
        stroke_w: float = 1,
        stroke_opa: float = 1,
        tightness: float = 0.3,
        **kwargs,
    ):
        super().__init__(**kwargs)
        self.func_main_color = func_main_color
        self.func_2_color = func_2_color
        self.func_3_color = func_3_color
        self.text_color = text_color
        self.axis_opacity = axis_opacity
        self.axis_stroke = axis_stroke
        self.decorator_presence = decorator_presence
        self.decorator_color = decorator_color
        self.decorator_stroke_w = decorator_stroke_w
        self.corner_rad = list(corner_rad * np.array(corner_rad_direction))
        self.fill_opa = fill_opa
        self.stroke_w = stroke_w
        self.stroke_opa = stroke_opa
        self.tightness = tightness
