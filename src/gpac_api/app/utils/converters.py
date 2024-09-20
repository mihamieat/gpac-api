# -*- coding: utf-8 -*-
"""converter modules."""

from bson import ObjectId
from fastapi import HTTPException


def convert_object_ids(data):
    """
    Recursively converts ObjectId instances in a data structure to their string representations.

    Args:
        data: The input data structure, which can be a dictionary, \
list, ObjectId, or any other type.

    Returns:
        The modified data structure with ObjectId instances converted to strings,
        while leaving other data unchanged.

    Raises:
        None
    """
    conversion_map = {
        dict: lambda dct: {k: convert_object_ids(v) for k, v in dct.items()},
        list: lambda lst: [convert_object_ids(i) for i in lst],
        ObjectId: str,
    }

    return conversion_map.get(type(data), lambda x: x)(data)


def str_to_object_id(string: str) -> ObjectId:
    """
    Converts a string representation of an ObjectId to an ObjectId instance.

    Args:
        string (str): The string representation of the ObjectId to be converted.

    Returns:
        ObjectId: The ObjectId instance corresponding to the provided string.

    Raises:
        None
    """
    return ObjectId(string)


def validate_object_ids(id_string: str):
    """Validate and convert a string to an object ID.

    Args:
        id_string (str): The string representation of the ID to be validated.

    Returns:
        str: The converted object ID as a string.

    Raises:
        HTTPException: If the provided id_string is not in a valid format.
    """
    try:
        return str_to_object_id(id_string)
    except Exception as e:
        raise HTTPException(
            status_code=400, detail="Invalid notification ID format"
        ) from e
