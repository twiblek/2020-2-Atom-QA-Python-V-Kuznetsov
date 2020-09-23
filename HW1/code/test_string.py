import pytest

class TestClass:
    @pytest.mark.parametrize("input, expected", [('qwerty', 6), ('test', 4)])
    def test_len(self, input, expected):
        assert len(input) == expected

    def test_concat(self):
        assert 'qwe' + 'rty' == 'qwerty'

    def test_inverse(self):
        assert 'qwerty'[::-1] == 'ytrewq'

    def test_cut(self):
        assert 'qwerty'[1:4] == 'wer'

    def test_upper(self):
        assert 'qwerty'.upper() == 'QWERTY'