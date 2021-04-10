FROM python:3.8-slim-buster as build

WORKDIR /app

RUN apt-get update && \
    apt-get -y upgrade && \
    apt-get -y install -q build-essential wget && \
    apt-get -y install -q python-dev libffi-dev libssl-dev python-pip

RUN cd /tmp && \
    wget https://artiya4u.keybase.pub/TA-lib/ta-lib-0.4.0-src.tar.gz && \
    tar -xvf ta-lib-0.4.0-src.tar.gz && \
    cd ta-lib/ && \
    ./configure --prefix=/usr && \
    make && \
    make install

ADD ./app/requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

ENV PYTHONUNBUFFERED=1

# Cleanup
RUN devpackages=`dpkg -l|grep '\-dev'|awk '{print $2}'|xargs` \
  && DEBIAN_FRONTEND=noninteractive apt-get -y remove --purge \
    build-essential \
    ${devpackages} \
  && apt-get purge -y --auto-remove \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/* \
  && rm -rf /tmp/* \
  && rm -rf /var/tmp/*

# Pack Image
FROM scratch
COPY --from=build / .

ADD ./app /

CMD ["python","-u","bot.py"]