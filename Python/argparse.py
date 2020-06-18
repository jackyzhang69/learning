import argparse
import sys

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--noc',type=str,default='0013',help='input the noc code')
    parser.add_argument('--area',type=int,default=77,help='input the area index')
    parser.add_argument('--m',type=str,default='main duties',help='get main duties')
    args=parser.parse_args()
    do_something(args)


def do_something(args):
    print(args.noc,args.area,args.m)


if __name__=='__main__':
    main()

