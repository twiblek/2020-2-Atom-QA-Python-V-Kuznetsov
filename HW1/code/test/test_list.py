import pytest

def test_extend():
    first = [1, 2]
    second = [3, 4]
    first.extend(second)
    assert first == [1, 2, 3, 4]

def test_cut():
    first = [1, 2, 3, 4]
    assert first[1:3] == [2, 3]

@pytest.mark.parametrize('i', list(range(4)))
def test_index(i):
    first = [1, 3]
    assert i in first

def test_len():
    assert len([1, 2, 3]) == 3

class TestClass:
    def test_reverse(self):
        first = [1, 2, 3]
        first.reverse()
        assert first == [3, 2, 1]
