FROM python:3.10
RUN pip install --no-cache-dir --upgrade -r requirements.txt
CMD ["python", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
