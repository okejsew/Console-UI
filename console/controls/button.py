from enum import Enum

from console import Control

class ButtonStyle(Enum):
    default = "[ {} ]"
    pointed = "> {} <"
    rounded = "( {} )"
    arrowed = "--> {} <--"
    angled_up = "/ {} \\"
    line = "| {} |"
    angled_down = "\\ {} /"
    right_arrow = "{} <"
    left_arrow = "> {}"
    right_dash = "{} -"
    left_dash = "- {}"
    right_boxed = "{} ]"
    right_bullet = "{} •"
    left_bullet = "• {}"

class Button(Control):
    def __init__(self):
        super().__init__()
        self.text: str = 'Button'
        self.style: ButtonStyle = ButtonStyle.default

    def __str__(self):
        return self.style.value.format(self.text)