from apphub_configurator.models import *
import yaml
from pathlib import Path
import os
from loguru import logger
from apphub_configurator.helpers import (
    load_config_map,
    load_manifests,
    create_init_container,
    load_init_script,
)

storage_class_rwo = "standard"
storage_class_rwx = "standard"
profiles = []
workspace_volume_size = "10Gi"

image = "eoepca/pde-code-server:develop"
node_selector = {}

# get the current directory
current_dir = Path(os.path.dirname(os.path.realpath(__file__)))
parent_dir = current_dir.parent

dash_image = os.environ.get("DASH_IMAGE")
reflex_image = os.environ.get("REFLEX_IMAGE")
streamlit_image = os.environ.get("STREAMLIT_IMAGE")
nicegui_image = os.environ.get("NICEGUI_IMAGE")
taipy_image = os.environ.get("TAIPY_IMAGE")
panel_image = os.environ.get("PANEL_IMAGE")
solara_image = os.environ.get("SOLARA_IMAGE")

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

profile_dash = Profile(
    id=f"profile_dash",
    groups=["group-a", "group-b"],
    definition=ProfileDefinition(
        display_name="Dash - work in progress",
        description="This profile is used to demonstrate a Dash Plotty dashboard (https://dash.plotly.com/)",
        slug="profile_dash",
        default=False,
        kubespawner_override=KubespawnerOverride(
            cpu_guarantee=1,
            cpu_limit=2,
            mem_guarantee="4G",
            mem_limit="6G",
            image=dash_image,
        ),
    ),
    node_selector=node_selector,
    volumes=[workspace_volume],
    config_maps=[
    ],
    pod_env_vars={
        "HOME": "/workspace",
        "CONDA_ENVS_PATH": "/workspace/.envs",
        "CONDARC": "/workspace/.condarc",
        "XDG_RUNTIME_DIR": "/workspace/.local",
        "CODE_SERVER_WS": "/workspace/mastering-app-package",
    },
    init_containers=[],
    manifests=[],
    env_from_config_maps=[],
    env_from_secrets=[],
    secret_mounts=[],
    image_pull_secrets=[],
)

profile_streamlit = Profile(
    id=f"profile_streamlit",
    groups=["group-a", "group-b"],
    definition=ProfileDefinition(
        display_name="Streamlit",
        description="This profile is used to demonstrate a Streamlit dashboard (https://streamlit.io/)",
        slug="profile_streamlit",
        default=False,
        kubespawner_override=KubespawnerOverride(
            cpu_guarantee=1,
            cpu_limit=2,
            mem_guarantee="4G",
            mem_limit="6G",
            image=streamlit_image,
        ),
    ),
    node_selector=node_selector,
    volumes=[workspace_volume],
    config_maps=[
    ],
    pod_env_vars={
        "HOME": "/workspace",
        "CONDA_ENVS_PATH": "/workspace/.envs",
        "CONDARC": "/workspace/.condarc",
        "XDG_RUNTIME_DIR": "/workspace/.local",
        "CODE_SERVER_WS": "/workspace/mastering-app-package",
    },
    init_containers=[],
    manifests=[],
    env_from_config_maps=[],
    env_from_secrets=[],
    secret_mounts=[],
    image_pull_secrets=[],
)

profile_reflex = Profile(
    id=f"profile_reflex",
    groups=["group-a", "group-b"],
    definition=ProfileDefinition(
        display_name="Reflex",
        description="This profile is used to demonstrate a Reflex dashboard (https://reflex.dev/)",
        slug="profile_reflex",
        default=False,
        kubespawner_override=KubespawnerOverride(
            cpu_guarantee=1,
            cpu_limit=2,
            mem_guarantee="4G",
            mem_limit="6G",
            image=reflex_image,
        ),
    ),
    node_selector=node_selector,
    volumes=[workspace_volume],
    config_maps=[
    ],
    pod_env_vars={
        "HOME": "/workspace",
        "CONDA_ENVS_PATH": "/workspace/.envs",
        "CONDARC": "/workspace/.condarc",
        "XDG_RUNTIME_DIR": "/workspace/.local",
        "CODE_SERVER_WS": "/workspace/mastering-app-package",
    },
    init_containers=[],
    manifests=[],
    env_from_config_maps=[],
    env_from_secrets=[],
    secret_mounts=[],
    image_pull_secrets=[],
)

profile_nicegui = Profile(
    id=f"profile_nicegui",
    groups=["group-a", "group-b"],
    definition=ProfileDefinition(
        display_name="Nicegui - work in Progress",
        description="This profile is used to demonstrate a Nicegui dashboard (https://nicegui.io/)",
        slug="profile_nicegui",
        default=False,
        kubespawner_override=KubespawnerOverride(
            cpu_guarantee=1,
            cpu_limit=2,
            mem_guarantee="4G",
            mem_limit="6G",
            image=nicegui_image,
        ),
    ),
    node_selector=node_selector,
    volumes=[workspace_volume],
    config_maps=[
    ],
    pod_env_vars={
        "HOME": "/workspace",
        "CONDA_ENVS_PATH": "/workspace/.envs",
        "CONDARC": "/workspace/.condarc",
        "XDG_RUNTIME_DIR": "/workspace/.local",
        "CODE_SERVER_WS": "/workspace/mastering-app-package",
    },
    init_containers=[],
    manifests=[],
    env_from_config_maps=[],
    env_from_secrets=[],
    secret_mounts=[],
    image_pull_secrets=[],
)

