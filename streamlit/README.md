
docker build . -t streamlit

docker run --rm -p 8888:8888  docker.io/library/streamlit


On JupyterHub the log shows:

```
/bin/sh
-c
["jhsingle-native-proxy", "--destport", "8505", "streamlit", "run" "/workspaces/dashboard/app.py", "{--}server.port", "{port}", "{--}server.headless", "True", "{--}server.enableCORS", "False", "--port", "8888"]
Using internal port 8889
[I 250415 10:32:47 proxyhandlers:864] SuperviseAndProxyHandler http_get 8889 api
[I 250415 10:32:47 proxyhandlers:752] ['streamlit', 'run', '/workspaces/dashboard/app.py', '--server.port', '8889', '--server.headless', 'True', '--server.enableCORS', 'False']
```

Not using `CMD` as it was removed