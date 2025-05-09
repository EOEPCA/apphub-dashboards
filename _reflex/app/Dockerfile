# This Dockerfile is used to deploy a single-container Reflex app instance
# to services like Render, Railway, Heroku, GCP, and others.

# It uses a reverse proxy to serve the frontend statically and proxy to backend
# from a single exposed port, expecting TLS termination to be handled at the
# edge by the given platform.
FROM python:3.13

# If the service expects a different port, provide it here (f.e Render expects port 10000)
ARG PORT=8888
# Only set for local/direct access. When TLS is used, the API_URL is assumed to be the same as the frontend.
ARG API_URL
ENV PORT=$PORT API_URL=${API_URL:-http://localhost:$PORT} REDIS_URL=redis://localhost PYTHONUNBUFFERED=1

# Install Caddy and redis server inside image
RUN apt-get update -y && apt-get install -y caddy redis-server && rm -rf /var/lib/apt/lists/*
#RUN groupadd -g 0 jovyan
RUN useradd -m jovyan -u 1001 -g 0
ENV HOME=/home/jovyan
WORKDIR /app

# Copy local context to `/app` inside container (see .dockerignore)
COPY --chown=jovyan:0 . .

# Install app requirements and reflex in the container
COPY requirements.txt ./
RUN pip install -r requirements.txt

# Deploy templates and prepare app
#RUN reflex init

# Download all npm dependencies and compile frontend
#RUN reflex export --frontend-only --no-zip && mv .web/_static/* /srv/ && rm -rf .web

# Needed until Reflex properly passes SIGTERM on backend.
STOPSIGNAL SIGKILL

EXPOSE $PORT

# Apply migrations before starting the backend.
# CMD [ -d alembic ] && reflex db migrate; \
#     caddy start && \
#     redis-server --daemonize yes && \
#     exec reflex run --env prod --backend-only

COPY --chown=jovyan:0 entrypoint.sh /app
RUN chmod +x /app/entrypoint.sh
ENTRYPOINT ["/app/entrypoint.sh"]
RUN chown -R jovyan:0 /app && chown -R jovyan:0 /srv 

#CMD ["jhsingle-native-proxy", "--destport", "8505", "reflex", "run",  "{--}env", "prod", "{--}backend-only", "--port", "8888"]

