import pytest
from television import *


@pytest.fixture
def tv():
    return Television()


def test_init(tv):
    assert tv._status == False
    assert tv._muted == False
    assert tv._volume == Television._MIN_VOLUME
    assert tv._channel == Television._MIN_CHANNEL


def test_power(tv):
    tv.power()
    assert tv._status == True
    tv.power()
    assert tv._status == False


def test_mute(tv):
    tv.power()
    tv.mute()
    assert tv._muted == True
    tv.mute()
    assert tv._muted == False


def test_channel_up(tv):
    tv.channel_up()
    assert tv._channel == Television._MIN_CHANNEL

    tv.power()
    tv.channel_up()
    assert tv._channel == Television._MIN_CHANNEL + 1


def test_channel_down(tv):
    tv.power()
    tv.channel_down()
    assert tv._channel == Television._MAX_CHANNEL
    for _ in range(Television._MAX_CHANNEL - Television._MIN_CHANNEL + 1):
        tv.channel_down()
    assert tv._channel == Television._MAX_CHANNEL


def test_volume_up(tv):
    tv.volume_up()
    assert tv._volume == Television._MIN_VOLUME

    tv.power()

    tv.volume_up()
    assert tv._volume == Television._MIN_VOLUME + 1

    tv.mute()
    tv.volume_up()
    assert tv._volume == Television._MIN_VOLUME + 1

    for _ in range(Television._MAX_VOLUME - Television._MIN_VOLUME):
        tv.volume_up()
    tv.volume_up()
    assert tv._volume == Television._MAX_VOLUME


def test_volume_down(tv):
    tv.volume_down()
    assert tv._volume == Television._MIN_VOLUME

    tv.power()

    for _ in range(Television._MAX_VOLUME - Television._MIN_VOLUME):
        tv.volume_up()

    tv.volume_down()
    assert tv._volume == Television._MAX_VOLUME - 1

    tv.mute()
    tv.volume_down()
    assert tv._volume == Television._MAX_VOLUME - 2

    for _ in range(Television._MAX_VOLUME - Television._MIN_VOLUME + 1):
        tv.volume_down()
    assert tv._volume == Television._MIN_VOLUME
