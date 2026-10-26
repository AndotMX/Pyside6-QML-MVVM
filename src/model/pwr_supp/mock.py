from random import uniform
from time import sleep

from utils import log

from ..core import HALRegistry, multiton
from .base import PowerSupplyBase


@HALRegistry.register("PowerSupply", "mock")
@multiton
class PowerSupplyMock(PowerSupplyBase):
    _available_channels = [1, 2]
    _voltage = 0.0
    _current = 0.0

    def open(self) -> bool:
        log.info(
            f"[bold green]Mock Power Supply[/bold green]: Opening connection on port {self._port}..."
        )
        self.is_open = True
        return True

    def close(self) -> bool:
        log.info(
            f"[bold red]Mock Power Supply[/bold red]: Closing connection on port {self._port}..."
        )
        self.is_open = False
        return True

    def dispose(self) -> bool:
        log.info("[bold yellow]Mock Power Supply[/bold yellow]: Disposing resources...")
        return self.close()

    def send(self, data: float | bool) -> float | bool:
        log.info("[bold blue]Mock Power Supply[/bold blue]: Sending message to protocol...")
        sleep(uniform(0.1, 0.5))  # Simulate a delay in sending
        return data

    def expect(self, data: float | bool, timeout: float = 1.0) -> float | bool:
        log.info(
            "[bold magenta]Mock Power Supply[/bold magenta]: Expecting message from protocol..."
        )
        sleep(uniform(0.1, timeout))  # Simulate a delay in response
        return data

    @property
    def voltage(self) -> float:
        log.info(f"[bold green]Mock Power Supply[/bold green]: Getting voltage: {self._voltage} V")
        return self.expect(self._voltage)  # Simulate reading the voltage

    @voltage.setter
    def voltage(self, voltage: float) -> None:
        log.info(f"[bold green]Mock Power Supply[/bold green]: Setting voltage to: {voltage} V")
        self._voltage = self.send(voltage)  # Simulate sending the voltage command

    @property
    def current(self) -> float:
        log.info(f"[bold green]Mock Power Supply[/bold green]: Getting current: {self._current} A")
        return self.expect(self._current)  # Simulate reading the current

    @current.setter
    def current(self, current: float) -> None:
        log.info(f"[bold green]Mock Power Supply[/bold green]: Setting current to: {current} A")
        self._current = self.send(current)  # Simulate sending the current command

    @property
    def output_state(self) -> bool:
        log.info(
            f"[bold green]Mock Power Supply[/bold green]: Getting output state: {self._output_state}"
        )
        return bool(self.expect(self._output_state))  # Simulate reading the output state

    @output_state.setter
    def output_state(self, state: bool) -> None:
        log.info(f"[bold green]Mock Power Supply[/bold green]: Setting output state to: {state}")
        self._output_state = bool(self.send(state))  # Simulate sending the output state command

    def set_active_channel(self, channel: int) -> None:
        if channel not in self._available_channels:
            raise ValueError(
                f"Channel must be between {self._available_channels[0]} or {self._available_channels[-1]}."
            )
        log.info(
            f"[bold green]Mock Power Supply[/bold green]: Setting active channel to: {channel}"
        )
        self._active_channel = channel
