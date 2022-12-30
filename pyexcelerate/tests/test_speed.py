from .benchmark import (
    run_pyexcelerate_value_fastest,
    run_xlsxwriter_value,
    run_openpyxl,
)
from nose.tools import ok_
import nose


def test_vs_xlsxwriter():
    raise nose.SkipTest("Skipping speed test")
