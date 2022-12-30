import six
from . import Utility
from . import Border


class Borders(object):
    __slots__ = ("_left", "_right", "_top", "_bottom", "id")

    def __init__(self, left=None, right=None, top=None, bottom=None):
        self._left = left
        self._right = right
        self._top = top
        self._bottom = bottom

    @property
    def left(self):
        return Utility.lazy_get(self, "_left", Border.Border())

    @left.setter
    def left(self, value):
        Utility.lazy_set(self, "_left", None, value)

    @property
    def right(self):
        return Utility.lazy_get(self, "_right", Border.Border())

    @right.setter
    def right(self, value):
        Utility.lazy_set(self, "_right", None, value)

    @property
    def top(self):
        return Utility.lazy_get(self, "_top", Border.Border())

    @top.setter
    def top(self, value):
        Utility.lazy_set(self, "_top", None, value)

    @property
    def bottom(self):
        return Utility.lazy_get(self, "_bottom", Border.Border())

    @bottom.setter
    def bottom(self, value):
        Utility.lazy_set(self, "_bottom", None, value)

    @property
    def is_default(self):
        return not (self._left or self._right or self._top or self._bottom)

    def get_xml_string(self):
        tokens = ["<border>"]
        if self._left:
            tokens.append(
                f'<left style="{self._left.style}"><color rgb="{self._left.color.hex}"/></left>'
            )
        else:
            tokens.append("<left/>")
        if self._right:
            tokens.append(
                f'<right style="{self._right.style}"><color rgb="{self._right.color.hex}"/></right>'
            )
        else:
            tokens.append("<right/>")
        if self._top:
            tokens.append(
                f'<top style="{self._top.style}"><color rgb="{self._top.color.hex}"/></top>'
            )
        else:
            tokens.append("<top/>")
        if self._bottom:
            tokens.append(
                f'<bottom style="{self._bottom.style}"><color rgb="{self._bottom.color.hex}"/></bottom>'
            )
        else:
            tokens.append("<bottom/>")
        tokens.append("</border>")
        return "".join(tokens)

    def __or__(self, other):
        return self._binary_operation(other, Utility.nonboolean_or)

    def __and__(self, other):
        return self._binary_operation(other, Utility.nonboolean_and)

    def __xor__(self, other):
        return self._binary_operation(other, Utility.nonboolean_xor)

    def _binary_operation(self, other, operation):
        return Borders(
            top=operation(self._top, other._top, None),
            left=operation(self._left, other._left, None),
            right=operation(self._right, other._right, None),
            bottom=operation(self._bottom, other._bottom, None),
        )

    def __eq__(self, other):
        if other is None:
            return self.is_default
        return (
            self._right == other._right
            and self._bottom == other._bottom
            and self._top == other._top
            and self._left == other._left
        )

    def __hash__(self):
        return hash((self._top, self._left))
