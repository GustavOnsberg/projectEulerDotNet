def solve(n):
    zum = 0
    for x in range(n + 1):
        zum += x ** 2
    zum = sum(range(n+1)) ** 2 - zum
    return zum



if __name__ == "__main__":
    print(solve(100))
