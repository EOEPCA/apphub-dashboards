
Inspired from https://github.com/reflex-dev/reflex/blob/main/docker-example/simple-one-port/

Fixed with

```python
    frontend_path=os.environ.get("JUPYTERHUB_SERVICE_PREFIX").rstrip('/'),
```
