FROM python:3.12

WORKDIR /app

COPY . .

RUN pip install --upgrade pip && pip install -r req.txt

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
