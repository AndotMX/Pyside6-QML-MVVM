import sys

from PySide6.QtCore import QObject, Slot
from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine

from utils import get_source_root, log  # Import the function to get the source root path

# Get the path to your python script's directory, then point to your QML folder
app = QGuiApplication(sys.argv)
engine = QQmlApplicationEngine()
engine.addImportPath(get_source_root())


class Backend(QObject):
    @Slot()
    def on_button_clicked(self):
        log.info("Button was clicked! Triggered from Python backend.")


if __name__ == "__main__":
    # Expose the Python class backend to the QML context
    backend = Backend()
    engine.rootContext().setContextProperty("pythonBackend", backend)

    # Load the visual layout
    engine.loadFromModule("view", "Main")

    if not engine.rootObjects():
        sys.exit(-1)

    sys.exit(app.exec())
