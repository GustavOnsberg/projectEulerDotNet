def is_prime(num):
    m = 2
    while m <= num / 2:
        if num % m == 0:
            return False
        else:
            m += 1
    return True


def next_prime(num):
    if num < 2:
        return 2
    if num % 2 == 0:
        num -= 1
    while True:
        num += 2
        if is_prime(num):
            return num


def previous_prime(num):
    while True:
        num -= 1
        if is_prime(num):
            return num


if __name__ == "__main__":
    print(previous_prime(7))
