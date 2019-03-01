FROM python:3-slim
WORKDIR /app
COPY requirements.txt /app
RUN pip install -r requirements.txt --no-cache
COPY . /app
CMD ["python", "example_pandas.py"]
