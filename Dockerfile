FROM python:3.8.2-slim

WORKDIR /usr/app/src

COPY Pipfile* ./

RUN pipenv install

COPY app.py ./

CMD ["sh", "-c", "streamlit run --server.port $PORT /usr/app/src/app.py"]