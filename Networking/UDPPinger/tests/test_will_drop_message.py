from unittest.mock import patch
from Networking.UDPPinger.utils import will_drop_message


RANDOM_STR = "random.randint"


@patch(RANDOM_STR, return_value=100)
def test_unreliable(mock_random):
    assert will_drop_message(0)
    mock_random.assert_called_once_with(1, 100)


@patch(RANDOM_STR, return_value=1)
def test_reliable(mock_random):
    assert not will_drop_message(1)
    mock_random.assert_called_once_with(1, 100)


@patch(RANDOM_STR, return_value=30)
def test_mostly_reliable_at_threshold(mock_random):
    assert will_drop_message(0.7)
    mock_random.assert_called_once_with(1, 100)


@patch(RANDOM_STR, return_value=20)
def test_mostly_reliable_below_threshold(mock_random):
    assert will_drop_message(0.7)
    mock_random.assert_called_once_with(1, 100)


@patch(RANDOM_STR, return_value=40)
def test_mostly_reliable_above_threshold(mock_random):
    assert not will_drop_message(0.7)
    mock_random.assert_called_once_with(1, 100)
