FROM python:3-alpine


COPY requirements.txt .

RUN  apk --update add postgresql-dev \
  && apk --update add --virtual build-dependencies gcc python3-dev musl-dev \
  && pip3 install --no-cache-dir -r requirements.txt \
  && apk del build-dependencies

ENV DB db

WORKDIR /usr/src/app
VOLUME /usr/src/app

EXPOSE 8080
ENTRYPOINT ["python3"]
CMD ["-m", "swagger_server"]
