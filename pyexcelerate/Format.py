from . import Utility
import six


class Format(object):
    __slots__ = ("_id", "format")

    def __init__(self, format=None):
        self._id = 0  # autopopulated by workbook.py
        self.format = format

    def __eq__(self, other):
        return self.is_default if other is None else self.format == other.format

    def __or__(self, other):
        return Format(format=Utility.nonboolean_or(self.format, other.format, None))

    def __and__(self, other):
        return Format(format=Utility.nonboolean_and(self.format, other.format, None))

    def __xor__(self, other):
        return Format(format=Utility.nonboolean_xor(self.format, other.format, None))

    def __hash__(self):
        return hash(self.format)

    @property
    def is_default(self):
        return self == Format()

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value + 1000

    def get_xml_string(self):
        return '<numFmt numFmtId="%d" formatCode="%s"/>' % (self.id, self.format)

    def __str__(self):
        return f"Format: {self.format}"
