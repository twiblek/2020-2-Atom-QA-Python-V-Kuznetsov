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

    def test_intersection(self):
        a = set('12345')
        b = set('34567')
        assert a.intersection(b) == {'3', '4', '5'}

    def test_pop_len(self):
        a = set('len')
        a.pop()
        assert len(a) == 2

    def test_remove(self):
        a = set('remove')
        with pytest.raises(KeyError):
            a.remove('b')