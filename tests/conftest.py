import pytest

@pytest.fixture(scope="session")
def preWork():
    print("Pre work done...")
    return "Pass"