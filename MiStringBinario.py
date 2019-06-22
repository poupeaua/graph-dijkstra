import numpy as np
from itertools import product
import logging


def get_k_perm(k):
    """
        Argument:
            k (int) : integer number

        Return:
            symboles_available (array) : array of integer of the 2**k
                different combinations of element formed by string in [0, 1]
                of size k.
    """
    symboles_available = []
    for i, symb in enumerate(product(range(2), repeat=k)):
        cur_str_symbole = ""
        for number in symb:
            cur_str_symbole += str(number)
        symboles_available.append(cur_str_symbole)
    return symboles_available


def compute_k_compl(k):
    """
        Argument:
            k (int) : integer number

        Return:
            k_compl (str) : a minimum string k-complete (not the unique one)
    """
    length = 2**k + k - 1
    k_compl = "0"*k
    # get all permutations EXCEPT all zeros
    symboles_available = get_k_perm(k)[1:]

    for i in range(1, length-k+1):
        tmp_symb = (k_compl+"1")[i:]
        if tmp_symb in symboles_available:
            symboles_available.remove(tmp_symb)
            k_compl += "1"
        else:
            symboles_available.remove((k_compl+"0")[i:])
            k_compl += "0"

    # making sure everything went well
    assert(len(symboles_available) == 0)
    assert(len(k_compl) == length)

    return k_compl


if __name__ == "__main__":
    # input format as asked
    k = int(input())

    print(compute_k_compl(k))
