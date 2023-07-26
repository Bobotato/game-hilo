from api.repository.pickler import pickle_object, unpickle_object


def test_pickle_object():
    assert pickle_object("test") == "gASVCAAAAAAAAACMBHRlc3SULg==\n"


def test_unpickle_object():
    pickled_object = "gASVCAAAAAAAAACMBHRlc3SULg==\n"
    assert unpickle_object(pickled_object) == "test"
