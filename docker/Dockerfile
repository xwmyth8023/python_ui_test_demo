#image from ubuntu:xenial
FROM ubuntu:latest

#user is root
USER root

# install ca-certificates,curl, wget, bzip2, unzip xz-utils
RUN apt-get update && apt-get install -y --no-install-recommends \
		ca-certificates \
		curl \
		wget \
		bzip2 \
		unzip \
		xz-utils \
	&& rm -rf /var/lib/apt/lists/*

#install firefox
RUN apt-get update \
    && apt-get install -y \
        libxcomposite-dev \
        libasound2-dev \
        libdbus-glib-1-dev \
        libgtk2.0-0 \
	      libgtk-3-dev \
    && wget --no-verbose -O /tmp/firefox.tar.bz2 https://ftp.mozilla.org/pub/firefox/releases/67.0b5/linux-x86_64/en-US/firefox-67.0b5.tar.bz2 \
    && rm -rf /opt/firefox \
    && tar -C /opt -xjf /tmp/firefox.tar.bz2 \
    && rm /tmp/firefox.tar.bz2 \
    && mv /opt/firefox /opt/firefox-67.0b5 \
    && ln -fs /opt/firefox-67.0b5/firefox /usr/local/bin/firefox

#install chrome
RUN \
    apt-get -yq install gconf-service libgconf-2-4 libpango1.0-0 fonts-liberation xdg-utils libasound2 libappindicator3-1 libnspr4 libnss3 lsb-release && \
    apt-get -yq install libxss1 libappindicator1 libindicator7 &&   \
    wget --no-verbose -O /tmp/google-chrome.deb https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb &&  \
    dpkg -i /tmp/google-chrome.deb &&   \
    apt-get install -f &&   \
    echo GOOGLE CHROME INSTALLED


#install python
RUN \
  echo INSTALLING PYTHON && \
  apt-get -y install python3 && \
  apt-get install python3-pip -y && \
  rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*


WORKDIR /app

ADD . /app

RUN pip3 install -r requirement.txt

CMD [ "python3", "test_runner.py"]
    

