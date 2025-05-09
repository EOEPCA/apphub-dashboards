# Application Hub Dashboards

This repo contains examples of dashboards that can be hosted by the Application Hub

## For developers

Create a Python environment with the Application Hub configuration helpers:

```
python -m venv .env
source .env/bin/activate
pip install -r requirements.txt
```

Use skaffold to deploy the Application Hub on minikube:

```
skaffold dev
```

Open your browser on [http://127.0.0.1:8080](http://127.0.0.1:8080)

Log as user `alice` without a password.

Start a profile to launch a dashboard.

Note: If you see the message "Pending configuration", wait a few seconds and refresh the page until the profiles are displayed