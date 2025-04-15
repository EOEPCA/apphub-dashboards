FROM python:3.11-slim

RUN pip3 install \
    jhsingle-native-proxy>=0.0.9 \
    dash \
    numpy \
    pandas \
    plotly

# create a user, since we don't want to run as root
RUN useradd -m jovyan
ENV HOME=/home/jovyan
WORKDIR /workspaces


COPY --chown=jovyan:jovyan . /workspaces/dashboard

COPY --chown=jovyan:jovyan entrypoint.sh /workspaces

RUN chmod +x /workspaces/entrypoint.sh
USER jovyan

EXPOSE 8888

ENTRYPOINT ["/workspaces/entrypoint.sh"]

CMD ["jhsingle-native-proxy", "--destport", "8050", "python", "/workspaces/dashboard/app.py"]