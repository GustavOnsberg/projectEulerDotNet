import math


def solve(n):
    for a in range(n):
        for b in range(n):
            c = math.sqrt(a ** 2 + b ** 2)
            # print(f"{a} {b} {c}:  {a + b + c}")
            if a + b + c == n and c < a + b:
                return a * b * c



if __name__ == "__main__":
    print(solve(1000))
