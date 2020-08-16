from unittest.mock import patch
from Networking.UDPPinger.utils import process_message


PONG_STR = "Networking.UDPPinger.utils.create_pong"


@patch(PONG_STR, return_value=["PONG"])
def test_with_empty_message(mock_pong):
    assert process_message("") == "PONG"
    mock_pong.assert_called_once_with([])


@patch(PONG_STR, return_value=["PONG"])
def test_with_one_word_message(mock_pong):
    assert process_message("ping") == "PONG"
    mock_pong.assert_called_once_with(["PING"])


@patch(PONG_STR, return_value=["PONG", "A", "MESSAGE"])
def test_with_multi_word_message(mock_pong):
    assert process_message("Ping a MESSAGE") == "PONG A MESSAGE"
    mock_pong.assert_called_once_with(["PING", "A", "MESSAGE"])
