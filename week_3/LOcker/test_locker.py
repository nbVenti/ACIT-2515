import pytest

from locker import Locker


def test_locker_invalid_code():
    """Constructor does not accept anything but strings with more than 3 characters"""
    with pytest.raises(AttributeError):
        Locker("12")

    with pytest.raises(AttributeError):
        Locker(1234)


def test_locker_locked():
    """Locker is unlocked by default"""
    storage = Locker("12345")
    assert storage.locked is False

    # Constructor takes only one argument
    with pytest.raises(TypeError):
        Locker("12345", False)


def test_locker_lock():
    """We can lock the storage"""
    storage = Locker("12345")
    storage.lock()
    assert storage.locked is True


def test_locker_unlock():
    """Or unlock it"""
    storage = Locker("12345")
    storage.locked = True
    assert storage.unlock_with_code(12345) is False
    assert storage.locked is True
    assert storage.unlock_with_code("12345")
    assert storage.locked is False


def test_locker_contents():
    """Locker has contents. It starts as an empty list, and is related to the is_empty method"""
    storage = Locker("12345")
    assert storage.contents == []
    assert storage.is_empty() is True
    storage.contents = ["stuff"]
    assert storage.is_empty() is False
