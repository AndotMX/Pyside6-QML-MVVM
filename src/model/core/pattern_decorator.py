"""Reusable design patterns for the project to be used as decorators."""

from collections import defaultdict
from functools import wraps


def singleton(cls):
    """Decorator to make a class a singleton.
    Ensures that only one instance of the class exists throughout the application."""
    instances = {}

    @wraps(cls)
    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return get_instance


def multiton(cls):
    """
    A class decorator that transforms a class into a Multiton.
    It maintains a registry of unique instances based on the first argument (the key).
    """
    # Map to store instance references: { key: instance }
    instances = {}

    @wraps(cls)
    def get_instance(*args, **kwargs):
        # Determine the key. Typically, the first positional argument is used.
        # If no positional arguments are provided, use a sentinel or default key.
        if args:
            key = args[0]
        elif kwargs:
            # Fallback to the first keyword argument sorted by name if no positional args exist
            key = kwargs[sorted(kwargs.keys())[0]]
        else:
            key = None

        # Check if the instance already exists for the given key
        if key not in instances:
            instances[key] = cls(*args, **kwargs)

        return instances[key]

    return get_instance


class HALRegistry:
    """Hardware Abstration Layer decorator using Registry pattern.
    This ensures that the appropiate Hardware is used when reading the bench_cfg .json file

    Raises:
        ImportError: Driver is already registered,
        KeyError: Trying to initialize a driver not it the registry
    """

    _registry = defaultdict(dict)

    @classmethod
    def register(cls, module: str, driver: str):
        """Decorator to register a HAL device or driver class."""

        def decorator(hw_class):
            if driver in cls._registry:
                raise ImportError(f"Hardware driver '{driver}' is already registered.")
            cls._registry[module][driver] = hw_class
            return hw_class

        return decorator

    @classmethod
    def create(cls, module: str, driver: str, *args, **kwargs):
        """Factory method to instantiate a registered HAL driver by name."""
        if module not in cls._registry:
            raise ImportError(f"Hardware Module {module} is not included.")
        if driver not in cls._registry[module]:
            raise KeyError(f"Hardware driver '{driver}' not found in {module}.")
        hw_class = cls._registry[module][driver]
        return hw_class(*args, **kwargs)

    @classmethod
    def list_drivers(cls):
        """Return a list of all registered driver names."""
        return [*cls._registry.items()]
