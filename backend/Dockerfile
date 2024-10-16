FROM python:3.11
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt --no-cache-dir
COPY . .
CMD ["sh", "-c", "sleep 10 && python manage.py runserver 0:8000"]