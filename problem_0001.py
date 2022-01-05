def solve():
    zum = 0
    for x in range(1000):
        if x % 3 == 0 or x % 5 == 0:
            zum += x
    return zum


if __name__ == "__main__":
    print(solve())
