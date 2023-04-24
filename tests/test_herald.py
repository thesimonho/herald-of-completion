import pytest

from herald import Herald
from herald.types import Messenger

herald = Herald()


class TestMessenger(Messenger):
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
