import os
import time
import logging
import threading
from taipy.gui import Gui
import taipy.gui.builder as tgb
import pystac_client
import planetary_computer

# Logging setup
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("taipy_app")

# STAC client setup
catalog = pystac_client.Client.open(
    "https://planetarycomputer.microsoft.com/api/stac/v1",
    modifier=planetary_computer.sign_inplace,
)

# Shared state
s2a_md = "Loading Sentinel-2..."
s1_md = "Loading Sentinel-1..."

def get_latest_items(collection_id):
    logger.info(f"Fetching latest items for {collection_id}")
    search = catalog.search(
        collections=[collection_id],
        sortby=[{"field": "datetime", "direction": "desc"}],
        limit=10,
        max_items=10
    )
    return [
        f"**{item.id}** — {item.datetime.strftime('%Y-%m-%d %H:%M')}"
        for item in search.items()
    ]

def update_data(state=None):
    global s2a_md, s1_md
    s2a_items = get_latest_items("sentinel-2-l2a")
    s1_items = get_latest_items("sentinel-1-grd")

    s2a_md = "### Sentinel-2 L2A (Latest 10)\n\n" + "\n\n".join(f"- {item}" for item in s2a_items)
    s1_md = "### Sentinel-1 GRD (Latest 10)\n\n" + "\n\n".join(f"- {item}" for item in s1_items)

# Initial fetch
update_data()

# Build dashboard page with Builder API
with tgb.Page() as page:
    tgb.text("# Taipy - Live Sentinel Feed Dashboard", mode="md")
    with tgb.layout(columns="1 1", gap="30px"):
        tgb.text("{s2a_md}", mode="md")
        tgb.text("{s1_md}", mode="md")
    tgb.button("Refresh", on_action=update_data)

# Background refresh thread
def run_with_refresh():
    while True:
        update_data()
        time.sleep(15)

threading.Thread(target=run_with_refresh, daemon=True).start()

# Start the GUI
Gui(page=page).run(
    base_url=os.environ.get("JUPYTERHUB_SERVICE_PREFIX"),
    title="Taipy Sentinel Feed Dashboard",
    dark_mode=True
)
