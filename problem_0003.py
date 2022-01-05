import helper.prime_numbers as prime


def solve():
    num = 600851475143
    n = 2
    while True:
        if num % n == 0 and prime.is_prime(num / n):
            return num / n
        else:
            n += 1


if __name__ == "__main__":
    print(solve())
