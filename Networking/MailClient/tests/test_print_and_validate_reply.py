import pytest
import io
import sys
from Networking.Base import exceptions as exc
from Networking.MailClient.utils import print_and_validate_reply


def test_with_expected_code():
    captured_output = io.StringIO()
    sys.stdout = captured_output
    reply_msg = "250 Hello user@email.com, pleased to meet you."
    print_and_validate_reply(reply_msg, 250)
    sys.stdout = sys.__stdout__
    assert str(captured_output.getvalue()) == "{}\n".format(reply_msg)


def test_with_unexpected_code():
    captured_output = io.StringIO()
    sys.stdout = captured_output
    reply_msg = "530 could not verify sender identity."
    with pytest.raises(exc.UnexpectedResponseCode):
        print_and_validate_reply(reply_msg, 250)
    sys.stdout = sys.__stdout__
    assert str(captured_output.getvalue()) == "{}\n".format(reply_msg)
