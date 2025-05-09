import reflex as rx
import pystac_client
import planetary_computer
import asyncio
import logging

# Logging configuration
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("reflex_app")

# STAC client with signed URLs
catalog = pystac_client.Client.open(
    "https://planetarycomputer.microsoft.com/api/stac/v1",
    modifier=planetary_computer.sign_inplace,
)

# Reactive state
class State(rx.State):
    s2a_text: str = "Loading Sentinel-2 L2A..."
    s1_text: str = "Loading Sentinel-1 GRD..."
    initialized: bool = False

    async def load_and_start(self):
        if self.initialized:
            return
        await self.refresh_data()
        self.initialized = True
        asyncio.create_task(self.auto_refresh())

    async def refresh_data(self):
        def fetch_latest(collection_id):
            logger.info(f"Fetching items for {collection_id}")
            search = catalog.search(
                collections=[collection_id],
                sortby=[{"field": "datetime", "direction": "desc"}],
                limit=10,
                max_items=10,
            )
            return [
                {"id": item.id, "datetime": item.datetime.strftime("%Y-%m-%d %H:%M")}
                for item in search.items()
            ]

        s2a_list = fetch_latest("sentinel-2-l2a")
        s1_list = fetch_latest("sentinel-1-grd")

        self.s2a_text = (
            "<h3 style='margin-bottom: 0.5em;'>Sentinel-2 L2A (Latest 10)</h3>"
            + "".join(
                f"""
                <div style='margin-bottom: 0.75em; padding: 0.5em; border-left: 4px solid #0d9488; background: #f0fdfa;'>
                    <div style='font-weight: 600; color: #0f766e;'>🛰️ {item["id"]}</div>
                    <div style='font-size: 0.9em; color: #334155;'>📅 {item["datetime"]}</div>
                </div>
                """
                for item in s2a_list
            )
        )

        self.s1_text = (
            "<h3 style='margin-bottom: 0.5em;'>Sentinel-1 GRD (Latest 10)</h3>"
            + "".join(
                f"""
                <div style='margin-bottom: 0.75em; padding: 0.5em; border-left: 4px solid #3b82f6; background: #eff6ff;'>
                    <div style='font-weight: 600; color: #1e40af;'>🛰️ {item["id"]}</div>
                    <div style='font-size: 0.9em; color: #334155;'>📅 {item["datetime"]}</div>
                </div>
                """
                for item in s1_list
            )
        )

    async def auto_refresh(self):
        while True:
            logger.info("Auto-refreshing feed...")
            await self.refresh_data()
            await asyncio.sleep(15)

# Page layout
@rx.page(title="Sentinel Dashboard")
def index():
    return rx.fragment(
        rx.vstack(
            rx.heading("🛰️ Live Sentinel Feed Dashboard", size="4"),
            rx.button("Refresh Now", on_click=State.refresh_data, color="teal", size="4"),
            rx.hstack(
                rx.html(State.s2a_text),
                rx.html(State.s1_text),
                spacing="8",
                align="start",
                wrap="wrap",
            ),
            spacing="6",
            padding="4",
        ),
        # Trigger auto-load only once
        rx.cond(
            ~State.initialized,
            rx.button("Init", on_click=State.load_and_start, display="none"),
        ),
    )

# App entry
app = rx.App()
