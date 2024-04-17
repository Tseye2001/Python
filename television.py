class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self):
        self._status = False
        self._muted = False
        self._volume = Television.MIN_VOLUME
        self._channel = Television.MIN_CHANNEL

    def power(self):
        self._status = not self._status

    def mute(self):
        if self._status:
            self._muted = not self._muted
            if self._muted:
                self._volume = Television.MIN_VOLUME

    def channel_up(self):
        if self._status:
            if self._channel == Television.MAX_CHANNEL:
                self._channel = Television.MIN_CHANNEL
            else:
                self._channel += 1

    def channel_down(self):
        if self._status:
            if self._channel == Television.MIN_CHANNEL:
                self._channel = Television.MAX_CHANNEL
            else:
                self._channel -= 1

    def volume_up(self):
        if self._status:
            if self._muted:
                self._muted = False
            if self._volume < Television.MAX_VOLUME:
                self._volume += 1

    def volume_down(self):
        if self._status:
            if self._muted:
                self._muted = False
            if self._volume > Television.MIN_VOLUME:
                self._volume -= 1

    def __str__(self):
        status_str = "True" if self._status else "False"
        return f"Power = {status_str}, Channel = {self._channel}, Volume = {self._volume}"
