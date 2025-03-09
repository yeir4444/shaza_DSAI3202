from mpi4py import MPI
import numpy as np
import time


def compute_squares(start_idx, end_idx):
    # Instead of returning a huge list, just return the max square
    return (end_idx - 1) ** 2
