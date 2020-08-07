from unittest.mock import patch, mock_open
from Networking.WebServer.utils import read_message


OPEN_STR = "builtins.open"


def test_with_empty_file():
    message = "http://some/url /some_page.html"
    with patch(OPEN_STR, mock_open(read_data="")) as mock_file:
        assert read_message(message) == []
    mock_file.assert_called_once_with("some_page.html", "r")


def test_with_one_line_file():
    message = "http://a/second/url /another_page.html"
    with patch(OPEN_STR, mock_open(read_data="data\n")) as mock_file:
        assert read_message(message) == ["data\n"]
    mock_file.assert_called_once_with("another_page.html", "r")


def test_with_multi_line_file():
    message = "http://another/url /a_long_page.html"
    data = "line1\nline2\nline3\n"
    with patch(OPEN_STR, mock_open(read_data=data)) as mock_file:
        assert read_message(message) == ["line1\n", "line2\n", "line3\n"]
    mock_file.assert_called_once_with("a_long_page.html", "r")
