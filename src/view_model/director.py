from collections import defaultdict

from model.core import HALRegistry
from utils import load_cfg


def initiate():
    """Initiate the wanted drivers for the particular env"""
    current_env = defaultdict(dict)
    cfg = load_cfg()
    for mod in HALRegistry._registry.keys() & cfg.keys():
        driver = cfg[mod]["type"]
        kwargs = cfg[mod]["kwargs"]
        current_env[mod] = HALRegistry.create(mod, driver, **kwargs)
    return current_env


def get(module):
    """Find the wanted driver class for the particular  module"""
    cfg = load_cfg()
    return HALRegistry._registry[module][cfg[module]["type"]]
