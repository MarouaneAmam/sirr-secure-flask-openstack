FROM python:3.12-slim
RUN useradd -m -u 10001 appuser
WORKDIR /app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY app/ ./app/
USER appuser
EXPOSE 8000
ENV APP_ENV=dev
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--workers", "2", "--threads", "1", "app.wsgi:application"]
