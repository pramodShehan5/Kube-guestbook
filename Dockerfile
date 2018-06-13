FROM python:2.7-onbuild

ENV BIND_PORT 5000

COPY ./requirements.txt /requirements.txt
COPY ./app.py /app.py

RUN pip install --upgrade pip -r /requirements.txt

EXPOSE $BIND_PORT

CMD ["python", "/app.py"]

