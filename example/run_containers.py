from example.init_client import client


def run_containers(image, cmd):
    return client.containers.run(image=image, command=cmd)
