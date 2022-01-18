from math import sqrt

import numpy as np

from helper.prime_numbers import *
from time import time
import threading

prime_array_0 = []
bin_array_0 = []
prime_array_1 = []
bin_array_1 = []
p = 0
start_time = 0
sq = 0
psr = 0

seg_size = 1

end_get_base_url = False


def get_base_mul():
    global end_get_base_url
    if end_get_base_url:
        return -1

    global bin_array_0

    bin_array_0[0] = not bin_array_0[0]
    incr = not bin_array_0[0]

    if bin_array_0[0]:
        num = prime_array_0[0]
    else:
        num = 1

    for x in range(1, len(prime_array_0)):
        if not bin_array_0[x - 1] and incr:
            bin_array_0[x] = not bin_array_0[x]
            incr = not bin_array_0[x]
        if bin_array_0[x]:
            num *= prime_array_0[x]

    if True not in bin_array_0:
        end_get_base_url = True

    return num


def test_seg():
    global psr

    running = True

    while running:
        bin_array = [False] * seg_size
        for _ in range(2 ** seg_size):
            bin_array[0] = not bin_array[0]
            incr = not bin_array[0]

            num = get_base_mul()

            if num == -1:
                print("seg done")
                running = False
                break

            if bin_array[0]:
                num *= prime_array_1[0]

            for x in range(1, len(prime_array_1)):
                if not bin_array[x - 1] and incr:
                    bin_array[x] = not bin_array[x]
                    incr = not bin_array[x]
                if bin_array[x]:
                    num *= prime_array_1[x]

            if psr < num <= sq:
                psr = num
                print(f"PSR updated: {psr}")


def solve(n):
    global prime_array_0
    global bin_array_0
    global prime_array_1
    global bin_array_1
    global p
    global sq

    prime_array_0 = [2]
    bin_array_0 = [False]
    p = 2

    i = next_prime(2)

    while i < n:
        p *= i
        prime_array_0.append(i)
        i = next_prime(i)

    sq = int(sqrt(p))
    print(f"{prime_array_0=} {p=} {sq=}")

    prime_array_1 = prime_array_0[-seg_size:]
    prime_array_0 = prime_array_0[:-seg_size]

    print(f"{prime_array_0=} {prime_array_1=}")

    bin_array_0 = [False] * len(prime_array_0)
    total_runs = 2 ** len(prime_array_0)

    test_seg()

    return 1


if __name__ == "__main__":
    start_time = time()
    print(solve(80))
