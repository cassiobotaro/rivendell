FROM python:3-alpine as builder
RUN apk add --update build-base
COPY requirements.txt .
RUN pip install -r requirements.txt


FROM python:3-alpine
# required by pandas
RUN apk add --update libstdc++
COPY --from=builder /root/.cache /root/.cache
COPY --from=builder requirements.txt .
RUN pip install -r requirements.txt && rm -rf /root/.cache
WORKDIR /app
COPY . /app
CMD ["python", "example_pandas.py"]
