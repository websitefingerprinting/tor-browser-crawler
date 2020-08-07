# This dockerfile allows to run an crawl inside a docker container

# Pull base image.
#FROM ubuntu:18.04
FROM python:3.6

# Install required packages.
RUN apt-get update
RUN DEBIAN_FRONTEND=noninteractive apt-get --assume-yes --yes install sudo build-essential autoconf git zip unzip xz-utils apt-utils psmisc
RUN DEBIAN_FRONTEND=noninteractive apt-get --assume-yes --yes install firefox-esr
RUN DEBIAN_FRONTEND=noninteractive apt-get --assume-yes --yes install libtool libevent-dev libssl-dev zlib1g zlib1g-dev
RUN DEBIAN_FRONTEND=noninteractive apt-get --assume-yes --yes install python3 python3-dev python3-setuptools python3-pip
RUN DEBIAN_FRONTEND=noninteractive apt-get --assume-yes --yes install net-tools ethtool tshark libpcap-dev iw tcpdump
RUN DEBIAN_FRONTEND=noninteractive apt-get --assume-yes --yes install xvfb x11-utils
RUN apt-get clean \
	&& rm -rf /var/lib/apt/lists/*


# Install python requirements.
RUN pip install --upgrade pip
COPY requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt

# add host user to container
RUN adduser --system --group --disabled-password --gecos '' --shell /bin/bash docker

# download geckodriver
ADD https://github.com/mozilla/geckodriver/releases/download/v0.27.0/geckodriver-v0.27.0-linux64.tar.gz /bin/
RUN tar -zxvf /bin/geckodriver* -C /bin/
ENV PATH /bin/geckodriver:$PATH

# add setup.py
RUN git clone https://gist.github.com/websitefingerprinting/b4d306f80aa083508fb4c569c5b27b08.git /home/docker/tbb_setup
RUN python /home/docker/tbb_setup/setup.py 9.5.3

# Set the display
ENV DISPLAY $DISPLAY
