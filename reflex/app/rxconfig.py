import os
import reflex as rx

config = rx.Config(
    app_name="app",
   # deploy_url=os.getenv("JUPYTERHUB_SERVICE_PREFIX", "/"),
)