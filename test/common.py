# encoding: utf-8

"""
.. codeauthor:: Tsuyoshi Hombashi <gogogo.vm@gmail.com>
"""

from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals

import sys
import traceback


def print_traceback(result):
    traceback.print_tb(result.exc_info[2], file=sys.stdout)
    print("{}\n{}\n".format(result.exc_info[0], result.exc_info[1]))
    print("[output]\n{}".format(result.output))
