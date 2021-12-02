import sys
import math
from random import choice

if __name__ == "__main__":

    sentence = sys.argv[1]
    print(''.join(choice((str.upper, str.lower))(c) for c in sentence))
