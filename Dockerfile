FROM python:3
RUN mkdir /app
ADD . /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 9000
CMD ["python", "main.py"]