import pytest

def test_concat():
    assert 'qwe' + 'rty' == 'qwerty'

def test_inverse():
    assert 'qwerty'[::-1] == 'ytrewq'

def test_cut():
    assert 'qwerty'[1:4] == 'wer'

def test_upper():
    assert 'qwerty'.upper() == 'QWERTY'

class TestClass:
    @pytest.mark.parametrize("input_val, expected", [('qwerty', 6), ('test', 4)])
    def test_len(self, input_val, expected):
        assert len(input_val) == expected
