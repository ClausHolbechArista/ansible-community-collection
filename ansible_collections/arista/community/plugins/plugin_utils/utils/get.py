# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import Any


def get(
    dictionary: dict,
    key: str,
    default: Any = None,
    required: bool = False,
    org_key: str | None = None,
    separator: str = ".",
    custom_error_msg: str | None = None,
) -> Any:
    """
    Get a value from a dictionary or nested dictionaries.

    Key supports dot-notation like "foo.bar" to do deeper lookups.
    Returns the supplied default value or None if the key is not found and required is False.

    Parameters
    ----------
    dictionary : dict
        Dictionary to get key from
    key : str
        Dictionary Key - supporting dot-notation for nested dictionaries
    default : any
        Default value returned if the key is not found
    required : bool
        Fail if the key is not found
    org_key : str
        Internal variable used for raising exception with the full key name even when called recursively
    separator: str
        String to use as the separator parameter in the split function. Useful in cases when the key
        can contain variables with "." inside (e.g. hostnames)
    custom_error_msg: str
        Custom error message to raise when required is True and the value is not found

    Returns:
    -------
    any
        Value or default value

    Raises:
    ------
    KeyError
        If the key is not found and required == True
    """
    if org_key is None:
        org_key = key
    keys = str(key).split(separator)
    value = dictionary.get(keys[0])
    if value is None:
        if required is True:
            if custom_error_msg:
                raise KeyError(custom_error_msg)
            raise KeyError(org_key)
        return default

    if len(keys) > 1:
        return get(value, separator.join(keys[1:]), default=default, required=required, org_key=org_key, separator=separator, custom_error_msg=custom_error_msg)

    return value
