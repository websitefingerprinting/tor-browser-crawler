from os.path import join, dirname, abspath, pardir
from time import strftime

# defaults for batch and instance numbers
NUM_BATCHES = 10
NUM_INSTANCES = 4
MAX_SITES_PER_TOR_PROCESS = 100  # reset tor process after crawling 100 sites

# max dumpcap size in KB
MAX_DUMP_SIZE = 30000
# max filename length
MAX_FNAME_LENGTH = 200
STREAM_CLOSE_TIMEOUT = 20  # wait 20 seconds before raising an alarm signal
# otherwise we had many cases where get_streams hanged

# timeouts
SOFT_VISIT_TIMEOUT = 60     # timeout used by selenium
HARD_VISIT_TIMEOUT = 80     # hard timeout used by process


DEFAULT_SOCKS_PORT = 9051

# virtual display dimensions
# W = width of the virtual display
# H = height of the virtual display
DEFAULT_XVFB_WIN_W = 1280
DEFAULT_XVFB_WIN_H = 800

# Default paths
BASE_DIR = abspath(join(dirname(__file__), pardir))
CONFIG_FILE = join(BASE_DIR, 'config.ini')
RESULTS_DIR = join(BASE_DIR, 'results')
CONFIG_DIR = join(BASE_DIR, 'config')
DEFAULT_CONFIG_DIR = join(CONFIG_DIR, "default")
TORRC_FILE = join(DEFAULT_CONFIG_DIR, 'torrc')
FFPREF_FILE = join(DEFAULT_CONFIG_DIR, 'ffprefs')
SRC_DIR = join(BASE_DIR, 'tbcrawler')
CRAWL_DIR = join(RESULTS_DIR, strftime('%y%m%d_%H%M%S'))
LOGS_DIR = join(CRAWL_DIR, 'logs')
DEFAULT_CRAWL_LOG = join(LOGS_DIR, 'crawl.log')
DEFAULT_TOR_LOG = join(LOGS_DIR, 'tor.log')
DEFAULT_FF_LOG = join(LOGS_DIR, 'ff.log')
TEST_DIR = join(SRC_DIR, 'test')
TBB_DIR = join(BASE_DIR, 'tor-browser_en-US')
SITE_LIST = join(BASE_DIR, "sites.txt")

# PCAP capture filter
LOCALHOST_IP = "127.0.0.1"  # default localhost IP
DEFAULT_FILTER = 'tcp and not host %s and not tcp port 22 and not tcp port 20' % LOCALHOST_IP

#Hard-coded bridge IP
My_Bridge_Ips = ['13.75.78.82', '52.175.31.228', '23.100.88.30','40.83.88.194']

SENDMAILPYDIR = join(BASE_DIR, "private/sendmail.py")
PARSERPYDIR = join(BASE_DIR, "dataprocessing/parser.py")
class TimeoutException(Exception):
    pass


class HardTimeoutException(Exception):
    pass
