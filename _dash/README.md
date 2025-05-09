See https://dash.plotly.com/reference

```python
app = Dash(requests_pathname_prefix="/user/alice/") 
```

Leads to `http://127.0.0.1:4503/hub/user/alice/_dash-component-suites/dash/deps/polyfill@7.v3_0_2m1744645890.12.1.min.js`

```python
app = Dash(requests_pathname_prefix="/../user/alice/")
```

Leads to ``

```python
app = Dash(requests_pathname_prefix="/..", routes_pathname_prefix="/user/alice/")
```

Leads to 500

```python
app = Dash(routes_pathname_prefix="/user/alice/")
```

Leads to 500 

```
[I 250418 12:15:00 proxyhandlers:864] SuperviseAndProxyHandler http_get 8889 api
[I 250418 12:15:00 proxyhandlers:752] ['python', '/workspaces/dashboard/app.py', '--port', '8889']
[I 250418 12:15:04 proxyhandlers:795] b'Dash is running on http://0.0.0.0:8889/user/alice/\n'
```

```python
app = Dash(routes_pathname_prefix="/../user/alice/")
```

Leads to 500