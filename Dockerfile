FROM python:3

# USER app
ENV PYTHONUNBUFFERED 1
RUN mkdir /app
WORKDIR /app
ADD requirements.txt /app
RUN pip install -r requirements.txt
ADD . /app
CMD gunicorn app:app --bind 0.0.0.0:$PORT --reload
