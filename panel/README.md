# Panel 

This is the README for supporting [Panel](https://panel.holoviz.org/) dashboards in the Application Hub.

## Developing a dashboard

Create a `dashboard.py` file.

Include the dependencies in the `requirements.txt` file.

Build the container with:

```console
docker build . -t panel -f Dockerfile
```

Run the container with:

```console
docker run --rm -it -p 8888:8888 --entrypoint panel docker.io/library/panel serve /code/dashboard.py --port 8888
```

Open your browser on [http://127.0.0.1:8888](http://127.0.0.1:8888)

## Deployment in the Application Hub

Generate a profile with:

```python
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
    config_maps=[],
    pod_env_vars={},
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