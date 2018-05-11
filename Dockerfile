FROM python:3
WORKDIR /app
ADD . /app
RUN pip install --trusted-host pypi.python.org -r requirements.txt
CMD [ "python", "./kiwidock.py" ]

