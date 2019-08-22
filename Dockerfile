FROM python:3.7

WORKDIR /Money-bot

COPY requirements.txt /Money-bot

RUN pip install --no-cache-dir -r requirements.txt

COPY . /Money-bot

CMD ["python", "-m", "money_bot"]
