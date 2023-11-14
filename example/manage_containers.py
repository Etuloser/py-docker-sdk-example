from example.init_client import client


def list_containers():
    return client.containers.list()
