from ..my_imports import *
from .refeq_funcs import *
from .text_general import *

__all__ = ["Ref"]


class Ref(Text_General, VGroup):
    """Class to create citations of References. It has a dictionary built in. You can check it in [source].

    - Parameters::

        - the_dictionary: The path to the .txt file containing the dictionary.
        - the_ref: the key (label) of the equation you want to display.

    .. note::
        Each reference will require its own definition, as one can play with the boxes and flip them to close the design and so on. See an example in Text_General Class.

    """

    def __init__(self, the_dictionary, the_ref, **kwargs):
        super().__init__(**kwargs)

        my_path = split_dictionary_path(the_dictionary)[
            0
        ]  # Uses previous function to split the relative path
        my_file = split_dictionary_path(the_dictionary)[-1]

        if check_file_exists(my_path, my_file):  # Checks if the dictionary input exist
            open_the_dic = open(the_dictionary)
            read_the_dic = open_the_dic.read()
            load_the_dic = eval(read_the_dic)
            open_the_dic.close()

        else:  # If not, it recommends to run first the code to extract dictionaries.
            print(
                "The are two possible options for this error: \n"
                "---------------------------------------------------\n"
                "- The path you have specified is wrong. Double check.\n"
                "- The dictionary you refer to does not exist yet.\n"
                "---------------------------------------------------\n"
                'Consider running the code "extract ref from bib" in the tools subpackage\n'
                "to extract the equations in a dictionary."
            )

        self.chosen_ref = Tex(
            load_the_dic[the_ref], font_size=0.6 * self.text_size, color=self.text_color
        )

        if self.decorator_presence == "box":
            self.box = SurroundingRectangle(
                self.chosen_ref,
                corner_radius=self.corner_rad,
                buff=self.tightness,
                stroke_width=self.decorator_stroke_width,
                color=self.decorator_color,
                fill_opacity=self.fill_opa,
                stroke_opacity=self.stroke_opa,
            )
            self.add(self.chosen_ref, self.box)
        else:
            self.add(self.chosen_ref)
