FROM python:3.11.4-slim-bullseye

WORKDIR /app

COPY requirements.txt setup.py config.ini ./
COPY ist ./ist

RUN pip install -r requirements.txt
RUN python setup.py install

CMD ["ist"]