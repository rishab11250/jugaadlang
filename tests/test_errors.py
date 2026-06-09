"""
Tests for JugaadLang Funny Errors.
"""
from jugaadlang.errors.messages import format_error


def test_name_error_formatting():
    try:
        eval("non_existent_var")
    except NameError as e:
        formatted = format_error(e, "non_existent_var")
        assert "dhundte dhundte thak gaya" in formatted
        assert "non_existent_var" in formatted
        assert "mila hi nahi" in formatted
        assert "Universe collapse ho gaya" in formatted


def test_zero_division_formatting():
    try:
        1 / 0
    except ZeroDivisionError as e:
        formatted = format_error(e, "x = 1 / 0")
        assert "Zero se divide?" in formatted
        assert "Newton bhi confuse ho gaya" in formatted


def test_type_error_formatting():
    try:
        "string" + 5
    except TypeError as e:
        formatted = format_error(e, '"string" + 5')
        assert "Type mismatch ho gaya" in formatted
        assert "Galat data-type" in formatted


def test_index_error_formatting():
    try:
        [][0]
    except IndexError as e:
        formatted = format_error(e, "vals[0]")
        assert "Index out of bounds" in formatted
        assert "List ke bahar chala gaya" in formatted


def test_key_error_formatting():
    try:
        {}["key"]
    except KeyError as e:
        formatted = format_error(e, 'd["key"]')
        assert "Key gayab hai" in formatted
        assert "ye key to hai hi nahi" in formatted


def test_attribute_error_formatting():
    try:
        object().non_existent_attr
    except AttributeError as e:
        formatted = format_error(e, "obj.non_existent_attr")
        assert "Attribute mila hi nahi" in formatted
        assert "ye feature/method nahi hai" in formatted


def test_module_not_found_formatting():
    try:
        import non_existent_module
    except ModuleNotFoundError as e:
        formatted = format_error(e, "lao non_existent_module")
        assert "Module missing" in formatted
        assert "Dhundne se bhi nahi mila" in formatted
