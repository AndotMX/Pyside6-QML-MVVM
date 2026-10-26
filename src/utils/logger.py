import logging

from rich.logging import RichHandler

# Advanced setup with custom parameters
rich_handler = RichHandler(
    level=logging.DEBUG,
    show_time=True,  # Toggles the timestamp column
    omit_repeated_times=True,  # Hides the timestamp if it's the exact same as the previous log
    show_level=True,  # Toggles the [INFO], [WARNING], etc. label column
    show_path=True,  # Toggles the file path and line number column
    enable_link_path=True,  # Makes the path column a clickable link in supported terminals
    markup=True,  # Allows you to use Rich console markup inside your log strings
    rich_tracebacks=True,  # Renders beautiful, multi-colored exception tracebacks
    tracebacks_show_locals=True,  # Dumps local variables inside the exception traceback for fast debugging
)

# Configure the root logger to use RichHandler
logging.basicConfig(
    level="NOTSET",
    format="%(message)s",
    datefmt="[%X]",
    handlers=[rich_handler],
)

log = logging.getLogger("rich")
