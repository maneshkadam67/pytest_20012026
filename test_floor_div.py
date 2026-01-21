import pytest


@pytest.mark.parametrize("a,b",[(2,3),(4,5)])
def test_sub(a,b):
    print(a%b)