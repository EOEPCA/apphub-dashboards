FROM python:3.11-slim

COPY requirements.txt /tmp/requirements.txt

RUN pip3 install -r /tmp/requirements.txt

# create a user, since we don't want to run as root
RUN useradd -m jovyan
ENV HOME=/home/jovyan
WORKDIR /workspaces


COPY --chown=jovyan:jovyan . /workspaces/

COPY --chown=jovyan:jovyan entrypoint.sh /workspaces

RUN chmod +x /workspaces/entrypoint.sh
USER jovyan

EXPOSE 8888

ENTRYPOINT ["/workspaces/entrypoint.sh"]
