FROM python:3.13-slim

WORKDIR /app

COPY . .
RUN pip install --no-cache-dir -r requirements.txt

CMD ["hypercorn", "main:app", "-b 0.0.0.0:6000"]
