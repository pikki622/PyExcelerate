import time
from nose.tools import *


def test_benchmark():
    TRIALS = range(1000000)

    integer = 1
    float = 3.0
    long = 293203948032948023984023948023957245

    # attempt isinstance

    stime = time.clock()
    for _ in TRIALS:
        answer = isinstance(integer, (int, float, long, complex))
        ok_(answer)
    print(f"isinstance, {time.clock() - stime}")

    # attempt __class__

    stime = time.clock()
    for _ in TRIALS:
        answer = integer.__class__ in {int, float, long, complex}
        ok_(answer)
    print(f"__class__, set, {time.clock() - stime}")

    stime = time.clock()
    answer = integer.__class__ in [int, float, long, complex]
    for _ in TRIALS:
        ok_(answer)
    print(f"__class__, or, {time.clock() - stime}")
