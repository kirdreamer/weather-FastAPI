FROM python:3.12

WORKDIR /app

RUN python -m pip install --upgrade pip

COPY requirements.txt /app

RUN pip install -r requirements.txt

COPY . /app

CMD [ "uvicorn", "main:app", "--reload", "--host", "0.0.0.0"]