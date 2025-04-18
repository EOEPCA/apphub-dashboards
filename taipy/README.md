
Taipy behing jh proxy:

```python
Gui(page=page).run(base_url=os.environ.get("JUPYTERHUB_SERVICE_PREFIX"))
```