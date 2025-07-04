FROM python:3.12-slim

WORKDIR /app

COPY app /app/app
COPY tests /app/tests
COPY requirements.txt /app/
# Only copy pytest.ini if it exists
RUN if [ -f pytest.ini ]; then cp pytest.ini /app/; fi

RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"] 