import pytest

class TestSet:
    def test_add(self):
        a = set('a')
        a.add('b')
        assert a == {'a', 'b'}

    def test_copy(self):
        a = set('copy')
        b = a.copy()
        assert a == b

    @pytest.mark.parametrize("input, expected", [(['123', '456'], ''), (['2345', '4567'], '45')])
    def test_intersection(self, input, expected):
        a = set(input[0])
        b = set(input[1])
        assert a.intersection(b) == set(expected)

    def test_pop_len(self):
        a = set('len')
        a.pop()
        assert len(a) == 2

    def test_remove(self):
        a = set('remove')
        with pytest.raises(KeyError):
            a.remove('b')