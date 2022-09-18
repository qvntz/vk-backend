import pytest
from unittest.mock import Mock, patch

from main import CrossZeros


@pytest.fixture
def cross_zeros():
    return CrossZeros()


@pytest.mark.parametrize(
    "test_input, expected",
    [
        ('a', None), (' ', None), ('0', None), ('10', None), ('1.1', None),
        ('1', 1), ('2', 2), ('3', 3), ('9', 9)
    ]
)
def test_validate_input(cross_zeros, monkeypatch, test_input, expected):
    monkeypatch.setattr('builtins.input', lambda _: test_input)
    print(cross_zeros.validate_input())
    assert cross_zeros.validate_input() == expected


@pytest.mark.parametrize(
    'test_input, expected',
    [
        ((1, 2, 3), 'x'), ((4, 5, 6), 'x'), ((7, 8, 9), 'x'), ((1, 4, 7), 'x'),
        ((2, 5, 8), 'x'), ((3, 6, 9), 'x'), ((1, 5, 9), 'x'), ((3, 5, 7), 'x')
    ]
)
def test_win(cross_zeros, test_input, expected):
    for i in test_input:
        cross_zeros.board[i] = expected
    assert cross_zeros.check_winner() == expected


@pytest.mark.parametrize(
    'test_input, expected',
    [
        (['1', '5', '2', '3', '7', '4', '6', '8', '9'], None),
        (['9', '5', '1', '3', '7', '4', '6', '8', '2'], None)
    ]
)
def test_draw(cross_zeros, monkeypatch, test_input, expected):
    input_mock = Mock()
    input_mock.side_effect = test_input
    with patch('builtins.input', input_mock):
        assert cross_zeros.start_game() == expected