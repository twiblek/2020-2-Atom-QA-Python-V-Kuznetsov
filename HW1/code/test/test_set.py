import pytest

def test_add():
    first = set('a')
    first.add('b')
    assert first == {'a', 'b'}

def test_copy():
    first = set('copy')
    second = first.copy()
    assert first == second

@pytest.mark.parametrize("input_val, expected", [(['123', '456'], ''), (['2345', '4567'], '45')])
def test_intersection(input_val, expected):
    first = set(input_val[0])
    second = set(input_val[1])
    assert first.intersection(second) == set(expected)

class TestSet:
    def test_pop_len(self):
        first = set('len')
        initial_length = len(first)
        first.pop()
        assert len(first) == initial_length - 1

    def test_remove(self):
        first = set('remove')
        with pytest.raises(KeyError):
            assert first.remove('b')
