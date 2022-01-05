import helper.prime_numbers as prime


def solve(n):
    i = 0
    p = 0
    while i <= n:
        i += 1
        p = prime.next_prime(p)
        if i % 1000 == 0:
            print(f"{i}th: {p}")
    return p



if __name__ == "__main__":
    print(solve(10001))
