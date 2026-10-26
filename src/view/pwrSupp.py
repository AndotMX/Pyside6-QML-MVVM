import sys

from PySide6.QtCore import QThread, Slot
from PySide6.QtWidgets import QApplication, QLabel, QMainWindow, QPushButton, QVBoxLayout, QWidget

from model.pwr_supp.base import PowerSupplyBase
from view_model import PowerSuppViewModel, initiate


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        env = initiate()
        self.setWindowTitle("PySide6 HAL Architecture Example")

        # UI Elements
        self.label = QLabel("Voltage: -- V")
        self.status_label = QLabel("Status: Idle")
        self.btn_start = QPushButton("Start HW Stream")

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.status_label)
        layout.addWidget(self.btn_start)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        # Thread & HAL Initialization
        self.hardware_thread = QThread()
        self.sensor_hal: PowerSupplyBase = env[
            "PowerSupply"
        ]  # Easily switchable to any concrete HAL
        self.worker = PowerSuppViewModel(self.sensor_hal)

        # Move worker context to separate thread
        self.worker.moveToThread(self.hardware_thread)

        # Wire communication bindings
        self.hardware_thread.started.connect(self.worker.start_polling)
        self.worker.data_ready.connect(self.update_ui)
        self.worker.status_message.connect(self.status_label.setText)

        self.btn_start.clicked.connect(self.toggle_hardware)

    def toggle_hardware(self):
        if not self.hardware_thread.isRunning():
            self.btn_start.setText("Stop HW Stream")
            self.hardware_thread.start()
        else:
            self.btn_start.setText("Start HW Stream")
            self.worker.stop_polling()
            self.hardware_thread.quit()
            self.hardware_thread.wait()

    @Slot(float)
    def update_ui(self, value: float):
        self.label.setText(f"Voltage: {value} V")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
