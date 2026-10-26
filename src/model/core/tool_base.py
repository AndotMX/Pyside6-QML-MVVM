from abc import ABC, abstractmethod
from typing import Any


class Tool(ABC):
    """Abstract base class for tools to be used in the application.
    This class defines the interface that all tool implementations must adhere to.
    """

    is_open: bool = False
    _port: None | str = None

    def __init__(self, port: str, auto_open: bool = True):
        self._port = port
        if auto_open:
            self.open()  # Automatically open the mock power supply connection upon initialization

    @abstractmethod
    def open(self) -> bool:
        """Open the tool and prepare it for operation.

        Returns:
            bool: operation success status.
        """
        ...

    @abstractmethod
    def close(self) -> bool:
        """Close the tool and release any resources it holds.

        Returns:
            bool: operation success status.
        """
        ...

    @abstractmethod
    def dispose(self) -> bool:
        """Clean up resources and prepare the object for garbage collection.

        Returns:
            bool: operation success status.
        """
        ...

    # --- Context Manager Implementation ---
    def __enter__(self):
        self.open()
        return self  # This is what the 'as' variable receives

    def __exit__(self, exc_type, exc_val, exc_tb):
        # Always call your cleanup logic when exiting the 'with' block
        self.dispose()
        # Returning False (or None) allows any exceptions raised inside
        # the 'with' block to propagate normally.
        return False


class SendExpect(Tool):
    """Abstract base class for tools that support sending and expecting data.
    This class extends the Tool abstract base class.

    """

    @abstractmethod
    def send(self, data: Any) -> Any: ...

    @abstractmethod
    def expect(self, data: Any, timeout: float = 10.0) -> Any: ...
