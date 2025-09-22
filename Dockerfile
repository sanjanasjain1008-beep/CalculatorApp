FROM python:3.12-slim
WORKDIR /app
COPY calculator.py /app/
# If you decide to have dependencies, also copy requirements.txt and install
ENTRYPOINT ["python", "calculator.py"]
