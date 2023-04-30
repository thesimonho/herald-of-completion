"""Helper functions used throughout the package."""

from typing import TypeVar, Union

T = TypeVar("T")


def truncate(input: T, length: int) -> Union[T, str]:
    """Truncate an input value to custom typed representation.

    Args:
        input: Value to be truncated. Can be of any type.
        length: Length to truncate the value to.

    Returns:
        Truncated representation of the input.
    """
    if isinstance(input, bool) or isinstance(input, type(None)):
        return input

    input_type = type(input).__name__
    try:
        input_clean = str(input).strip().replace("\n", " ")
    except Exception:
        return input_type

    if len(input_clean) > length:
        half_len = length // 2
        start = input_clean[:half_len]
        end = input_clean[-half_len:]
        output = f"{start}..<{input_type}>..{end}"
    else:
        output = input

    return output


def build_arg_string(args: tuple, truncate_length: int = 10) -> str:
    """Create string representation of an args tuple.

    Args:
        args: Tuple of arguments to be converted to a string.
        truncate_length: Length to truncate the string to.

    Returns:
        String representation of the args.
    """
    result = ""
    for arg in args:
        truncated = truncate(arg, truncate_length)
        if isinstance(arg, str):
            result += f"'{truncated}', "
        else:
            result += f"{truncated}, "
    result = result[:-2]  # remove last comma
    return result


def build_kwarg_string(kwargs: dict, truncate_length: int = 10) -> str:
    """Create string representation of a kwargs dict.

    Args:
        kwargs: Dictionary of keyword arguments to be converted to a string.
        truncate_length: Length to truncate the string to.

    Returns:
        String representation of the kwargs dict.
    """
    result = ""
    for key, value in kwargs.items():
        truncated = truncate(value, truncate_length)
        if isinstance(value, str):
            result += f"{key}='{truncated}', "
        else:
            result += f"{key}={truncated}, "
    result = result[:-2]  # remove last comma
    return result
