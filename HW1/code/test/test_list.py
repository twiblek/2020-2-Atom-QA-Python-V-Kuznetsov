import pytest

def test_extend():
    first = [1, 2]
    second = [3, 4]
    first.extend(second)
    assert first == [1, 2, 3, 4]

def test_cut():
    first = [1, 2, 3, 4]
    assert first[1:3] == [2, 3]

@pytest.mark.parametrize("input_val, expected", [(1, 2), (2, 0)])
def test_count(input_val, expected):
    first = [1, 1, 3]
    assert first.count(input_val) == expected

def test_len():
    assert len([1, 2, 3]) == 3

class TestClass:
    def test_reverse(self):
        first = [1, 2, 3]
        first.reverse()
        assert first == [3, 2, 1]
