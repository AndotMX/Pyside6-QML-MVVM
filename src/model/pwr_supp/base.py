from abc import abstractmethod

from ..core import SendExpect


class PowerSupplyBase(SendExpect):
    _available_channels: list[int] = [1]
    _active_channel: int = 1
    _output_state = False
    voltage: float
    current: float

    @property
    @abstractmethod
    def voltage(self) -> float:
        """Get the current output voltage of the power supply.

        Returns:
            float: The current output voltage.
        """
        ...

    @voltage.setter
    @abstractmethod
    def voltage(self, voltage: float) -> None:
        """Set the output voltage of the power supply.

        Args:
            voltage (float): The desired output voltage.
        """
        ...

    @property
    @abstractmethod
    def current(self) -> float:
        """Get the current output current of the power supply.

        Returns:
            float: The current output current.
        """
        ...

    @current.setter
    @abstractmethod
    def current(self, current: float) -> None:
        """Set the output current of the power supply.

        Args:
            current (float): The desired output current.
        """
        ...

    @property
    @abstractmethod
    def output_state(self) -> bool:
        """Get the current output state of the power supply.

        Returns:
            bool: True if the output is ON, False if OFF.
        """
        ...

    @output_state.setter
    @abstractmethod
    def output_state(self, state: bool) -> None:
        """Set the output state of the power supply.

        Args:
            state (bool): True to turn ON the output, False to turn OFF.
        """
        ...
