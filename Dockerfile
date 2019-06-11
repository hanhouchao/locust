FROM index.alauda.cn/alaudaorg/alaudabase-alpine-run:alpine3.9.3
MAINTAINER hchan@alauda.io

RUN apk --no-cache --update add python3 vim curl python3-dev bash gcc musl-dev

COPY requirements.txt .
RUN pip3 install --upgrade pip && pip3 install -r /requirements.txt

WORKDIR /app/
COPY . /app

CMD ["bash", "/app/run.sh"]

