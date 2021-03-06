import pytest

def test_comp():
    assert 1 == 1

def test_abs():
    assert abs(-1) == 1

def test_to_int():
    assert int('1') == 1

class TestClass:
    @pytest.mark.parametrize("values", [[1,2,3], [0,-2,-2]])
    def test_sum(self, values):
        assert values[0] + values[1] == values[2]

    @pytest.mark.parametrize("values", [[1,2,2], [0,-2,0]])
    def test_multiply(self, values):
        assert values[0] * values[1] == values[2]
