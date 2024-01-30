from fastapi import FastAPI
from prometheus_client import make_asgi_app, Gauge

from example.manage_containers import list_containers


# Create app
app = FastAPI(debug=False)

# Add prometheus asgi middleware to route /metrics requests
metrics_app = make_asgi_app()
app.mount("/metrics", metrics_app)

containers = list_containers()

g = Gauge("container_running_status", "容器运行状态", ["name", "status"])
for container in containers:
    name = container.name
    status = container.status
    if status != "running":
        g.labels(name=name, status=status).set(0)
    else:
        g.labels(name=name, status=status).set(1)
