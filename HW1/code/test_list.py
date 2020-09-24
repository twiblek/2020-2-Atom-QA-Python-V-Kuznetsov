import pytest

class TestClass:
    def test_len(self):
        assert len([1, 2, 3]) == 3

    def test_reverse(self):
        a = [1, 2, 3]
        a.reverse()
        assert a == [3, 2, 1]

    def test_extend(self):
        a = [1, 2]
        b = [3, 4]
        a.extend(b)
        assert a == [1, 2, 3, 4]

    def test_cut(self):
        a = [1, 2, 3, 4]
        assert a[1:3] == [2, 3]

    @pytest.mark.parametrize('i', list(range(10)))
    def test_index(self, i):
        a = [1, 3, 5, 7, 9]
        assert i in a