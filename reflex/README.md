
Inspired from https://github.com/reflex-dev/reflex/blob/main/docker-example/simple-one-port/

In folder `reflex/app`, build the container with:

```
docker build . -t reflex-app
```

Then run:

```
docker run --rm -it -p 8080:8080 docker.io/library/reflex-app 
```

Open the browser on localhost:8080

The container logs:

```
Using internal port 8081
Setting pretty logging
Starting jhsingle-native-proxy server on address None port 8080, proxying to port 8081
URL Prefix: 
Auth Type: none
Command: ('caddy', 'start')
The following env vars are required to report activity back to the hub for keep alive: JUPYTERHUB_ACTIVITY_URL (), JUPYTERHUB_SERVER_NAME()
───────────────────────────────────────────────────────────────────────────────────────────────── Starting Reflex App ─────────────────────────────────────────────────────────────────────────────────────────────────
Warning: Your version (0.7.6) of reflex is out of date. Upgrade to 0.7.7 with 'pip install reflex --upgrade'
Backend running at: http://0.0.0.0:8000
[I 250415 12:47:13 proxyhandlers:864] SuperviseAndProxyHandler http_get 8081 _static/out/browser/serviceWorker.js
[I 250415 12:47:13 proxyhandlers:752] ['caddy', 'start']
[E 250415 12:47:13 proxyhandlers:797] b'{"level":"info","ts":1744721233.06677,"msg":"using adjacent Caddyfile"}\n'
[E 250415 12:47:13 proxyhandlers:797] b'{"level":"warn","ts":1744721233.0686495,"msg":"Caddyfile input is not formatted; run the \'caddy fmt\' command to fix inconsistencies","adapter":"caddyfile","file":"Caddyfile","line":14}\n'
[E 250415 12:47:13 proxyhandlers:797] b'{"level":"info","ts":1744721233.069408,"logger":"admin","msg":"admin endpoint started","address":"localhost:2019","enforce_origin":false,"origins":["//localhost:2019","//[::1]:2019","//127.0.0.1:2019"]}\n'
[E 250415 12:47:13 proxyhandlers:797] b'{"level":"info","ts":1744721233.0695984,"logger":"tls.cache.maintenance","msg":"started background certificate maintenance","cache":"0xc000032cb0"}\n'
[E 250415 12:47:13 proxyhandlers:797] b'{"level":"info","ts":1744721233.0698352,"logger":"http.log","msg":"server running","name":"srv0","protocols":["h1","h2","h3"]}\n'
[E 250415 12:47:13 proxyhandlers:797] b'{"level":"info","ts":1744721233.0698981,"logger":"tls","msg":"cleaning storage unit","description":"FileStorage:/home/jovyan/.local/share/caddy"}\n'
[E 250415 12:47:13 proxyhandlers:797] b'{"level":"info","ts":1744721233.0699449,"logger":"tls","msg":"finished cleaning storage units"}\n'
[E 250415 12:47:13 proxyhandlers:797] b'{"level":"info","ts":1744721233.07127,"msg":"autosaved config (load with --resume flag)","file":"/home/jovyan/.config/caddy/autosave.json"}\n'
[E 250415 12:47:13 proxyhandlers:797] b'{"level":"info","ts":1744721233.071278,"msg":"serving initial configuration"}\n'
[I 250415 12:47:13 proxyhandlers:795] b'Successfully started Caddy (pid=32) - Caddy is running in the background\n'
```