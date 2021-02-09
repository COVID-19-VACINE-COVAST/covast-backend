FROM python:3
WORKDIR /covast
COPY . .
EXPOSE 80
EXPOSE 5432
ENV PYTHONUNBUFFERED 1
RUN pip install -r requirements.txt