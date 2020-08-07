import argparse
import sys

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--x', type=float, default = 1.0, help = 'what is the first number?')
    parser.add_argument('--y', type=float, default = 1.0, help = 'what is the 2nd number?')
    parser.add_argument('--operation', type=str, default = 1.0, help = 'what is the operation string?')
    args = parser.parse_args()
    sys.stdout.write(str(calc(args))) #useing argparse

def calc(args):
    if args.operation == 'add':
        return args.x + args.y
    elif args.operation == 'sub':
        return args.x - args.y
    elif args.operation == 'mul':
        return args.x * args.y
    elif args.operation == 'div':
        return args.x / args.y

if __name__ == '__main__':
    main()
