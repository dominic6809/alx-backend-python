# 0x00-python_variable_annotations

## Overview

This project focuses on using type annotations in Python 3, emphasizing how to specify function signatures, variable types, and leveraging duck typing. It also includes code validation using `mypy` for type checking.

## Learning Objectives

- Understand type annotations in Python 3.
- Specify function signatures and variable types.
- Utilize duck typing in Python.
- Validate code with `mypy`.

## Project Structure

The project consists of multiple Python files, each demonstrating different aspects of type annotations:

1. **0-add.py**: Function `add` that adds two floats.
2. **1-concat.py**: Function `concat` that concatenates two strings.
3. **2-floor.py**: Function `floor` that returns the floor of a float.
4. **3-to_str.py**: Function `to_str` that converts a float to a string.
5. **4-define_variables.py**: Variables defined with specific types.
6. **5-sum_list.py**: Function `sum_list` that sums a list of floats.
7. **6-sum_mixed_list.py**: Function `sum_mixed_list` that sums a mixed list of integers and floats.
8. **7-to_kv.py**: Function `to_kv` that returns a tuple with a string and the square of a number.
9. **8-make_multiplier.py**: Function `make_multiplier` that returns a multiplier function.
10. **9-element_length.py**: Function `element_length` that returns lengths of elements in a sequence.
11. **100-safe_first_element.py**: Function `safe_first_element` with duck typing annotations.
12. **101-safely_get_value.py**: Function `safely_get_value` using `TypeVar` for flexible typing.
13. **102-type_checking.py**: Function `zoom_array` for zooming into an array, demonstrating type annotations.

## Usage

To run the scripts, use the following command:

```bash
chmod +x <script_name>.py
./<script_name>.py