profile_taipy = Profile(
    id=f"profile_taipy",
    groups=["group-a", "group-b"],
    definition=ProfileDefinition(
        display_name="Taipy",
        description="This profile is used to demonstrate a Taipy dashboard (https://taipy.io/)",
        slug="profile_taipy",
        default=False,
        kubespawner_override=KubespawnerOverride(
            cpu_guarantee=1,
            cpu_limit=2,
            mem_guarantee="4G",
            mem_limit="6G",
            image=taipy_image,
        ),
    ),
    node_selector=node_selector,
    volumes=[workspace_volume],
    config_maps=[
    ],
    pod_env_vars={
        "HOME": "/workspace",
        "CONDA_ENVS_PATH": "/workspace/.envs",
        "CONDARC": "/workspace/.condarc",
        "XDG_RUNTIME_DIR": "/workspace/.local",
        "CODE_SERVER_WS": "/workspace/mastering-app-package",
    },
    init_containers=[],
    manifests=[],
    env_from_config_maps=[],
    env_from_secrets=[],
    secret_mounts=[],
    image_pull_secrets=[],
)

profile_panel = Profile(
    id=f"profile_panel",
    groups=["group-a", "group-b"],
    definition=ProfileDefinition(
        display_name="Panel",
        description="This profile is used to demonstrate a Panel dashboard (https://panel.holoviz.org/)",
        slug="profile_panel",
        default=False,
        kubespawner_override=KubespawnerOverride(
            cpu_guarantee=1,
            cpu_limit=2,
            mem_guarantee="4G",
            mem_limit="6G",
            image=panel_image,
        ),
    ),
    node_selector=node_selector,
    volumes=[workspace_volume],
    config_maps=[
    ],
    pod_env_vars={
        "HOME": "/workspace",
        "CONDA_ENVS_PATH": "/workspace/.envs",
        "CONDARC": "/workspace/.condarc",
        "XDG_RUNTIME_DIR": "/workspace/.local",
        "CODE_SERVER_WS": "/workspace/mastering-app-package",
    },
    init_containers=[],
    manifests=[],
    env_from_config_maps=[],
    env_from_secrets=[],
    secret_mounts=[],
    image_pull_secrets=[],
)

profile_solara = Profile(
    id=f"profile_solara",
    groups=["group-a", "group-b"],
    definition=ProfileDefinition(
        display_name="Solara",
        description="This profile is used to demonstrate a Solara dashboard (https://solara.dev/)",
        slug="profile_solara",
        default=False,
        kubespawner_override=KubespawnerOverride(
            cpu_guarantee=1,
            cpu_limit=2,
            mem_guarantee="4G",
            mem_limit="6G",
            image=solara_image,
        ),
    ),
    node_selector=node_selector,
    volumes=[workspace_volume],
    config_maps=[
    ],
    pod_env_vars={
        "HOME": "/workspace",
        "CONDA_ENVS_PATH": "/workspace/.envs",
        "CONDARC": "/workspace/.condarc",
        "XDG_RUNTIME_DIR": "/workspace/.local",
        "CODE_SERVER_WS": "/workspace/mastering-app-package",
    },
    init_containers=[],
    manifests=[],
    env_from_config_maps=[],
    env_from_secrets=[],
    secret_mounts=[],
    image_pull_secrets=[],
)

profile_1 = Profile(
    id=f"profile_1",
    groups=["group-a", "group-b"],
    definition=ProfileDefinition(
        display_name="Coder demo init script",
        description="This profile is used to demonstrate the use of an init script",
        slug="profile_1",
        default=False,
        kubespawner_override=KubespawnerOverride(
            cpu_guarantee=1,
            cpu_limit=2,
            mem_guarantee="4G",
            mem_limit="6G",
            image=image,
        ),
    ),
    node_selector=node_selector,
    volumes=[workspace_volume],
    config_maps=[
    ],
    pod_env_vars={
        "HOME": "/workspace",
        "CONDA_ENVS_PATH": "/workspace/.envs",
        "CONDARC": "/workspace/.condarc",
        "XDG_RUNTIME_DIR": "/workspace/.local",
        "CODE_SERVER_WS": "/workspace/mastering-app-package",
    },
    init_containers=[],
    manifests=[],
    env_from_config_maps=[],
    env_from_secrets=[],
    secret_mounts=[],
    image_pull_secrets=[],
)




profiles.append(profile_1)
profiles.append(profile_dash)
profiles.append(profile_streamlit)
profiles.append(profile_reflex)
profiles.append(profile_nicegui)
profiles.append(profile_taipy)
profiles.append(profile_panel)
profiles.append(profile_solara)

config = Config(profiles=profiles)
config_file_path = str(Path(current_dir).parent / 'files' / 'hub' / 'config.yml')


with open(config_file_path, "w") as file:
    yaml.dump(config.model_dump(), file, width=200)
