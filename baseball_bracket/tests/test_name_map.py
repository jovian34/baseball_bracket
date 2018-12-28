from baseball_bracket.data_collect.name_map import boyds_to_nolan


def test_name_map_type():
    assert type(boyds_to_nolan) == dict


def test_size_of_dict():
    assert len(boyds_to_nolan) > 50
    assert len(boyds_to_nolan) < 100
