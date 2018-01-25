FROM python:3
COPY requirements.txt .
RUN pip install -r requirements.txt && rm -rf /root/.cache
WORKDIR /app
COPY . /app
CMD ["python", "example_pandas.py"]
