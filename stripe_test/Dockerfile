FROM python:3.10-slim

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt --no-cache-dir

CMD ["python", "manage.py", "runserver", "0:8000"]