from src.core import Core
import argparse
import os

def displayProgress():
    pass

def displayFinished():
    pass

parser = argparse.ArgumentParser(description='This program is designed to perform a regular expression search on a dataset of mess\
ages supplied form a input file. Found results can beadditionally checked with a functions implemented in Python language. A dicti\
on-ary search which checks if a string matched with regular expression belongs to aprovided wordlist can also be performed.')
parser.add_argument('reg', metavar='S', type=str, nargs='+', help='Strings representing desired types of search: ipv4 - IPv4 address,\
 ipv6 - IPv6 address, socialsec - National identification number, id_number - Serial number of the identification document, mac- MAC address\
, domain - Domain address, email - Email address, password - Potential passwords, login - Potential logins, phone_number - Phone numbers')
parser.add_argument('-i', type=str, help='Path of the input file.', required=True)
parser.add_argument('-o', type=str, help='Path of the output file. If empty the output is saved to the input path appended with "_output" suffix.')
parser.add_argument('-d', type=str, help='Path of the dictionary file')
parser.add_argument('-a', action='store_true', help='Enables additional searches.')
args = parser.parse_args()

if args.o is None:
    inPath = args.i
    args.o = os.path.splitext(inPath)[0] + "_output.json"
    print("Input path set to ", args.o)

core = Core(args.i, args.o, expectedRegexes=args.reg, additional=args.a, progressEvent=displayProgress, finishedEvent=displayFinished) 
core.start()
core.join()
