import time

from PySide6.QtCore import QObject, Signal, Slot

from model import PowerSupplyBase


class PowerSuppViewModel(QObject):
    data_ready = Signal(float)
    status_message = Signal(str)

    def __init__(self, backned: PowerSupplyBase):
        super().__init__()
        self.backend = backned

    @Slot()
    def start_polling(self):
        if self.backend.open():
            self.status_message.emit("Hardware connected.")
            self._running = True
            while self._running:
                voltage = self.backend.voltage
                self.data_ready.emit(voltage)
                time.sleep(1.0)  # Polling rate limit
        else:
            self.status_message.emit("Connection failed.")

    @Slot()
    def stop_polling(self):
        self._running = False
        self.status_message.emit("Polling stopped.")
