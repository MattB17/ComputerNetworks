import pytest
from Networking.Base import exceptions as exc


def test_invalid_proportion():
    with pytest.raises(exc.InvalidProportion) as prop_exc:
        raise exc.InvalidProportion(1.2)
    assert (str(prop_exc.value) == "1.2 is not a valid proportion. Please "
                                   "specify a number in the range [0, 1].")
