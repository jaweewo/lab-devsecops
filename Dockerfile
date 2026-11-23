FROM python:3.14.10-alpine3.24

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY app.py .

RUN adduser -D appuser
USER appuser

ENV FLASK_HOST=0.0.0.0
EXPOSE 5000
CMD ["python", "app.py"]