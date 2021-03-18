import rps
import pytest

@pytest.fixture(scope='session', autouse=True)
def game(request):
    return rps.Game()