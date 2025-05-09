from apphub_configurator.models import *
import yaml
from pathlib import Path
import os

storage_class_rwo = "standard"
workspace_volume_size = "10Gi"

node_selector = {}

current_dir = Path(os.path.dirname(os.path.realpath(__file__)))
parent_dir = current_dir.parent

profile_definition = {}

profile_definition["panel"] = {"display_name": "Panel", "description": "This profile is used to demonstrate a Panel dashboard (https://panel.holoviz.org/)", "image": os.environ.get("PANEL_IMAGE")}
profile_definition["streamlit"] = {"display_name": "Streamlit", "description": "This profile is used to demonstrate a Streamlit dashboard (https://streamlit.io/)", "image":  os.environ.get("STREAMLIT_IMAGE")}
profile_definition["taipy"] = {"display_name": "Taipy", "description": "This profile is used to demonstrate a Taipy dashboard (https://taipy.io/)", "image": os.environ.get("TAIPY_IMAGE")}
profile_definition["solara"] = {"display_name": "Solara", "description": "This profile is used to demonstrate a Solara dashboard (https://solara.dev/)", "image": os.environ.get("SOLARA_IMAGE")}

profiles = []

for key, value in profile_definition.items():
    print(value)
    # volumes
    workspace_volume = Volume(
        name="workspace-volume",
        size=workspace_volume_size,
        claim_name="workspace-claim",
        mount_path="/workspace",
        storage_class=storage_class_rwo,
        access_modes=["ReadWriteOnce"],
        volume_mount=VolumeMount(name="workspace-volume", mount_path="/workspace"),
        persist=True,
    )

    profiles.append(Profile(
        id=f"profile_dash",
        groups=["group-a", "group-b"],
        definition=ProfileDefinition(
            display_name=value["display_name"],
            description=value["description"],
            slug=f"profile_{value['display_name'].lower()}",
            default=False,
            kubespawner_override=KubespawnerOverride(
                cpu_guarantee=1,
                cpu_limit=2,
                mem_guarantee="1G",
                mem_limit="2G",
                image=value["image"],
            ),
        ),
        node_selector=node_selector,
        volumes=[workspace_volume],
        config_maps=[
        ],
        pod_env_vars={
            "HOME": "/workspace",
        },
        init_containers=[],
        manifests=[],
        env_from_config_maps=[],
        env_from_secrets=[],
        secret_mounts=[],
        image_pull_secrets=[],
    ))


config = Config(profiles=profiles)
config_file_path = str(Path(current_dir).parent / 'files' / 'hub' / 'config.yml')


with open(config_file_path, "w") as file:
    yaml.dump(config.model_dump(), file, width=200)
