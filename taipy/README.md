# Taipy 

This is the README for supporting [Taipy](https://taipy.io/) dashboards in the Application Hub.

## Developing a dashboard

Create a `dashboard.py` file.

Include the dependencies in the `requirements.txt` file.

Build the container with:

```console
docker build . -t taipy -f Dockerfile
```

Run the container with:

```console
docker run --rm -it -p 8888:8888 docker.io/library/taipy --port 8888
```

Open your browser on [http://127.0.0.1:8888](http://127.0.0.1:8888)

## Deployment in the Application Hub

Generate a profile with:

```python
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

See https://docs.taipy.io/en/latest/

