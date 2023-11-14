import pytest

from example.manage_containers import list_containers


def test_list_containers():
    got = list_containers()
    print(dir(got[0]))
    assert got != None
