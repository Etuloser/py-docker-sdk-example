import pytest

from example.manage_containers import list_containers


def test_list_containers():
    containers = list_containers()
    for container in containers:
        print(container.attrs.get("Name"))


# dir
# ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'attach', 'attach_socket', 'attrs', 'client', 'collection', 'commit', 'diff', 'exec_run', 'export', 'get_archive', 'health', 'id', 'id_attribute', 'image', 'kill', 'labels', 'logs', 'name', 'pause', 'ports', 'put_archive', 'reload', 'remove', 'rename', 'resize', 'restart', 'short_id', 'start', 'stats', 'status', 'stop', 'top', 'unpause', 'update', 'wait']
