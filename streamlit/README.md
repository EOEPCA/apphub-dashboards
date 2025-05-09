# Streamlit 

This is the README for supporting [Streamlit](https://streamlit.io/) dashboards in the Application Hub.

## Developing a dashboard

Create a `dashboard.py` file.

Include the dependencies in the `requirements.txt` file.

Build the container with:

```console
docker build . -t streamlit -f Dockerfile
```

Run the container with:

```console
docker run --rm -it -p 8888:8888 docker.io/library/streamlit --port 8888
```

Open your browser on [http://127.0.0.1:8888](http://127.0.0.1:8888)

## Deployment in the Application Hub

Generate a profile with:

```python
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

See https://streamlit.io/

