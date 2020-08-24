import pytest
from unittest.mock import MagicMock, patch, call
from Networking.UDPPinger.udp_server import UDPServer
from Networking.Base.NetworkServer import NetworkServer
from Networking.Base import exceptions as exc
from socket import AF_INET, SOCK_DGRAM


SOCKET_STR = "socket.socket"
DROP_STR = "Networking.UDPPinger.utils.will_drop_message"
PROCESS_STR = "Networking.UDPPinger.utils.process_message"
VALIDATE_STR = "Networking.UDPPinger.utils.validate_proportion"


@pytest.fixture(scope="function")
def mock_server_socket():
    server_socket = MagicMock()
    server_socket.bind = MagicMock(side_effect=None)
    server_socket.close = MagicMock(side_effect=None)
    return server_socket


@pytest.fixture(scope="function")
def mostly_reliable_server(mock_server_socket):
    with patch(SOCKET_STR, return_value=mock_server_socket), \
        patch(VALIDATE_STR, side_effect=None) as mock_validate:
        server = UDPServer('127.0.0.1', 8080, 0.7)
    mock_validate.assert_called_once_with(0.7)
    return server


def test_correct_inheritance():
    assert issubclass(UDPServer, NetworkServer)


def test_instantiation(mostly_reliable_server):
    assert mostly_reliable_server.get_host() == '127.0.0.1'
    assert mostly_reliable_server.get_port() == 8080
    assert not mostly_reliable_server.is_running()
    assert mostly_reliable_server.get_reliability() == 0.7


@patch(VALIDATE_STR, side_effect=exc.InvalidProportion(1.2))
def test_instantiation_gives_error(mock_validate):
    with pytest.raises(exc.InvalidProportion):
        UDPServer('123.45.62.111', 6259, 1.2)
    mock_validate.assert_called_once_with(1.2)


@patch(DROP_STR, return_value=False)
def test_run_once(mock_drop, mostly_reliable_server, mock_server_socket):
    mock_addr = MagicMock()
    mock_server_socket.recvfrom = MagicMock(return_value=(
        b'ping 3 2020-08-17 01:01:01.0', mock_addr))
    mostly_reliable_server.is_running = MagicMock(side_effect=(True, False))
    mock_server_socket.sendto = MagicMock(side_effect=None)
    with patch(PROCESS_STR,
               return_value="PONG 3 2020-08-17 01:01:01.0") as mock_process:
        mostly_reliable_server.run()
    mock_server_socket.recvfrom.assert_called_once_with(1024)
    assert mostly_reliable_server.is_running.call_count == 2
    mock_drop.assert_called_once_with(0.7)
    mock_process.assert_called_once_with("ping 3 2020-08-17 01:01:01.0")
    mock_server_socket.sendto.assert_called_once_with(
        b'PONG 3 2020-08-17 01:01:01.0', mock_addr)


@patch(DROP_STR, side_effect=(False, True, False))
def test_run_multi(mock_drop, mostly_reliable_server, mock_server_socket):
    mock_recvs = ((b'ping 1 2020-08-17 19:25:32.1', MagicMock()),
                  (b'ping 2 2020-08-17 19:48:21.7', MagicMock()),
                  (b'ping 3 2020-08-17 20:15:49.5', MagicMock()))
    mock_server_socket.recvfrom = MagicMock(side_effect=mock_recvs)
    mostly_reliable_server.is_running = MagicMock(
        side_effect=(True, True, True, False))
    mock_server_socket.sendto = MagicMock(side_effect=None)
    return_msgs = ("PONG 1 2020-08-17 19:25:32.1",
                   "PONG 3 2020-08-17 20:15:49.5")
    with patch(PROCESS_STR, side_effect=return_msgs) as mock_process:
        mostly_reliable_server.run()
    assert mostly_reliable_server.is_running.call_count == 4
    recv_calls = [call(1024) for _ in range(3)]
    assert mock_server_socket.recvfrom.call_count == 3
    mock_server_socket.recvfrom.assert_has_calls(recv_calls)
    drop_calls = [call(0.7) for _ in range(3)]
    assert mock_drop.call_count == 3
    mock_drop.assert_has_calls(drop_calls)
    process_calls = [call("ping 1 2020-08-17 19:25:32.1"),
                     call("ping 3 2020-08-17 20:15:49.5")]
    assert mock_process.call_count == 2
    mock_process.assert_has_calls(process_calls)
    send_calls = [call(b'PONG 1 2020-08-17 19:25:32.1', mock_recvs[0][1]),
                  call(b'PONG 3 2020-08-17 20:15:49.5', mock_recvs[2][1])]
    assert mock_server_socket.sendto.call_count == 2
    mock_server_socket.sendto.assert_has_calls(send_calls)
