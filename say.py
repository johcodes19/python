from saying import hello, calc
import sys

if len(sys.argv) > 2:
    hello(sys.argv[1])
    print(calc(sys.argv[2]))

