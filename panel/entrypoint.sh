#!/bin/bash

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

echo "Running entrypoint.sh with port $port"

# enable local development mode
if [ -z "$JUPYTERHUB_SERVICE_PREFIX" ]; then
    echo "JUPYTERHUB_SERVICE_PREFIX is not set, using default /"
    JUPYTERHUB_SERVICE_PREFIX="/"
fi

jhsingle-native-proxy --destport $destport --authtype none panel serve /code/dashboard.py {--}log-level info {--}address 0.0.0.0 {--}allow-websocket-origin='*' {--}root-path $JUPYTERHUB_SERVICE_PREFIX {--}port $destport {--}num-procs 1 {--}num-threads 0 {--}session-token-expiration=900000 --port $port

