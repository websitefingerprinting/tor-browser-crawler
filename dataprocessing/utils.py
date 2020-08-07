from os import makedirs
import os

def init_directories(path):
    # Create a results dir if it doesn't exist yet
    if not os.path.exists(path):
        makedirs(path)


def getTimestamp(pkt, t0):
    return float(pkt.time - t0)


def getDirection(pkt):
    if pkt.payload.src in My_Source_Ips:
        return 1
    else:
        return -1
def init_directories(path):
    # Create a results dir if it doesn't exist yet
    if not os.path.exists(path):
        makedirs(path)
My_Bridge_Ips = ['13.75.78.82', '52.175.31.228', '52.175.49.114','40.83.88.194', '13.94.61.159']
My_Source_Ips = {
'10.0.0.4',
'10.0.0.5',
'10.0.0.6',
'10.0.0.7',
'10.0.1.4',
'10.0.1.5',
'10.0.1.6',
'10.0.1.8',
'172.17.0.1',
'172.17.0.2',
'172.17.0.3',
'172.17.0.4',
'172.17.0.5',
'172.17.0.6',
'172.17.0.7',
'172.17.0.8',
}