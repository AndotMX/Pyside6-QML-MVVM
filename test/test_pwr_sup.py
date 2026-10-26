import pytest

from model import PowerSupplyBase
from view_model import get


@pytest.fixture
def pwr_module() -> PowerSupplyBase:
    """Fixture for the PowerSupplyMock instance."""
    pwr = get(module="PowerSupply")
    return pwr


def test_multiton(pwr_module: type[PowerSupplyBase]):
    """Test that the multiton pattern is working correctly."""
    pwr1 = pwr_module(port="COM1")
    pwr2 = pwr_module(port="COM1")
    pwr3 = pwr_module(port="COM2")

    assert pwr1 is pwr2, "Instances with the same port should be the same (multiton)."
    assert pwr1 is not pwr3, "Instances with different ports should be different."
