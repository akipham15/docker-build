FROM python:3.12
ADD . /app
WORKDIR /app
RUN python -m pip install --upgrade pip 
RUN pip install --upgrade pipenv
RUN pipenv install --system
