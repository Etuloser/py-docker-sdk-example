import pytest

from example.run_containers import run_containers


def test_run_containers():
    got = run_containers("ubuntu", "echo hello world")
    print(got)
    assert got == b"hello world\n"
