from collections import OrderedDict

import pytest

from herald import Herald
from herald.types import Messenger

herald = Herald(secrets="tests/test.env")


class TestMessenger(Messenger):
    def __init__(self):
        self.secrets = None

    def set_secrets(self, secrets) -> None:
        self.secrets = secrets

    def notify(self, info) -> None:
        print(info)


def test_function_complete():
    @herald(TestMessenger())
    def get_list():
        x = [1, 2, 3]
        return x

    result = get_list()
    return result


def test_function_error():
    @herald(TestMessenger())
    def get_item():
        x = [1, 2, 3]
        return x[len(x) + 1]

    with pytest.raises(IndexError):
        result = get_item()
        return result


def test_secrets_are_loaded():
    assert type(herald.secrets) is OrderedDict


def test_messenger_secrets_are_set():
    test_messenger = TestMessenger()
    herald._set_messenger_secrets(test_messenger)
    assert test_messenger.secrets is not None
    assert len(test_messenger.secrets) > 0
