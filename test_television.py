import pytest
from television import *
@pytest.fixture
def tv():
   return Television()


def test_init(tv):
   assert tv._status == False
   assert tv._muted == False
   assert tv._volume == Television.MIN_VOLUME
   assert tv._channel == Television.MIN_CHANNEL


def test_power(tv):
   tv.power()
   assert tv._status == True
   tv.power()
   assert tv._status == False


def test_mute(tv):
   tv.power()  # Ensure TV is powered on
   tv.mute()
   assert tv._muted == True
   tv.mute()
   assert tv._muted == False


def test_channel_up(tv):
   tv.channel_up()
   assert tv._channel == Television.MIN_CHANNEL

   tv.power()
   tv.channel_up()
   assert tv._channel == Television.MIN_CHANNEL + 1


def test_channel_down(tv):
   tv.power()  # Ensure TV is powered on
   tv.channel_down()
   assert tv._channel == Television.MAX_CHANNEL
   for _ in range(Television.MAX_CHANNEL - Television.MIN_CHANNEL + 1):
       tv.channel_down()
   assert tv._channel == Television.MAX_CHANNEL


def test_volume_up(tv):
   # Volume up when TV is off
   tv.volume_up()
   assert tv._volume == Television.MIN_VOLUME

   tv.power()  # Ensure TV is powered on

   # Volume up when TV is on
   tv.volume_up()
   assert tv._volume == Television.MIN_VOLUME + 1

   # Mute the TV and volume up
   tv.mute()
   tv.volume_up()
   assert tv._volume == Television.MIN_VOLUME + 2

   # Increase volume to maximum and volume up
   for _ in range(Television.MAX_VOLUME - Television.MIN_VOLUME):
       tv.volume_up()
   tv.volume_up()
   assert tv._volume == Television.MAX_VOLUME


def test_volume_down(tv):
   # Volume down when TV is off
   tv.volume_down()
   assert tv._volume == Television.MIN_VOLUME

   tv.power()  # Ensure TV is powered on

   # Increase volume to maximum
   for _ in range(Television.MAX_VOLUME - Television.MIN_VOLUME):
       tv.volume_up()

   # Volume down when TV is on
   tv.volume_down()
   assert tv._volume == Television.MAX_VOLUME - 1

   # Mute the TV and volume down
   tv.mute()
   tv.volume_down()
   assert tv._volume == Television.MAX_VOLUME - 2

   # Decrease volume to minimum and volume down
   for _ in range(Television.MAX_VOLUME - Television.MIN_VOLUME + 1):  # Include the +1 for wraparound
       tv.volume_down()
   assert tv._volume == Television.MIN_VOLUME
