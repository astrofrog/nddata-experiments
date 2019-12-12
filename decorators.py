from functools import wraps
import inspect
import numpy as np


def view_as_nddata(expected_type):
    def decorator(func):
        @wraps(func)
        def func_wrapper(*args, **kwargs):
            # Introspect the function arguments
            # fargs = inspect.getfullargspec(func)

            # Get the expected data argument
            input_data = args[0]

            new_input_data = expected_type.__from_nddata__(input_data)

            output_data = func(new_input_data, *args[1:], **kwargs)

            new_output_data = input_data.__from_nddata__(output_data, input_data)

            return new_output_data
        return func_wrapper
    return decorator