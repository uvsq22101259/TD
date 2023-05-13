#!/usr/bin/python3

import argparse
import queue
import random
import sys

def fifo_routine(page_list, num_frames):
    """
    Implementation of a FIFO routine.

    Sizes of page_list and output are the same.
    Do not consider releasing the last accessed pages frames.

    input:  page_list       list of accessed pages, in order
            num_frames      number of available frames ie. memory spaces
    output: list of page movements where
            [(A, _), (B, A), (_, B)] means that:
            - A is loaded in a space and nothing was evicted;
            - then B is loaded in place of A;
            - then nothing is loaded but B space is released.
    """
    raise NotImplementedError

def random_routine(page_list, num_frames):
    """
    Implementation of random routine.
    Same inputs/output as fifo_routine.
    """
    raise NotImplementedError

def lru_routine(page_list, num_frames):
    """
    Implementation of LRU routine.
    Same inputs/output as fifo_routine.
    """
    raise NotImplementedError

def chance_routine(page_list, num_frames):
    """
    Implementation of second chance routine.
    Same inputs/output as fifo_routine.
    """
    raise NotImplementedError

def belady_routine(page_list, num_frames):
    """
    Implementation of belady routine.
    Same inputs/output as fifo_routine.
    """
    raise NotImplementedError

# DO NOT MODIFY THE PART BELOW

def __check_positive(value):
    ivalue = int(value)
    if ivalue <= 0:
        raise argparse.ArgumentTypeError("%s is not a strict positive value" %
                                         (value))
    return ivalue

if __name__ == '__main__':
    NAME_TO_FUNC = {
        "fifo":     fifo_routine,
        "random":   random_routine,
        "lru":      lru_routine,
        "chance":   chance_routine,
        "belady":   belady_routine,
    }
    
    # Command line parsing, execute `./schedmem.py -h for more information
    AP = argparse.ArgumentParser()
    AP.add_argument('-a', '--algo', help='algorithm to use',
                    default='fifo', choices=NAME_TO_FUNC.keys())
    AP.add_argument('-n', '--nb-frames', help='number of page frames',
                    default=3, type=__check_positive)
    AP.add_argument('input', help='file which contains the accessed page list')
    args = AP.parse_args(sys.argv[1::])

    # Input file parsing
    with open(args.input) as input_file:
        page_list = [x for x in input_file.readline().strip()]

    res = NAME_TO_FUNC[args.algo](page_list, args.nb_frames)

    print(res)
