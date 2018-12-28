import pytest
from baseball_bracket.data_collect.get_current_isr_bw import BoydsIsr


@pytest.fixture()
def boyd_dict():
    boyd = BoydsIsr()
    return boyd.get_isr_dict()


def test_dict_type(boyd_dict):
    assert type(boyd_dict) == dict


def test_size_of_dict_in_range(boyd_dict):
    size = len(boyd_dict)
    assert size < 315
    assert size > 275


def test_number_of_hawaii_teams(boyd_dict):
    counter = 0
    for key, value in boyd_dict.items():
        if value['state'] == 'HI':
            counter += 1
    assert counter == 1


def test_isr_in_correct_range(boyd_dict):
    assert boyd_dict['INDIANA']['isr'] <= 200
    assert boyd_dict['INDIANA']['isr'] >= 0
    assert boyd_dict['TEXAS A&M']['isr'] <= 200
    assert boyd_dict['TEXAS A&M']['isr'] >= 0


