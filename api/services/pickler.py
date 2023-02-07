import codecs
import pickle
from typing import Any


def pickle_object(object: Any) -> str:
    return codecs.encode(pickle.dumps(object), "base64").decode()


def unpickle_object(pickled_object: str) -> Any:
    return pickle.loads(codecs.decode((pickled_object).encode(), "base64"))
