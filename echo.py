import sys


def parse_args():
    result = ""

    for arg in sys.argv[1:]:
            result += arg + " "           
    return result.rstrip()


print(parse_args())

#print(help(str))