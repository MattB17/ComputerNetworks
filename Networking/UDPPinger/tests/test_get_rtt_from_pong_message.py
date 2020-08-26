from datetime import datetime
from Networking.UDPPinger.utils import get_rtt_from_pong_message


def test_with_rtt_under_one_second():
    pong_message = "PONG 3 2020-08-23 17:53:27.152000"
    received_time = datetime(2020, 8, 23, 17, 53, 27, 765000)
    assert get_rtt_from_pong_message(pong_message, received_time) == 613000


def test_with_rtt_over_one_second():
    pong_message = "PONG 5 2020-08-23 17:55:14.327000"
    received_time = datetime(2020, 8, 23, 17, 55, 16, 530000)
    assert get_rtt_from_pong_message(pong_message, received_time) == 2203000
