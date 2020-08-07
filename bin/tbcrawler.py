#!/usr/bin/env python2
# From: https://gitweb.torproject.org/pluggable-transports/obfsproxy.git/tree/bin/obfsproxy
import sys, os
import datetime
from tbcrawler.utils import sendmail
# Forcerfully add root directory of the project to our path.
# http://www.py2exe.org/index.cgi/WhereAmI
if hasattr(sys, "frozen"):
    dir_of_executable = os.path.dirname(sys.executable)
else:
    dir_of_executable = os.path.dirname(__file__)
path_to_project_root = os.path.abspath(os.path.join(dir_of_executable, '..'))

sys.path.insert(0, path_to_project_root)

from tbcrawler.pytbcrawler import run


try:
    run()
    msg = "'Crawler Message:Crawl done at {}!'".format(datetime.datetime.now())
    sendmail(msg)
except KeyboardInterrupt:
    sys.exit(-1)
except Exception as e:
    msg = "'Crawler Message: An error occurred:\n{}'".format(e)
    sendmail(msg)