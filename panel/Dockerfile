FROM python:3.11

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt
RUN python3 -m pip install --no-cache-dir --upgrade pip
RUN python3 -m pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY . .

#CMD ["panel", "serve", "/code/app.py", "--address", "0.0.0.0", "--port", "7860",  "--allow-websocket-origin", "*", "--num-procs", "2", "--num-threads", "0", "--index", "app"]
COPY  entrypoint.sh /code

RUN chmod +x /code/entrypoint.sh
EXPOSE 8888

ENTRYPOINT ["/code/entrypoint.sh"]

RUN mkdir /.cache
RUN chmod 777 /.cache