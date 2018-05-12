FROM python:2.7-slim
WORKDIR /app
ADD . /app
RUN apt-get update
RUN apt-get install salt-minion --assume-yes
RUN /usr/bin/salt-call --local -l debug --file-root=/app/salt-states --pillar-root=/app/salt-pillar state.highstate 2>&1 | tee /app/state.highstate.log
CMD [ "python", "./kiwidock.py" ]

