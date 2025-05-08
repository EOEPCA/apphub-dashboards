import solara
import pystac_client
import planetary_computer
from datetime import datetime
import asyncio

# Connect to the Planetary Computer STAC API with signing
catalog = pystac_client.Client.open(
    "https://planetarycomputer.microsoft.com/api/stac/v1",
    modifier=planetary_computer.sign_inplace,
)

# Reactive state variables
s2a_items = solara.reactive([])
s1_items = solara.reactive([])
last_updated = solara.reactive(datetime.now())
auto_refresh_enabled = solara.reactive(True)

async def refresh_data():
    def get_latest_items(collection_id):
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

    s2a_items.set(get_latest_items("sentinel-2-l2a"))
    s1_items.set(get_latest_items("sentinel-1-grd"))
    last_updated.set(datetime.now())

# Initial fetch
@solara.component
def AutoRefresh():
    async def _loop():
        while True:
            if auto_refresh_enabled.value:
                await refresh_data()
            await asyncio.sleep(15)

    solara.use_thread(_loop)
    return solara.Text("")

# Card renderer
@solara.component
def ItemCard(item, accent_color="#0d9488", bg_color="#f0fdfa"):
    return solara.Card(
        children=[
            solara.Markdown(f"**🛰️ {item['id']}**", style={"color": accent_color}),
            solara.Text(f"📅 {item['datetime']}", style={"color": "#334155", "fontSize": "0.9em"}),
        ],
        style={
            "borderLeft": f"4px solid {accent_color}",
            "background": bg_color,
            "padding": "0.5em",
            "marginBottom": "0.5em",
        },
    )

# Page layout
@solara.component
def Page():
    AutoRefresh()

    with solara.Column():
        solara.Title("🛰️ Sentinel Feed Dashboard")

        with solara.Columns([1, 1]):
            with solara.Card("Sentinel-2 L2A (Latest 10)"):
                for item in s2a_items.value:
                    ItemCard(item, accent_color="#0d9488", bg_color="#f0fdfa")

            with solara.Card("Sentinel-1 GRD (Latest 10)"):
                for item in s1_items.value:
                    ItemCard(item, accent_color="#3b82f6", bg_color="#eff6ff")

        with solara.Columns([3, 1]):
            solara.Text(f"Last updated: {last_updated.value.strftime('%H:%M:%S')}")
            solara.Button("🔄 Refresh Now", on_click=lambda: asyncio.create_task(refresh_data()))

        solara.Switch(
            value=auto_refresh_enabled,
            on_value=auto_refresh_enabled.set,
            label="Auto Refresh (15s)"
        )
