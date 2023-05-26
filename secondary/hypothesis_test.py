# import pytest
import unittest

import pytest
from hypothesis import strategies as st, given
from hypothesis_jsonschema import from_schema


from jsonschema.exceptions import ValidationError
from jsonschema.validators import validate

schema = {"category": {"type": "string"}}


def is_valid(json_data):
    try:
        validate(instance=json_data, schema=schema)
    except ValidationError:
        return False
    return True


@given(data=from_schema(schema))
def test_json(data):
    assert is_valid(data)


if __name__ == "__main__":
    pytest.main()
