# Note that this class is mainly to play with the output
# I will write separate test classes in the future.
from enrep import *
from permutation import Permutation

import sys


def enrep_main():
    nrep = Enrep("ABC", mode=UPTO_LENGTH)

    for i in nrep.generate_words():
        print(i)


def permutation_main():
    permut = Permutation("WORD")
    for i in permut.generate_words():
        print(i)

def count_main():
    k = Count(10)

    def increment():
        k.set_number([0])
        print(k.get_digits())
        for i in range(10):
            print(k.increment_by(5))

    def decrement():
        k.set_number([5, 0])
        print(k.get_digits())
        for i in range(10):
            print(k.decrement_by(5))

    # increment()
    decrement()

if __name__ == '__main__':
    args = sys.argv[1:]
    if not len(args):
        print(
            "Not capable of reading minds yet.\n"
            "Please specify valid arguments.\n"
        )

    elif args[0] == "enrep":
        enrep_main()

    elif args[0] == "permutation":
        permutation_main()

    elif args[0] == "count":
        count_main()
