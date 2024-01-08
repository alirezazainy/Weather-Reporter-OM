FROM python:latest

COPY requirements.txt /src/

WORKDIR /src

RUN pip install -U pip
RUN pip install -r requirements.txt

COPY . /src/

EXPOSE 8000

CMD [ "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000" ]
