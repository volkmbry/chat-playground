FROM python:3.8.2-slim
EXPOSE 8501

WORKDIR /usr/app

COPY Pipfile* ./

RUN pip install pipenv==2021.11.23
RUN pipenv install --system

COPY . .

CMD ["streamlit", "run", "/usr/app/app.py"]