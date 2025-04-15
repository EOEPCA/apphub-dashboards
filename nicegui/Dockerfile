FROM zauberzeug/nicegui:latest

COPY app /app
COPY requirements.txt /app/requirements.txt
RUN pip install --upgrade pip setuptools wheel
RUN pip3 install wheel 
RUN pip3 install -r /app/requirements.txt

COPY entrypoint.sh /app
RUN chmod +x /app/entrypoint.sh
ENTRYPOINT ["/app/entrypoint.sh"]