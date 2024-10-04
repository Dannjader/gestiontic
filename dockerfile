FROM python:3.11-alpine3.18

ENV PYTHONUMBUFFERED=1

WORKDIR /gestiontic_app

RUN pip install --upgrade pip

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt


EXPOSE 8000

CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]