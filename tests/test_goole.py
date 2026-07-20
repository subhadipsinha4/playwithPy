import pytest

@pytest.fixture(scope="function")
def pre_work():
    print("Pre work done for google...")
    return "fail"

def test_initCheck(pre_work):
    print("Executing test...")
    assert pre_work == "fail"

@pytest.mark.skip(reason="Skipping this test for now")
def test_SecondCheck(preWork):
    print("Executing Second test...")
    assert 2 + 2 == 4

