import os
import reflex as rx

config = rx.Config(
    app_name="app",
    frontend_path=os.environ.get("JUPYTERHUB_SERVICE_PREFIX").rstrip('/'),
)