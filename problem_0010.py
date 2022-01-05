from helper.prime_numbers import next_prime

def solve(n):
    zum = 0
    i = 2
    m = 10000
    while i < n:
        if i > m:
            print(f"m: {i}")
            m += 10000
        zum += i
        i = next_prime(i)
    return zum



if __name__ == "__main__":
    print(solve(2000000))
