# README.md

>Library reference
>
>https://docker-py.readthedocs.io/en/stable/

## 快速开始

poetry:

```bash
poetry install
```

pip:

```bash
pip install -r requirements.txt
```

### Docker Engine SDKs Python 实现示例：

* [init_client.py](https://github.com/Etuloser/py-docker-sdk-example/blob/main/example/init_client.py)：客户端初始化

* [manage_containers.py](https://github.com/Etuloser/py-docker-sdk-example/blob/main/example/manage_containers.py)：容器管理

* [run_containers.py](https://github.com/Etuloser/py-docker-sdk-example/blob/main/example/run_containers.py)：运行容器

### Prometheus Python Client 演示：

```bash
uvicorn example.metrics:app --host=0.0.0.0 --port=30000
```
