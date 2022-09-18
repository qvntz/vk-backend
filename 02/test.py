import json
from random import randint
from unittest.mock import Mock

import pytest

from main import parse_json


@pytest.fixture
def data():
    return json.dumps(
        {
            'a': 'a b c d e a',
            'b': '1 2 234 4 56 6',
            '123': '456',
            '123as': 'asdasdasd asd asd'
        }
    )


def test_data(data):
    mock = Mock()
    parse_json(
        data, mock, ['a', 'b', '123'],
        ['a', 'b', 'c', 'e', '1', '456', '234', '4', '56', 'asdasdw']
    )
    assert mock.call_count == 10


def test_faker(faker):
    data = faker.text()
    list_data = data.split()
    keywords = []
    for i in range(randint(0, len(list_data) - 1)):
        keywords.append(list_data[randint(0, len(list_data) - 1)])
    count = 0
    for i in keywords:
        count += list_data.count(i)
    mock = Mock()
    parse_json(
        json.dumps({'a': data, 'b': keywords[0]}), mock, ['a'], keywords
    )
    assert mock.call_count == count
