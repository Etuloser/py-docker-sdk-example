import pytest

from example.init_client import client


def test_dir_client():
    got = dir(client)
    print(got)
    assert got != None
