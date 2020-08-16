from Networking.UDPPinger.utils import create_pong


def test_empty_list():
    assert create_pong([]) == ["PONG"]


def test_list_with_no_ping():
    assert create_pong(["a", "short", "message"]) == [
        "PONG", "a", "short", "message"]


def test_list_with_one_ping():
    assert create_pong(["PING", "A", "MESSAGE"]) == [
        "PONG", "A", "MESSAGE"]


def test_list_with_multi_ping():
    message_lst = ["PING", "A", "ping", "Message", "Ping",
                   "PING", "with", "many", "pings", "PING"]
    assert create_pong(message_lst) == [
        "PONG", "A", "ping", "Message", "Ping",
        "PONG", "with", "many", "pings", "PONG"]
