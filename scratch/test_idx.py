import traceback
import ast
import re

def test_func():
    fruits = ["🍎", "🍌", "🍇"]
    idx = 10
    return fruits[idx]

try:
    test_func()
except IndexError as e:
    tb = e.__traceback__
    while tb.tb_next:
        tb = tb.tb_next
    frame = tb.tb_frame
    print("Locals:", frame.f_locals)
