import panel as pn
import planetary_computer
import pystac_client
import datetime
import logging

import logging
import panel as pn

FORMAT = "%(asctime)s | %(levelname)s | %(name)s | %(message)s"

@pn.cache
def reconfig_basic_config(format_=FORMAT, level=logging.INFO):
    """(Re-)configure logging"""
    logging.basicConfig(format=format_, level=level, force=True)
    logging.info("Logging.basicConfig completed successfully")

reconfig_basic_config()
logger = logging.getLogger(name="app")

logger.info("Hello World")

logger.info("Starting Sentinel Feed Dashboard")

pn.extension()

ACCENT = "teal"

# Connect to STAC
catalog = pystac_client.Client.open("https://planetarycomputer.microsoft.com/api/stac/v1",
                                    modifier=planetary_computer.sign_inplace,)

# Extract
def get_latest_items(collection_id):
    """Fetch latest 10 items for a given collection."""
    logger.info(f"Fetching latest items for collection: {collection_id}")
    search = catalog.search(
        collections=[collection_id],
        sortby=[{"field": "datetime", "direction": "desc"}],
        limit=10,
        max_items=10, 
    )

    return [
        f"**{item.id}** {item.datetime.strftime('%Y-%m-%d %H:%M')}"
        for item in search.items()
    ]

# Views
s2a_list = pn.pane.Markdown("", sizing_mode="stretch_both")
s1_list = pn.pane.Markdown("", sizing_mode="stretch_both")

logger.info("Creating lists")

def update_lists():
    """Refresh both lists."""
    s2a_items = get_latest_items("sentinel-2-l2a")
    s1_items = get_latest_items("sentinel-1-grd")

    s2a_list.object = "### Sentinel-2 L2A (Latest 10)\n\n" + "\n\n".join(f"- {i}" for i in s2a_items)
    s1_list.object = "### Sentinel-1 GRD (Latest 10)\n\n" + "\n\n".join(f"- {i}" for i in s1_items)

# Initial update
logger.info("Updating lists")
update_lists()

# Layout and template
logger.info("Creating layout")
content = pn.FlexBox(s2a_list, s1_list)

pn.template.FastListTemplate(
    title="Panel - Live Sentinel Feed Dashboard",
    main=[content],
    accent=ACCENT,
    theme="dark",
    theme_toggle=False,
    meta_refresh="15"  # Refresh browser tab every 10 seconds (optional)
).servable()
