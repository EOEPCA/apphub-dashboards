#exit 0

set -x

export PYTHONPATH=$PWD/`dirname $0`/.

export STREAMLIT_IMAGE=ghcr.io/eoepca/apphub-dashboards/streamlit:0.2.0
export TAIPY_IMAGE=ghcr.io/eoepca/apphub-dashboards/taipy:0.2.0
export PANEL_IMAGE=ghcr.io/eoepca/apphub-dashboards/panel:0.2.0
export SOLARA_IMAGE=ghcr.io/eoepca/apphub-dashboards/solara:0.2.0

.env/bin/python -m generate_config 