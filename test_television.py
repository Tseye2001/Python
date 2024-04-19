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
   tv.power()  
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
   tv.power() 
   tv.channel_down()
   assert tv._channel == Television.MAX_CHANNEL
   for _ in range(Television.MAX_CHANNEL - Television.MIN_CHANNEL + 1):
       tv.channel_down()
   assert tv._channel == Television.MAX_CHANNEL


def test_volume_up(tv):
   tv.volume_up()
   assert tv._volume == Television.MIN_VOLUME

   tv.power()  

   tv.volume_up()
   assert tv._volume == Television.MIN_VOLUME + 1

   tv.mute()
   tv.volume_up()
   assert tv._volume == Television.MIN_VOLUME + 2

   for _ in range(Television.MAX_VOLUME - Television.MIN_VOLUME):
       tv.volume_up()
   tv.volume_up()
   assert tv._volume == Television.MAX_VOLUME


def test_volume_down(tv):
   
   tv.volume_down()
   assert tv._volume == Television.MIN_VOLUME

   tv.power()  

   for _ in range(Television.MAX_VOLUME - Television.MIN_VOLUME):
       tv.volume_up()

   tv.volume_down()
   assert tv._volume == Television.MAX_VOLUME - 1

   tv.mute()
   tv.volume_down()
   assert tv._volume == Television.MAX_VOLUME - 2

   for _ in range(Television.MAX_VOLUME - Television.MIN_VOLUME + 1): 
       tv.volume_down()
   assert tv._volume == Television.MIN_VOLUME
