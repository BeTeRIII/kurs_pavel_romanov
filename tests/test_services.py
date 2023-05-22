from json import JSONDecodeError
import pytest

import json

from utils.services import load_json, date_format, sort_by_date, get_last_five_succsessful_operation

def test_load_json():
    assert load_json('data_tests/correct.json') == []

    with pytest.raises(JSONDecodeError):
        assert load_json('data_tests/no_correct.json')
        test_data = "2019-04-18T11:22:18.800453"
        assert date_format(test_data) == "18.04.2019 11.22.18"

def test_sort_by_date():
    test_data1 = [
        {"date": "2019-04-19T12:02:30.129240"}
        {"date": "2019-11-13T17:38:04.800051"}
        {"date": "2019-06-30T15:11:53.136004"}
    ]
    assert sort_by_date(test_data1) == [
        {"date": "2019-11-13T17:38:04.800051"}
        {"date": "2019-06-30T15:11:53.136004"}
        {"date": "2019-04-19T12:02:30.129240"}
    ]
