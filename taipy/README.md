
Taipy behing jh proxy:

```python
Gui(page=page).run(base_url=os.environ.get("JUPYTERHUB_SERVICE_PREFIX"))
```

docker run --rm -it -p 8888:8888 docker.io/library/taipy --port 8888

docker build -t taipy .