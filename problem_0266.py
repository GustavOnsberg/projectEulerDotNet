from math import sqrt

from helper.prime_numbers import *


def get_psr(n):
    i = int(sqrt(n))
    last_mod = n % (i + 1)
    counter = 0

    while True:
        mod = n % i
        mod_diff = mod - last_mod
        mod_to_i = i - mod
        mod_diff_times = int(mod_to_i / mod_diff * 0.8)

        print(f"{i} : {mod} : {mod_diff} : {mod_diff_times}")

        if mod_diff_times < 3:
            mod_diff_times = 1

        last_mod = mod

        if mod == 0:
            print(f"counter: {counter}")
            return i

        i -= mod_diff_times
        counter += 1


def solve(n):
    p = 1
    i = next_prime(0)
    while i < n:
        p *= i
        i = next_prime(i)
    print(f"p: {p}")
    return get_psr(p)


if __name__ == "__main__":
    print(solve(40))
