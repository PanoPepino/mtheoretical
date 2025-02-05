from ..my_imports import *

__all__ = ["Brane_General"]


class Brane_General(VGroup):
    """This is a mock-up class to load all inputs for branes and associated objects.

    - **Parameters**::

        - brane_color (ParsableManimColor, optional): filling in color of the brane.
        Defaults to RED.
        - brane_fill_opa (float, optional): Recall that fill opacity will become slightly
        when we go lower in AdS scale. Defaults to 0.1.
        - brane_radius (float, optional): Initial size of brane. Defaults to 1.
        - brane_text_color (ParsableManimColor, optional): Defaults to WHITE.
        - brane_stroke_w: (float, optional). Defaults to 0.2.

    """

    def __init__(
        self,
        brane_color: ParsableManimColor = RED,
        brane_radius: float = 1,
        brane_fill_opa: float = 0.1,
        brane_stroke_w: float = 0.2,
        brane_text_color: ParsableManimColor = WHITE,
        **kwargs,
    ):
        super().__init__(**kwargs)
        self.brane_color = brane_color
        self.brane_fill_opa = brane_fill_opa
        self.brane_radius = brane_radius
        self.brane_text_color = brane_text_color
        self.brane_stroke_w = brane_stroke_w
