FROM python:3.8.5
WORKDIR /usr/src/app

COPY testapi.py .
COPY requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "./testapi.py"]