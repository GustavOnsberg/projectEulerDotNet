from math import sqrt

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

seg_size = 20
segs_done = 0
total_segs = 0

end_get_base_url = False


def get_base_mul():
    global end_get_base_url
    global bin_array_0

    if end_get_base_url:
        return -1

    if bin_array_0[0]:
        num = prime_array_0[0]
    else:
        num = 1

    incr = bin_array_0[0]
    bin_array_0[0] = not bin_array_0[0]

    for x in range(1, len(prime_array_0)):
        if bin_array_0[x]:
            num *= prime_array_0[x]
        if not bin_array_0[x - 1] and incr:
            incr = bin_array_0[x]
            bin_array_0[x] = not bin_array_0[x]

    if True not in bin_array_0:
        end_get_base_url = True

    return num


def test_seg(thread_num):
    global psr
    global segs_done

    running = True

    while running:
        base_mul = get_base_mul()
        bin_array = [False] * seg_size
        for _ in range(2 ** seg_size):

            num = base_mul
            if bin_array[0]:
                num *= prime_array_1[0]

            bin_array[0] = not bin_array[0]
            incr = not bin_array[0]

            if num == -1:
                print("seg done")
                return
                running = False
                break

            for x in range(1, seg_size):
                if bin_array[x]:
                    num *= prime_array_1[x]
                if not bin_array[x - 1] and incr:
                    bin_array[x] = not bin_array[x]
                    incr = not bin_array[x]

            if psr < num <= sq:
                psr = num
                print(f"PSR updated: {psr}")

        segs_done += 1
        progress = segs_done / total_segs
        time_s = int((1 - progress) / progress * (time() - start_time))
        time_m = int(time_s / 60)
        time_s = time_s % 60
        time_h = int(time_m / 60)
        time_m = time_m % 60
        time_d = int(time_h / 24)
        time_h = time_h % 24
        print(f"{(progress * 100):.5f}% - {time_d}d {time_h:02d}d {time_m:02d}m {time_s:02d}s")


def solve(n, t):
    global prime_array_0
    global bin_array_0
    global prime_array_1
    global bin_array_1
    global p
    global sq
    global total_segs

    prime_array_0 = [2]
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
    total_segs = 2 ** len(prime_array_0)

    threads = []

    for x in range(t):
        threads.append(threading.Thread(target=test_seg, args=(x,)))
        threads[x].start()
        print(f"created thread: {x}")

    for x in range(t):
        threads[x].join()

    return 1


if __name__ == "__main__":
    start_time = time()
    solve(190, 16)
    print(f"{psr=}")


def run(t):
    global start_time
    start_time = time()
    solve(190, t)
    print(f"{psr=}")