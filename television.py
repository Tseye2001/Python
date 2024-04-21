class Television:
    """
    Attributes:
        _MIN_VOLUME : The minimum volume level.
        _MAX_VOLUME : The maximum volume level.
        _MIN_CHANNEL : The minimum channel number.
        _MAX_CHANNEL : The maximum channel number.
        _status: The power status of the television.
        _muted: Whether the television is muted.
        _volume: The current volume level of the television.
        _channel: The current channel number of the television.
    """

    _MIN_VOLUME: int = 0
    _MAX_VOLUME: int = 2
    _MIN_CHANNEL: int = 0
    _MAX_CHANNEL: int = 3

    def __init__(self) -> None:
        """
        Initializes a Television object with default settings.
        """
        self._status: bool = False
        self._muted: bool = False
        self._volume: int = Television._MIN_VOLUME
        self._channel: int = Television._MIN_CHANNEL

    def power(self) -> None:
        """
        Toggles the power status of the television on or off.
        """
        self._status = not self._status

    def mute(self) -> None:
        """
        Toggles the mute status of the television on and off.
        """
        if self._status:
            self._muted = not self._muted
            if self._muted:
                self._volume = Television._MIN_VOLUME

    def channel_up(self) -> None:
        """
        Increases channel number by 1 of the current channel.
        """
        if self._status:
            if self._channel == Television._MAX_CHANNEL:
                self._channel = Television._MIN_CHANNEL
            else:
                self._channel += 1

    def channel_down(self) -> None:
        """
        Decreases  channel number by 1 of the current channel.
        """
        if self._status:
            if self._channel == Television._MIN_CHANNEL:
                self._channel = Television._MAX_CHANNEL
            else:
                self._channel -= 1

    def volume_up(self) -> None:
        """
        Increases the volume level by 1 of the current volume.
        """
        if self._status:
            if self._muted:
                self._muted = False
            if self._volume < Television._MAX_VOLUME:
                self._volume += 1

    def volume_down(self) -> None:
        """
        Decreases the volume level by 1 of the current.
        """
        if self._status:
            if self._muted:
                self._muted = False
            if self._volume > Television._MIN_VOLUME:
                self._volume -= 1

    def __str__(self) -> str:
        """
        Returns a string of the television object.
        """
        status_str = "True" if self._status else "False"

        return f"Power = {status_str}, Channel = {self._channel}, Volume = {self._volume}"
