FROM python:3.10

COPY requirements.txt requirements.txt

COPY /sql_app/ /sql_app/

RUN pip install --no-cache-dir --upgrade -r requirements.txt

CMD ["uvicorn", "sql_app.main:app", "--host", "0.0.0.0", "--port", "90"]
