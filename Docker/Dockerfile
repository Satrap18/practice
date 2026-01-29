FROM python:3.11-slim
WORKDIR /Docker
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY app.py .
CMD [ "python", "app.py" ]