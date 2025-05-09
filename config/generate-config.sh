#exit 0

set -x

export PYTHONPATH=$PWD/`dirname $0`/.

export STREAMLIT_IMAGE=ttl.sh/streamlit-app:$( minikube ssh -- docker inspect ttl.sh/streamlit-app:5m | jq -r .[0].Id | cut -d: -f2 )
export TAIPY_IMAGE=ttl.sh/taipy-app:$( minikube ssh -- docker inspect ttl.sh/taipy-app:5m | jq -r .[0].Id | cut -d: -f2 )
export PANEL_IMAGE=ttl.sh/panel-app:$( minikube ssh -- docker inspect ttl.sh/panel-app:5m | jq -r .[0].Id | cut -d: -f2 )
export SOLARA_IMAGE=ttl.sh/solara-app:$( minikube ssh -- docker inspect ttl.sh/solara-app:5m | jq -r .[0].Id | cut -d: -f2 )

.env/bin/python -m generate_config 