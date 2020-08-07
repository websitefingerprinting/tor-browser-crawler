import subprocess
import os
from os import makedirs
from os.path import join, abspath, dirname, pardir
import glob
import argparse
import time
Pardir = abspath(join(dirname(__file__), pardir))

DumpDir = join( Pardir , "parsed")
def parse_arguments():

	parser = argparse.ArgumentParser(description='Crawl Alexa top websites and capture the traffic')

	parser.add_argument('--dir','-d',
						nargs='+',
						type=str,
						metavar='<batch dir>',
						dest = 'dirlist',
						default = [],
						help='bacth folders')
	parser.add_argument('--start','-s',
						type=int,
						metavar='<start ind>',
						default=0,
						help='Start from which site in the list (include this ind).')
	parser.add_argument('--end','-e',
						type=int,
						metavar='<end ind>',
						default=100,
						help='End to which site in the list (exclude this ind).')
	parser.add_argument('-c',
						action='store_true',
						default=False,
						help='Keep a copy of original dataset? (default:False)')
	parser.add_argument('-u',
						action='store_true',
						default=False,
						help='is monitored webpage or unmonitored? (default:is monitored, False)')
	parser.add_argument('--format','-f',
						type=str,
						metavar='<suffix>',
						default='.cell',
						help='suffix of the file')

	# Parse arguments
	args = parser.parse_args()
	return args

def init_directories(start,end, u):
	# Create a results dir if it doesn't exist yet
	if not os.path.exists(DumpDir):
		makedirs(DumpDir)
	if u:
		prefix = "u"
	else:
		prefix = ""
	# Define output directory
	timestamp = time.strftime('%m%d_%H%M%S')
	output_dir = join(DumpDir, prefix+'dataset'+str(start)+'_'+str(end-1)+'_'+timestamp)
	makedirs(output_dir)

	return output_dir

if __name__ == '__main__':
	args = parse_arguments()
	folders = args.dirlist
	raw = []
	for folder in folders:
		raw += glob.glob(join(folder, "*"+args.format))
	print("Total:{}".format(len(raw)))
	output_dir = init_directories(args.start,args.end, args.u)
	counter = [0]*args.end
	# print(raw)
	for r in raw:
		filename = r.split("/")[-1].split(args.format)[0]
		if args.u:
			web_id = filename
			newfilename = filename + args.format
		else:
			web_id,inst_id = filename.split("-")
			new_inst_id = str(counter[int(web_id)])
			newfilename = web_id + "-" + new_inst_id + args.format
		if args.c:
			command = "cp "
		else:
			command = "mv "
		#move pcapfile and time file
		cmd = command + r + " " +join(output_dir, newfilename)
		subprocess.call(cmd, shell=True)
		# cmd = command + r.split(".")[0]+".time" + " " +join(output_dir, newfilename.split(".")[0]+".time")
		# print(cmd)
		# subprocess.call(cmd, shell=True)
		counter[int(web_id)] += 1
	for i in range(len(counter)):
		if counter[i] > 0 :
			print("#{}:{}".format(i, counter[i]))
	print("Merged to {}".format(output_dir))


