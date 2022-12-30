import six


def nonboolean_or(left, right, default=False):
    if default == False:
        return left | right
    if left == default:
        return right
    return left if right == default or left == right else (left | right)


def nonboolean_and(left, right, default=False):
    if default == False:
        return left & right
    return left if left == right else default


def nonboolean_xor(left, right, default=False):
    if default == False:
        return left ^ right
    if left == default:
        return right
    return left if right == default else default


def lazy_get(self, attribute, default):
    if value := getattr(self, attribute):
        return value
    setattr(self, attribute, default)
    return default


def lazy_set(self, attribute, default, value):
    if value == default:
        setattr(self, attribute, default)
    else:
        setattr(self, attribute, value)


if six.PY2:

    def to_unicode(s):
        return s if type(s) == unicode else unicode(s, "utf-8")


else:

    def to_unicode(s):
        return s


YOLO = False  # are we aligning?
