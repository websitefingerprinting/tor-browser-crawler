import subprocess
import os
from os import makedirs
from os.path import join, abspath, dirname, pardir
import argparse
import time

Pardir = abspath(join(dirname(__file__), pardir))

DumpDir = join(Pardir, "parsed")


def parse_arguments():
    parser = argparse.ArgumentParser(description="Reorder the ids of unmonitored webpage.")

    parser.add_argument('--dir', '-d',
                        type=str,
                        metavar='<dir>',
                        help='bacth folders')
    parser.add_argument('--start', '-s',
                        type=int,
                        metavar='<start ind>',
                        default=0,
                        help='Start from which site in the list (include this ind).')
    parser.add_argument('--end', '-e',
                        type=int,
                        metavar='<end ind>',
                        default=100,
                        help='End to which site in the list (exclude this ind).')
    parser.add_argument('-c',
                        action='store_true',
                        default=False,
                        help='Keep a copy of original dataset? (default:False)')
    parser.add_argument('--format', '-f',
                        type=str,
                        metavar='<suffix>',
                        default='.cell',
                        help='suffix of the file')

    # Parse arguments
    args = parser.parse_args()
    return args


def init_directories(start, end):
    # Create a results dir if it doesn't exist yet
    if not os.path.exists(DumpDir):
        makedirs(DumpDir)
    prefix = "u"

    # Define output directory
    timestamp = time.strftime('%m%d_%H%M%S')
    output_dir = join(DumpDir, prefix + 'dataset' + str(start) + '_' + str(end - 1) + '_' + timestamp)
    makedirs(output_dir)

    return output_dir


if __name__ == '__main__':
    args = parse_arguments()
    dir = args.dir
    flist = []
    cnt = 0
    for i in range(args.start, args.end):
        fname = join(dir, str(i)+args.format)
        if os.path.exists(fname):
            flist.append(fname)
            cnt += 1

    print("Total:{}".format(len(flist)))
    output_dir = init_directories(0, cnt)

    for i,f in enumerate(flist):
        newfilename = str(i) + args.format
        if args.c:
            command = "cp "
        else:
            command = "mv "
        # move pcapfile and time file
        cmd = command + f + " " + join(output_dir, newfilename)
        subprocess.call(cmd, shell=True)

    print("Merged to {}".format(output_dir))
