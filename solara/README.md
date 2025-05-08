# Solara 

This is the README for supporting [Solara](https://solara.dev/) dashboards in the Application Hub.

## Developing a dashboard

Create a `app.py` file.

Include the dependencies in the `requirements.txt` file.

Build the container with:

```console
docker build . -t solara -f Dockerfile
```

Run the container with:

```console
docker run --rm -it -p 8765:8765 --entrypoint solara docker.io/library/solara run app.py --host=0.0.0.0
```

Open your browser on [http://127.0.0.1:8888](http://127.0.0.1:8888)

## Deployment in the Application Hub

Generate a profile with:

```python
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
```

## References:

See https://panel.holoviz.org/tutorials/basic/deploy.html

And https://panel.holoviz.org/tutorials/intermediate/serve.html