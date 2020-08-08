all: build test stop

# this is to forward X apps to host:
# See: http://stackoverflow.com/a/25280523/1336939
XSOCK=/tmp/.X11-unix
XAUTH=/tmp/.docker.xauth

# paths
TBB_PATH=/home/docker/tbcrawl/tor-browser_en-US/
CRAWL_PATH=/home/docker/tbcrawl
DPBURST_PATH=/home/docker/dpburst
RANDOM_WT_PATH=/home/docker/random_wt
GUEST_SSH=/home/docker/.ssh
HOST_SSH=${HOME}/.ssh

ENV_VARS = \
	--env="DISPLAY=${DISPLAY}" 					\
	--env="XAUTHORITY=${XAUTH}"					\
	--env="VIRTUAL_DISPLAY=$(VIRTUAL_DISPLAY)"  \
	--env="START_XVFB=false"                    \
	--env="TBB_PATH=${TBB_PATH}"
VOLUMES = \
	--volume=${XSOCK}:${XSOCK}					\
	--volume=${XAUTH}:${XAUTH}					\
	--volume=${HOST_SSH}:${GUEST_SSH}			\
	--volume=`pwd`:${CRAWL_PATH}				\
	--volume=${HOME}/adaptiveBurstPadding:${DPBURST_PATH}	\
	--volume=${HOME}/walkietalkie:${RANDOM_WT_PATH}	        \
# network interface on which to listen
DEVICE=eth0

tag=tbb
# commandline arguments

## mon sites
## undefended
# CRAWL_PARAMS=-c wang_and_goldberg -u ./sites/sites.txt -s -v -p -t --stop 100
## DP-Burst
# CRAWL_PARAMS=-c dpburst -u ./sites/sites.txt -s -v -p -t -m --stop 100
# CRAWL_PARAMS=-c random_wt -u ./sites/sites.txt -s -v -p -t -m --stop 100

#unmon sites
## undefended
# CRAWL_PARAMS=-c wang_and_goldberg -u ./sites/unmon_sites.txt -s -v -p --stop 10000
## DP-Burst
# CRAWL_PARAMS=-c dpburst -u ./sites/unmon_sites.txt -s -v -p -m --stop 10000
# CRAWL_PARAMS=-c random_wt -u ./sites/unmon_sites.txt -s -v -p -m --stop 10000

# Make routines
build:
	@docker build -t tbcrawl --rm .

run:
	@docker run -it --rm --name ${tag} ${ENV_VARS} ${VOLUMES} --net bridge --privileged \
	tbcrawl ${CRAWL_PATH}/Entrypoint.sh "./bin/tbcrawler.py $(CRAWL_PARAMS)" ${DEVICE}

shell:
	@docker run -it --rm ${ENV_VARS} ${VOLUMES} --net bridge --privileged \
	tbcrawl /bin/bash

stop:
	@docker stop `docker ps -a -q -f ancestor=tbcrawl`
	@docker rm `docker ps -a -q -f ancestor=tbcrawl`

destroy:
	@docker rmi -f tbcrawl

reset: stop destroy
