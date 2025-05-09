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

# enable local development mode
if [ -z "$JUPYTERHUB_SERVICE_PREFIX" ]; then
    echo "JUPYTERHUB_SERVICE_PREFIX is not set, using default /"
    JUPYTERHUB_SERVICE_PREFIX="/"
fi


jhsingle-native-proxy --destport $destport --authtype none solara run app.py {--}port ${destport} {--}host=0.0.0.0 {--}root-path $JUPYTERHUB_SERVICE_PREFIX --port $port