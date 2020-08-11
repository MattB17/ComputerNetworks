import io
import sys
import pytest
from unittest.mock import MagicMock, patch, call
from Networking.WebServer.WebServer import WebServer
from socket import AF_INET, SOCK_STREAM


SOCKET_STR = "Networking.WebServer.WebServer.socket.socket"
RENDER_STR = "Networking.WebServer.utils.render_page"


@pytest.fixture(scope="function")
def mock_server_socket():
    server_socket = MagicMock()
    server_socket.bind = MagicMock(side_effect=None)
    server_socket.listen = MagicMock(side_effect=None)
    server_socket.close = MagicMock(side_effect=None)
    return server_socket


@pytest.fixture(scope="function")
def web_server(mock_server_socket):
    with patch(SOCKET_STR, return_value=mock_server_socket) as mock_socket:
        server = WebServer('127.0.0.1', 8000)
    mock_socket.assert_called_once_with(AF_INET, SOCK_STREAM)
    mock_server_socket.bind.assert_called_once_with(('127.0.0.1', 8000))
    mock_server_socket.listen.assert_called_once_with(1)
    return server


def test_instantiation(web_server):
    assert web_server.get_host() == '127.0.0.1'
    assert web_server.get_port() == 8000
    assert not web_server.is_running()


def test_is_running_gives_true(web_server):
    web_server.running = True
    assert web_server.is_running()


@patch(RENDER_STR, side_effect=None)
def test_run_once(mock_render, web_server, mock_server_socket):
    web_server.is_running = MagicMock(side_effect=(True, False))
    mock_conn = MagicMock()
    mock_addr = MagicMock()
    mock_server_socket.accept = MagicMock(return_value=(mock_conn, mock_addr))
    captured_prints = io.StringIO()
    sys.stdout = captured_prints
    web_server.run()
    sys.stdout = sys.__stdout__
    mock_server_socket.accept.assert_called_once()
    mock_render.assert_called_once_with(mock_conn)
    assert captured_prints.getvalue() == "Ready to serve ...\n"


@patch(RENDER_STR, side_effect=None)
def test_run_multiple(mock_render, web_server, mock_server_socket):
    web_server.is_running = MagicMock(side_effect=(True, True, True, False))
    conns = [MagicMock() for _ in range(3)]
    addrs = [MagicMock() for _ in range(3)]
    mock_server_socket.accept = MagicMock(
        side_effect=tuple((conns[i], addrs[i]) for i in range(3)))
    captured_prints = io.StringIO()
    sys.stdout = captured_prints
    web_server.run()
    sys.stdout = sys.__stdout__
    assert mock_server_socket.accept.call_count == 3
    render_calls = [call(conn) for conn in conns]
    assert mock_render.call_count == 3
    mock_render.assert_has_calls(render_calls)
    assert (captured_prints.getvalue() ==
        "Ready to serve ...\nReady to serve ...\nReady to serve ...\n")


def test_close(web_server, mock_server_socket):
    web_server.close()
    mock_server_socket.close.assert_called_once()
