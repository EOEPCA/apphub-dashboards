#!/bin/bash
set -x
collect_port=0
port="8888"
delim='='

for var in "$@"
do
    echo "$var"

    if [ "$collect_port" == "1" ]; then
       echo "Collecting external port $var"
       port=$var
       collect_port=0
    fi

    splitarg=${var%%$delim*}

    if [ "$splitarg" == "--port" ]; then
       if [ ${#splitarg} == ${#var} ]; then
         collect_port=1
       else
         port=${var#*$delim}
         echo "Setting external port $port"
       fi
    fi
done

destport=$((port + 1))

echo "Using internal port $destport"
# env 
# cd /app
# reflex export --frontend-only --no-zip && mv .web/_static/* /srv/ && rm -rf .web
# mv .web/_static/* /srv/ && rm -rf .web
# cd -
export PORT=$destport
export API_URL=${API_URL:-http://localhost:$PORT}
export REDIS_URL=redis://localhost

redis-server --daemonize yes 

exec reflex run --env prod --backend-only &

#PORT=$PORT API_URL=${API_URL:-http://localhost:$PORT}

jhsingle-native-proxy --destport $destport --authtype none caddy start --port $port
