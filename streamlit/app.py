import streamlit as st
import pystac_client
import planetary_computer
import datetime
import time
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("streamlit_app")

# STAC client (signed)
catalog = pystac_client.Client.open(
    "https://planetarycomputer.microsoft.com/api/stac/v1",
    modifier=planetary_computer.sign_inplace,
)

# Fetch latest items from a collection
def get_latest_items(collection_id):
    logger.info(f"Fetching items for {collection_id}")
    search = catalog.search(
        collections=[collection_id],
        sortby=[{"field": "datetime", "direction": "desc"}],
        limit=10,
        max_items=10,
    )
    return [
        {
            "id": item.id,
            "datetime": item.datetime.strftime("%Y-%m-%d %H:%M"),
        }
        for item in search.items()
    ]

# Layout
st.set_page_config(page_title="Sentinel Feed Dashboard", layout="wide")
st.title("🛰️ Live Sentinel Feed Dashboard")

col1, col2 = st.columns(2)

# Sentinel-2 L2A
with col1:
    st.subheader("Sentinel-2 L2A (Latest 10)")
    for item in get_latest_items("sentinel-2-l2a"):
        st.markdown(
            f"""
            <div style="padding: 0.5em; border-left: 4px solid #0d9488; background: #f0fdfa; margin-bottom: 0.5em;">
                <div style="font-weight: bold; color: #0f766e;">🛰️ {item['id']}</div>
                <div style="font-size: 0.9em; color: #334155;">📅 {item['datetime']}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

# Sentinel-1 GRD
with col2:
    st.subheader("Sentinel-1 GRD (Latest 10)")
    for item in get_latest_items("sentinel-1-grd"):
        st.markdown(
            f"""
            <div style="padding: 0.5em; border-left: 4px solid #3b82f6; background: #eff6ff; margin-bottom: 0.5em;">
                <div style="font-weight: bold; color: #1e40af;">🛰️ {item['id']}</div>
                <div style="font-size: 0.9em; color: #334155;">📅 {item['datetime']}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

# Auto-refresh
st.markdown("---")
col_left, col_right = st.columns([3, 1])
with col_left:
    st.info("This page refreshes every 15 seconds. Click below to force an update.")
with col_right:
    if st.button("🔄 Refresh Now"):
        st.rerun()

# Delay + rerun (auto-refresh)
time.sleep(15)
st.rerun()
