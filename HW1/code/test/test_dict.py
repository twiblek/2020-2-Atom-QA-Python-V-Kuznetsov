import pytest

def test_copy():
    first = {'first': 1, 'b': 2}
    second = first.copy()
    assert first == second

@pytest.mark.parametrize("input_val, expected", [('a', 1), ('c', 'default')])
def test_pop(input_val, expected):
    first = {'a': 1, 'b': 2}
    value = first.pop(input_val, expected)
    assert value == expected

def test_len():
    first = {'a': 1, 'b': 2}
    assert len(first) == 2

def test_empty_key():
    first = {}
    with pytest.raises(KeyError):
        assert first['test']

class TestSet:
    def test_add(self):
        first = {}
        first['key'] = 'value'
        assert 'key' in first
