FROM python:latest

RUN python3 -V

COPY ./ ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

WORKDIR /app

CMD ["python", "__main__.py"]