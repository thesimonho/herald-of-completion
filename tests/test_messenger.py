import pytest

from herald.decorators import Herald
from herald.messengers import (DesktopMessenger, DiscordMessenger,
                               EmailMessenger)

herald = Herald(secrets="tests/test.env")


def test_desktop_has_no_secrets(mocker):
    desktop = DesktopMessenger()
    mocker.patch("herald.messengers.DesktopMessenger.notify", return_value=None)

    @herald(desktop)
    def get_list():
        x = [1, 2, 3]
        return x

    get_list()
    assert desktop.__dict__ == {}


def test_email_address_correct():
    _ = EmailMessenger("user@email.com")
    _ = EmailMessenger("user-name@email.address.com")


def test_email_address_incorrect():
    with pytest.raises(ValueError):
        _ = EmailMessenger("useremail.com")

    with pytest.raises(ValueError):
        _ = EmailMessenger("user@emailcom")


def test_discord_has_url(mocker):
    discord = DiscordMessenger()
    mocker.patch("herald.messengers.DiscordMessenger.notify", return_value=None)

    @herald(discord)
    def get_list():
        x = [1, 2, 3]
        return x

    get_list()
    assert discord.webhook_url == "http://google.com"
