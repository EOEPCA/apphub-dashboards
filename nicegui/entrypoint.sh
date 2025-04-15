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
export PORT=$destport
echo "Using internal port $destport"

echo "Running entrypoint.sh with port $port"

export STORAGE_SECRET="asasfasasfa"
cd /app
jhsingle-native-proxy --destport $destport --authtype none python3 main.py --port $port