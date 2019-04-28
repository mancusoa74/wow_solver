# Words of Wonder solver v0.1
#
# Antonio Mancuso
#
# 28/04/2019

import itertools as it
import argparse


def solve(args):
    dizio = {}
    with open('wow_dict.txt') as f:
        for line in f.readlines():
            word = line.rstrip()
            dizio[word] = len(word)

    words = it.permutations(args.c, int(args.l))
    for w in words:
        word = ''.join(list(w))
        if word in dizio:
            if args.cp:
                if word[int(args.cp) - 1] == args.cc:
                    print(word)
            else:
                print(word)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Help to solve Words of \
                                                  Wonders puzzle game')
    parser.add_argument('-c', help='characters of the puzzle', required=True)
    parser.add_argument('-l', help='length of the word <3..6>', required=True)
    parser.add_argument('-cp', help='character constraint position')
    parser.add_argument('-cc', help='character constraint')

    args = parser.parse_args()
    solve(args)
