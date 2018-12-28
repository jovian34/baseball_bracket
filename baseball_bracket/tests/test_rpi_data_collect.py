import pytest
from baseball_bracket.data_collect.get_current_rpi_wn import NolanRpiExpand


@pytest.fixture()
def nolan_dict():
    nolan = NolanRpiExpand()
    return nolan.get_nolan_dict()

def test_dict_type(nolan_dict):
    assert type(nolan_dict) == dict

def test_size_of_dict_in_range(nolan_dict):
    size = len(nolan_dict)
    assert size < 315
    assert size > 275

def test_number_of_B1G_teams(nolan_dict):
    counter = 0
    for key, value in nolan_dict.items():
        if value['conference'] == 'Big Ten':
            counter += 1
    assert counter == 13

def test_rpi_in_correct_range(nolan_dict):
    assert nolan_dict['INDIANA']['rpi'] <= 1
    assert nolan_dict['INDIANA']['rpi'] >= 0
    assert nolan_dict['TEXAS A&M']['rpi'] <= 1
    assert nolan_dict['TEXAS A&M']['rpi'] >= 0

def test_totals_greater_than_conf(nolan_dict):
    assert nolan_dict['MICHIGAN']['total_wins'] >= nolan_dict['MICHIGAN']['conf_wins']
    assert nolan_dict['VIRGINIA']['total_losses'] >= nolan_dict['MICHIGAN']['conf_losses']
    assert nolan_dict['CONNECTICUT']['total_ties'] >= nolan_dict['MICHIGAN']['conf_ties']
