FROM python:3.13.3-alpine

COPY ./requirements.txt .
RUN pip install --no-cache-dir -r ./requirements.txt

COPY ./src /src

CMD ["python", "/src/app.py"]